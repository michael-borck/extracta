from pathlib import Path
from typing import Dict, Any
from ..base_lens import BaseLens
from .video_processor import VideoProcessor, VideoInfo


class VideoLens(BaseLens):
    """Lens for extracting content from video files"""

    SUPPORTED_EXTENSIONS = {
        ".mp4",
        ".mov",
        ".avi",
        ".webm",
        ".mkv",
        ".flv",
        ".wmv",
        ".m4v",
    }

    def __init__(self):
        """Initialize video lens."""
        self.processor = VideoProcessor()

    def extract(self, file_path: Path) -> Dict[str, Any]:
        """Extract content from video file"""
        try:
            if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                return {
                    "success": False,
                    "error": f"Unsupported file type: {file_path.suffix}",
                    "data": {},
                }

            # Validate video file
            video_info = self.processor.validate_file(file_path)

            return {
                "success": True,
                "data": {
                    "content_type": "video",
                    "file_path": str(file_path),
                    "file_size": file_path.stat().st_size,
                    "video_info": {
                        "duration": video_info.duration,
                        "width": video_info.width,
                        "height": video_info.height,
                        "fps": video_info.fps,
                        "format": video_info.format,
                        "codec": video_info.codec,
                    },
                },
            }

        except Exception as e:
            return {"success": False, "error": str(e), "data": {}}
