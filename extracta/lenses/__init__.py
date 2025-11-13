from pathlib import Path


def get_lens_for_file(file_path: Path):
    """Get appropriate lens for file type"""
    from .document_lens import DocumentLens
    from .image_lens import ImageLens

    if file_path.suffix.lower() in DocumentLens.SUPPORTED_EXTENSIONS:
        return DocumentLens()
    elif file_path.suffix.lower() in ImageLens.SUPPORTED_EXTENSIONS:
        return ImageLens()

    # TODO: Add more lens types (audio, video, code)
    return None
