from pathlib import Path


def get_lens_for_file(file_path: Path):
    """Get appropriate lens for file type"""
    from .document_lens import DocumentLens

    if file_path.suffix.lower() in DocumentLens.SUPPORTED_EXTENSIONS:
        return DocumentLens()

    # TODO: Add more lens types (audio, video, image, code)
    return None
