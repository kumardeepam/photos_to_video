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
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_video_path, fourcc,
                              30, (frame_width, frame_height))

        # Generate frames for the video with a left to right wipe out transition
        num_frames = 150
        for frame_number in range(num_frames):
            progress = frame_number / num_frames  # Transition progress
            wipe_line = int(frame_width * progress)  # Line position

            # Create a frame with the wipe effect
            frame = raw_img.copy()
            frame[:, :wipe_line] = edited_img[:, :wipe_line]

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
