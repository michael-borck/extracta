def get_analyzer_for_content(content_type: str):
    """Get appropriate analyzer for content type"""
    if content_type == "text":
        from .text_analyzer import TextAnalyzer

        return TextAnalyzer()

    # TODO: Add more analyzers (image, code, etc.)
    return None
