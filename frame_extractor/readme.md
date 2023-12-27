# Video Frame Extractor

The Video Frame Extractor is a Python module that allows you to extract frames from a video and save them as images in a specified format.

## Installation

You can install the module using pip:

```bash
pip install video-frame-extractor
```

## Usage


```python
from video_frame_extractor import VideoFrameExtractor

# Create an instance of VideoFrameExtractor
extractor = VideoFrameExtractor()

# Specify the path to the video file, output folder, and optional output format
video_path = "path/to/video.mp4"
output_folder = "path/to/output_folder"
output_format = "png"

# Extract frames from the video and save them in the specified format
extractor.extract_frames_from_video(video_path, output_folder, output_format)
```


## Documentation
VideoFrameExtractor Class
extract_frames_from_video(video_path, output_folder, output_format="png")
Extract frames from a video and save them as images in the specified format.

### Parameters:

video_path (str): Path to the video to be processed.
output_folder (str): Destination directory to save the extracted frames.
output_format (str, optional): The image format for the extracted frames. Default is "png".
### Raises:

FileNotFoundError: If the video file is not found.
NotADirectoryError: If the output directory is not a valid directory.
Exception: If there is an error opening the video or saving the frames.
Examples
Check the provided example in the Usage section for a quick guide on how to use the module.

## Contributing
If you have suggestions, improvements, or issues, feel free to open an issue or submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
