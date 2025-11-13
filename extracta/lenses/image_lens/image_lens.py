from pathlib import Path
from typing import Dict, Any
from ..base_lens import BaseLens


class ImageLens(BaseLens):
    """Lens for extracting content from image files"""

    SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

    def extract(self, file_path: Path) -> Dict[str, Any]:
        """Extract content from image file"""
        try:
            if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                return {
                    "success": False,
                    "error": f"Unsupported file type: {file_path.suffix}",
                    "data": {},
                }

            return {
                "success": True,
                "data": {
                    "content_type": "image",
                    "file_path": str(file_path),
                    "file_size": file_path.stat().st_size,
                },
            }

        except Exception as e:
            return {"success": False, "error": str(e), "data": {}}
