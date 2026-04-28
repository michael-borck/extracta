from pathlib import Path
from typing import Any

from markitdown import MarkItDown

from ..base_lens import BaseLens

class DocumentLens(BaseLens):
    """Extracts text content from document files via markitdown.

    Supports: PDF, DOCX, PPTX, XLSX, XLS, CSV, TSV, TXT, MD, RST,
              JSON, HTML, EPUB, IPYNB, XML and any format markitdown handles.

    Note on images: markitdown extracts text only. Embedded image extraction
    (for document viewers) is a planned future feature requiring PyMuPDF for
    PDFs and python-pptx blob access for PPTX. See design doc for hook points.
    """

    SUPPORTED_EXTENSIONS = {
        # Plain text
        ".txt", ".md", ".rst",
        # Data
        ".json", ".csv", ".tsv",
        # Office documents
        ".pdf", ".docx", ".pptx", ".xlsx", ".xls",
        # Web / notebook
        ".html", ".htm", ".epub", ".ipynb", ".xml",
    }

    def __init__(self) -> None:
        self._markitdown = MarkItDown()

    def extract(self, file_path: Path | str) -> dict[str, Any]:
        """Extract text content from a document file.

        Args:
            file_path: Path to the document file (str or Path).

        Returns:
            dict with keys:
              success (bool)
              data (dict): content_type, raw_content, file_path, file_size
              error (str): present only on failure
        """
        try:
            if isinstance(file_path, str):
                file_path = Path(file_path)

            if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                return {
                    "success": False,
                    "error": f"Unsupported file type: {file_path.suffix}",
                    "data": {},
                }

            file_size = file_path.stat().st_size
            result = self._markitdown.convert(file_path)
            content = result.text_content or ""

            return {
                "success": True,
                "data": {
                    "content_type": "text",
                    "raw_content": content,
                    "file_path": str(file_path),
                    "file_size": file_size,
                },
            }

        except Exception as e:
            return {"success": False, "error": repr(e), "data": {}}
