def get_analyzer_for_content(content_type: str):
    """Get appropriate analyzer for content type"""
    if content_type == "text":
        from .text_analyzer import TextAnalyzer

        return TextAnalyzer()
    elif content_type == "image":
        from .image_analyzer import ImageAnalyzer

        return ImageAnalyzer()

    # TODO: Add more analyzers (code, etc.)
    return None
