# Photos to Video Transition Generator

This FastAPI application allows you to create captivating video
transitions between two photos. It\'s a handy tool for social media
creators, enabling you to quickly generate engaging content for
platforms like Instagram Reels, TikTok, YouTube Shorts, and other short
video platforms.

## How It Works

1.  The application takes two photo URLs as input: a raw photo and an
    edited photo.
2.  It downloads the photos from the provided URLs and checks if they
    have the same dimensions.
3.  A video is generated with a dynamic transition effect between the
    two photos. You can choose between left-to-right wipe-out transition
    and other transition effects.
4.  The generated video is saved with a unique filename and can be
    accessed through a URL.

## How to Use

### Prerequisites

- Python 3.7 or higher
- Git

### Clone the Repository

    git clone https://github.com/kumardeepam/photos_to_video.git

### Run the FastAPI Application

1.  Navigate to the cloned repository directory:
2.  Install the required Python dependencies:
3.  Start the FastAPI application:

The application should now be running locally at
<http://localhost:8000>.

### Access the Swagger API Documentation

1.  Open your web browser.
2.  Access the Swagger API documentation by navigating to:

This will open Swagger UI, which provides interactive documentation for
the API.

### Use the API

1.  In Swagger UI, you can explore the available endpoints, such as
    `/create_transition_video`.
2.  Click on the endpoint to expand it and see details about the request
    and response.
3.  To use the API, click the \"Try it out\" button, provide the
    required input (raw and edited photo URLs), and click \"Execute.\"
    The API will respond with the result, including a URL link to the
    generated video.
4.  You can access the generated video by opening the provided URL in
    your browser or downloading it for your social media content.

## Usefulness

This code can be incredibly useful for social media creators and
marketers looking to create eye-catching and engaging content for short
video platforms. Here are some ways it can benefit you:

- **Save Time**: Instead of manually creating transition videos
  between photos, you can automate the process with this tool, saving
  you time and effort.
- **Engagement**: Engaging transitions between photos can help capture
  the viewer\'s attention and make your content more shareable.
- **Customization**: You can easily customize the transition effect to
  match your branding and style.
- **Variety**: With the option to choose different transition effects,
  you can keep your content fresh and experiment with various styles.
- **Platform Compatibility**: The generated videos are suitable for
  various short video platforms, making it versatile for your content
  strategy.
- **Content Creation**: Whether you\'re a social media influencer,
  content creator, or marketer, this tool can enhance your content
  creation capabilities.

Start creating captivating short videos for your social media channels
today with the Photos to Video Transition Generator!

## License

This project is licensed under the MIT License. See the
[LICENSE](LICENSE) file for details.
