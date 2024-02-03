from fastapi import FastAPI
from typing import List
import cv2
import numpy as np
import tempfile
import os
import shutil
from pydantic import BaseModel
import requests
from io import BytesIO
from starlette.staticfiles import StaticFiles
import uuid

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class PhotoURL(BaseModel):
    raw_photo_url: str
    edited_photo_url: str

# Function to add watermark text to an image
def add_watermark(image, text, position, font, font_scale, font_thickness):
    # print(image, text, position, font, font_scale, font_thickness)
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    # print(text_size)
    text_x = position[0] - text_size[0]
    text_y = position[1] + text_size[1]
    # print(text_x, text_y)
    cv2.putText(image, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)
    return image


@app.get("/")
def read_root():
    return {"message": "Photos to Instagram Reel generator!"}

# input url exaample
# {
#   "raw_photo_url": "https://gcdnb.pbrd.co/images/Cnkd6ZQvnNW7.jpg",
#   "edited_photo_url": "https://gcdnb.pbrd.co/images/PivPTG9fqAxe.jpg"
# }
# {
#   "raw_photo_url": "https://gcdnb.pbrd.co/images/4TkOnJ9MNZ8n.jpg",
#   "edited_photo_url": "https://gcdnb.pbrd.co/images/kc1uB5he3039.jpg"
# }

@app.post("/create_transition_video")
async def create_transition_video(photos: PhotoURL):
    temp_dir = tempfile.mkdtemp()
    raw_photo_path = os.path.join(temp_dir, "raw_photo.jpg")
    edited_photo_path = os.path.join(temp_dir, "edited_photo.jpg")

    try:
        raw_photo_response = requests.get(photos.raw_photo_url)
        edited_photo_response = requests.get(photos.edited_photo_url)

        if raw_photo_response.status_code != 200 or edited_photo_response.status_code != 200:
            return {"error": "Failed to download photos from the provided URLs."}

        with open(raw_photo_path, "wb") as raw_photo_file:
            raw_photo_file.write(raw_photo_response.content)

        with open(edited_photo_path, "wb") as edited_photo_file:
            edited_photo_file.write(edited_photo_response.content)

        raw_img = cv2.imread(raw_photo_path)
        edited_img = cv2.imread(edited_photo_path)

        if raw_img.shape != edited_img.shape:
            return {"error": "Both photos must have the same dimensions."}

        frame_height, frame_width, _ = raw_img.shape
        video_filename = f"{uuid.uuid4().hex}.mp4"
        output_video_path = os.path.join(temp_dir, video_filename)
        # fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fourcc = cv2.VideoWriter_fourcc(*"avc1")


        
        out = cv2.VideoWriter(output_video_path, fourcc,
                              30, (frame_width, frame_height))
        
        # Define watermark properties
        print(frame_width)
        print(frame_height)
        watermark_text = "created with instareel.app"
        watermark_position = (frame_width - 1300, frame_height - 1100)  # Adjust x offset to match your frame size
        # watermark_position = (10, frame_height - 650)  # Adjust x offset to match your frame size

        watermark_font = cv2.FONT_HERSHEY_SIMPLEX
        watermark_font_scale = 2
        watermark_font_thickness = 3

        # Generate frames for the video with a left to right wipe out transition
        num_frames = 150
        for frame_number in range(num_frames):
            progress = frame_number / num_frames  # Transition progress
            wipe_line = int(frame_width * progress)  # Line position

            # Create a frame with the wipe effect
            frame = raw_img.copy()
            frame[:, :wipe_line] = edited_img[:, :wipe_line]

            # Add watermark to the frame
            frame = add_watermark(frame, watermark_text, watermark_position,
                              watermark_font, watermark_font_scale, watermark_font_thickness)


            out.write(frame)

        out.release()

        generated_video_dir = os.path.join("static", "generated-videos")
        os.makedirs(generated_video_dir, exist_ok=True)
        generated_video_path = os.path.join(
            generated_video_dir, video_filename)
        shutil.move(output_video_path, generated_video_path)

        video_url = f"/static/generated-videos/{video_filename}"
        return {"video_url": video_url}

    finally:
        shutil.rmtree(temp_dir)
