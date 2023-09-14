<!DOCTYPE html>
<html>

<head>
    <title>Photos to Video Transition Generator</title>
</head>

<body>
    <h1>Photos to Video Transition Generator</h1>

    <p>This FastAPI application allows you to create captivating video transitions between two photos. It's a handy tool for social media creators, enabling you to quickly generate engaging content for platforms like Instagram Reels, TikTok, YouTube Shorts, and other short video platforms.</p>

    <h2>How It Works</h2>

    <ol>
        <li>The application takes two photo URLs as input: a raw photo and an edited photo.</li>
        <li>It downloads the photos from the provided URLs and checks if they have the same dimensions.</li>
        <li>A video is generated with a dynamic transition effect between the two photos. You can choose between left-to-right wipe-out transition and other transition effects.</li>
        <li>The generated video is saved with a unique filename and can be accessed through a URL.</li>
    </ol>

    <h2>How to Use</h2>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.7 or higher</li>
        <li>Git</li>
    </ul>

    <h3>Clone the Repository</h3>

    <pre><code>git clone https://github.com/kumardeepam/photos_to_video.git</code></pre>

    <h3>Run the FastAPI Application</h3>

    <ol>
        <li>Navigate to the cloned repository directory:</li>
        <pre><code>cd photos_to_video</code></pre>
        <li>Install the required Python dependencies:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
        <li>Start the FastAPI application:</li>
        <pre><code>uvicorn main:app --reload</code></pre>
    </ol>

    <p>The application should now be running locally at <a href="http://localhost:8000">http://localhost:8000</a>.</p>

    <h3>Access the Swagger API Documentation</h3>

    <ol>
        <li>Open your web browser.</li>
        <li>Access the Swagger API documentation by navigating to:</li>
        <pre><code><a href="http://localhost:8000/docs">http://localhost:8000/docs</a></code></pre>
    </ol>

    <p>This will open Swagger UI, which provides interactive documentation for the API.</p>

    <h3>Use the API</h3>

    <ol>
        <li>In Swagger UI, you can explore the available endpoints, such as <code>/create_transition_video</code>.</li>
        <li>Click on the endpoint to expand it and see details about the request and response.</li>
        <li>To use the API, click the "Try it out" button, provide the required input (raw and edited photo URLs), and click "Execute." The API will respond with the result, including a URL link to the generated video.</li>
        <li>You can access the generated video by opening the provided URL in your browser or downloading it for your social media content.</li>
    </ol>

    <h2>Usefulness</h2>

    <p>This code can be incredibly useful for social media creators and marketers looking to create eye-catching and engaging content for short video platforms. Here are some ways it can benefit you:</p>

    <ul>
        <li><strong>Save Time</strong>: Instead of manually creating transition videos between photos, you can automate the process with this tool, saving you time and effort.</li>
        <li><strong>Engagement</strong>: Engaging transitions between photos can help capture the viewer's attention and make your content more shareable.</li>
        <li><strong>Customization</strong>: You can easily customize the transition effect to match your branding and style.</li>
        <li><strong>Variety</strong>: With the option to choose different transition effects, you can keep your content fresh and experiment with various styles.</li>
        <li><strong>Platform Compatibility</strong>: The generated videos are suitable for various short video platforms, making it versatile for your content strategy.</li>
        <li><strong>Content Creation</strong>: Whether you're a social media influencer, content creator, or marketer, this tool can enhance your content creation capabilities.</li>
    </ul>

    <p>Start creating captivating short videos for your social media channels today with the Photos to Video Transition Generator!</p>

    <h2>License</h2>

    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>

</html>
