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
