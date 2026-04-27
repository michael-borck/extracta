"""Tests for DocumentLens — document text extraction via markitdown."""

import tempfile
from pathlib import Path

import pytest

from extracta.lenses.document_lens import DocumentLens


@pytest.fixture
def lens():
    return DocumentLens()


@pytest.fixture
def sample_txt(tmp_path: Path) -> Path:
    """A minimal plain-text file."""
    p = tmp_path / "sample.txt"
    p.write_text(
        "This is a sample document.\n"
        "It has multiple lines of text.\n"
        "Used to verify plain-text extraction works correctly.",
        encoding="utf-8",
    )
    return p


@pytest.fixture
def sample_pdf() -> Path | None:
    """Reuse the PDF from document-lens test-data if available."""
    candidate = Path(__file__).parents[2] / "document-lens" / "test-data"
    pdfs = list(candidate.glob("*.pdf")) if candidate.exists() else []
    return pdfs[0] if pdfs else None


class TestDocumentLensExtract:
    def test_extract_txt_returns_success(self, lens: DocumentLens, sample_txt: Path):
        result = lens.extract(sample_txt)
        assert result["success"] is True
        assert "raw_content" in result["data"]
        assert len(result["data"]["raw_content"]) > 0

    def test_extract_txt_contains_text(self, lens: DocumentLens, sample_txt: Path):
        result = lens.extract(sample_txt)
        assert "sample document" in result["data"]["raw_content"].lower()

    def test_extract_txt_has_metadata(self, lens: DocumentLens, sample_txt: Path):
        result = lens.extract(sample_txt)
        data = result["data"]
        assert "file_path" in data
        assert "file_size" in data
        assert data["file_size"] > 0

    def test_extract_unsupported_type_returns_failure(self, lens: DocumentLens, tmp_path: Path):
        p = tmp_path / "file.xyz"
        p.write_bytes(b"binary content")
        result = lens.extract(p)
        assert result["success"] is False
        assert "error" in result

    def test_extract_string_path_accepted(self, lens: DocumentLens, sample_txt: Path):
        result = lens.extract(str(sample_txt))
        assert result["success"] is True

    def test_extract_pdf(self, lens: DocumentLens, sample_pdf: Path | None):
        if sample_pdf is None:
            pytest.skip("No PDF available in document-lens test-data")
        result = lens.extract(sample_pdf)
        assert result["success"] is True
        assert len(result["data"]["raw_content"]) > 0
