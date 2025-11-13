from pathlib import Path


def get_lens_for_file(file_path: Path):
    """Get appropriate lens for file type"""
    from .document_lens import DocumentLens
    from .image_lens import ImageLens
    from .audio_lens import AudioLens
    from .video_lens import VideoLens

    if file_path.suffix.lower() in DocumentLens.SUPPORTED_EXTENSIONS:
        return DocumentLens()
    elif file_path.suffix.lower() in ImageLens.SUPPORTED_EXTENSIONS:
        return ImageLens()
    elif file_path.suffix.lower() in AudioLens.SUPPORTED_EXTENSIONS:
        return AudioLens()
    elif file_path.suffix.lower() in VideoLens.SUPPORTED_EXTENSIONS:
        return VideoLens()

    # TODO: Add code lens
    return None
