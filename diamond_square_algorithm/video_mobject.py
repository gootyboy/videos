import cv2
import numpy as np
from manim import *

class VideoMobject(ImageMobject):
    def __init__(self, video_path: str, scale_factor: float = 1.0, **kwargs):
        self.video_path = video_path
        self.cap = None  # Keeps object picklable for deepcopy
        
        # Open temporarily to extract metadata and the first frame
        temp_cap = cv2.VideoCapture(video_path)
        if not temp_cap.isOpened():
            raise FileNotFoundError(f"Could not open video file: {video_path}")
            
        self.fps = temp_cap.get(cv2.CAP_PROP_FPS) or 30.0
        success, first_frame = temp_cap.read()
        temp_cap.release()
        
        if not success:
            raise ValueError(f"Could not read frames from: {video_path}")
            
        # CRITICAL FIX: Convert to RGBA (4 channels) instead of RGB (3 channels)
        first_frame_rgba = cv2.cvtColor(first_frame, cv2.COLOR_BGR2RGBA)
        
        super().__init__(first_frame_rgba, **kwargs)
        self.scale(scale_factor)
        
        # Attach the frame updater loop
        self.add_updater(self.update_video_frame)

    def update_video_frame(self, mobject, dt):
        """Automatically updates the video texture safely during rendering."""
        if self.cap is None:
            self.cap = cv2.VideoCapture(self.video_path)
            
        if self.cap.isOpened():
            success, frame = self.cap.read()
            if success:
                # CRITICAL FIX: Every subsequent frame must also be RGBA
                frame_rgba = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                mobject.set_pixel_array(frame_rgba)
            else:
                # Video reached the end, shut down safely
                self.cap.release()
                self.cap = None
                self.remove_updater(self.update_video_frame)

    def __del__(self):
        """Clean up background system hooks."""
        if hasattr(self, 'cap') and self.cap is not None:
            self.cap.release()
