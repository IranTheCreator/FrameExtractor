import cv2
import face_recognition
import os

class VideoFrameExtractor:
    def __init__(self):
        pass

    def extract_frames_from_video(self, video_path, output_folder, output_format="png"):
        """
        Extract frames from a video and save them as images in the specified format.

        Parameters:
            video_path (str): Path to the video to be processed.
            output_folder (str): Destination directory to save the extracted frames.
            output_format (str, optional): The image format for the extracted frames.
                                           Default is "png".

        Raises:
            FileNotFoundError: If the video file is not found.
            NotADirectoryError: If the output directory is not a valid directory.
            Exception: If there is an error opening the video or saving the frames.
        """
        # Check if the video path is valid
        if not os.path.isfile(video_path):
            raise FileNotFoundError(f"The video file '{video_path}' was not found.")

        # Check if the output folder is valid
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        elif not os.path.isdir(output_folder):
            raise NotADirectoryError(f"'{output_folder}' is not a valid directory.")

        # Open the video
        cap = cv2.VideoCapture(video_path)

        # Check if the video was opened correctly
        if not cap.isOpened():
            raise Exception("Error opening the video.")

        # Initialize variables to count the number of frames and set the image name format
        frame_count = 0
        image_name_format = os.path.join(output_folder, f"frame_{frame_count:04d}.{output_format}")

        while True:
            # Read a frame from the video
            ret, frame = cap.read()

            # Check if the frame was read correctly
            if not ret:
                break

            # Save the frame as an image
            image_name = image_name_format.format(frame_count)
            cv2.imwrite(image_name, frame)

            # Update the frame count
            frame_count += 1

        # Release the video and close the process
        cap.release()
        cv2.destroyAllWindows()