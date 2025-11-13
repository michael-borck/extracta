from pathlib import Path
from typing import Dict, Any
from ..base_lens import BaseLens


class DocumentLens(BaseLens):
    """Lens for extracting content from document files"""

    SUPPORTED_EXTENSIONS = {".txt", ".md", ".rst"}

    def extract(self, file_path: Path) -> Dict[str, Any]:
        """Extract content from document file"""
        try:
            if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                return {
                    "success": False,
                    "error": f"Unsupported file type: {file_path.suffix}",
                    "data": {},
                }

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            return {
                "success": True,
                "data": {
                    "content_type": "text",
                    "raw_content": content,
                    "file_path": str(file_path),
                    "file_size": file_path.stat().st_size,
                    "encoding": "utf-8",
                },
            }

        except Exception as e:
            return {"success": False, "error": str(e), "data": {}}
