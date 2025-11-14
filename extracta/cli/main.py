import json
import click
from pathlib import Path
from extracta.lenses import get_lens_for_file
from extracta.analyzers import get_analyzer_for_content


@click.group()
@click.version_option()
def main():
    """Extracta - Modular content analysis and insight generation"""
    pass


# Content-type specific subcommands
@main.group()
def video():
    """Video content analysis commands"""
    pass


@main.group()
def image():
    """Image content analysis commands"""
    pass


@main.group()
def text():
    """Text content analysis commands"""
    pass


@main.group()
def rubric():
    """Rubric management commands"""
    pass


@main.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "--mode", type=click.Choice(["research", "assessment"]), default="assessment"
)
@click.option("--output", "-o", type=click.Path())
def analyze(file_path, mode, output):
    """Analyze content from file"""
    file_path = Path(file_path)

    # Get appropriate lens
    lens = get_lens_for_file(file_path)
    if not lens:
        click.echo(f"No lens available for {file_path.suffix}", err=True)
        return

    click.echo(f"Analyzing {file_path.name}...")

    # Extract content
    result = lens.extract(file_path)
    if not result["success"]:
        click.echo(f"Error: {result['error']}", err=True)
        return

    # Analyze content
    if result["data"]["content_type"] == "video":
        # Video lens outputs textual descriptions - analyze them with text_analyzer
        from extracta.analyzers.text_analyzer import TextAnalyzer

        text_analyzer = TextAnalyzer()

        # Analyze transcript
        transcript_analysis = text_analyzer.analyze(result["data"]["transcript"], mode)

        # Analyze frame descriptions as combined text
        frame_text = " ".join(result["data"]["frame_descriptions"])
        frame_analysis = text_analyzer.analyze(frame_text, mode)

        # Analyze visual summary
        summary_analysis = text_analyzer.analyze(result["data"]["visual_summary"], mode)

        # Simple combined score (average of readability grades)
        combined_score = (
            transcript_analysis.get("readability", {}).get("grade_level", 8)
            + frame_analysis.get("readability", {}).get("grade_level", 8)
            + summary_analysis.get("readability", {}).get("grade_level", 8)
        ) / 3

        result["data"]["analysis"] = {
            "transcript_analysis": transcript_analysis,
            "frame_analysis": frame_analysis,
            "summary_analysis": summary_analysis,
            "combined_readability_grade": round(combined_score, 1),
        }
    else:
        analyzer = get_analyzer_for_content(result["data"]["content_type"])
        if analyzer:
            if result["data"]["content_type"] == "image":
                analysis = analyzer.analyze(result["data"]["file_path"], mode)
            else:
                analysis = analyzer.analyze(result["data"]["raw_content"], mode)
            result["data"]["analysis"] = analysis

    # Output results
    if output:
        with open(output, "w") as f:
            json.dump(result["data"], f, indent=2)
    else:
        click.echo(json.dumps(result["data"], indent=2))


@video.command("analyze")
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "--mode", type=click.Choice(["research", "assessment"]), default="assessment"
)
@click.option("--output", "-o", type=click.Path())
def video_analyze(file_path, mode, output):
    """Analyze video content"""
    file_path = Path(file_path)

    # Force video lens
    from extracta.lenses.video_lens import VideoLens

    lens = VideoLens()

    click.echo(f"Analyzing video {file_path.name}...")

    # Extract content
    result = lens.extract(file_path)
    if not result["success"]:
        click.echo(f"Error: {result['error']}", err=True)
        return

    # Analyze content
    from extracta.analyzers.text_analyzer import TextAnalyzer

    text_analyzer = TextAnalyzer()

    # Analyze transcript
    transcript_analysis = text_analyzer.analyze(result["data"]["transcript"], mode)

    # Analyze frame descriptions
    frame_text = " ".join(result["data"]["frame_descriptions"])
    frame_analysis = text_analyzer.analyze(frame_text, mode)

    # Analyze visual summary
    summary_analysis = text_analyzer.analyze(result["data"]["visual_summary"], mode)

    # Simple combined score
    combined_score = (
        transcript_analysis.get("readability", {}).get("grade_level", 8)
        + frame_analysis.get("readability", {}).get("grade_level", 8)
        + summary_analysis.get("readability", {}).get("grade_level", 8)
    ) / 3

    result["data"]["analysis"] = {
        "transcript_analysis": transcript_analysis,
        "frame_analysis": frame_analysis,
        "summary_analysis": summary_analysis,
        "combined_readability_grade": round(combined_score, 1),
    }

    # Output results
    if output:
        with open(output, "w") as f:
            json.dump(result["data"], f, indent=2)
        click.echo(f"Results saved to {output}")
    else:
        click.echo(json.dumps(result["data"], indent=2))


@image.command("analyze")
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "--mode", type=click.Choice(["research", "assessment"]), default="assessment"
)
@click.option("--output", "-o", type=click.Path())
def image_analyze(file_path, mode, output):
    """Analyze image content"""
    file_path = Path(file_path)

    # Force image lens
    from extracta.lenses.image_lens import ImageLens

    lens = ImageLens()

    click.echo(f"Analyzing image {file_path.name}...")

    # Extract content
    result = lens.extract(file_path)
    if not result["success"]:
        click.echo(f"Error: {result['error']}", err=True)
        return

    # Analyze content
    analyzer = get_analyzer_for_content(result["data"]["content_type"])
    if analyzer:
        analysis = analyzer.analyze(result["data"]["file_path"], mode)
        result["data"]["analysis"] = analysis

    # Output results
    if output:
        with open(output, "w") as f:
            json.dump(result["data"], f, indent=2)
        click.echo(f"Results saved to {output}")
    else:
        click.echo(json.dumps(result["data"], indent=2))


@text.command("analyze")
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "--mode", type=click.Choice(["research", "assessment"]), default="assessment"
)
@click.option("--output", "-o", type=click.Path())
def text_analyze(file_path, mode, output):
    """Analyze text content"""
    file_path = Path(file_path)

    # Force document lens
    from extracta.lenses.document_lens import DocumentLens

    lens = DocumentLens()

    click.echo(f"Analyzing text {file_path.name}...")

    # Extract content
    result = lens.extract(file_path)
    if not result["success"]:
        click.echo(f"Error: {result['error']}", err=True)
        return

    # Analyze content
    analyzer = get_analyzer_for_content(result["data"]["content_type"])
    if analyzer:
        analysis = analyzer.analyze(result["data"]["raw_content"], mode)
        result["data"]["analysis"] = analysis

    # Output results
    if output:
        with open(output, "w") as f:
            json.dump(result["data"], f, indent=2)
        click.echo(f"Results saved to {output}")
    else:
        click.echo(json.dumps(result["data"], indent=2))


@rubric.command("list")
def rubric_list():
    """List available rubrics"""
    from extracta.grading import default_rubrics

    rubrics = []
    rubrics.extend(default_rubrics.list_default_rubrics())

    click.echo("Available rubrics:")
    for rubric_type in rubrics:
        click.echo(f"  - {rubric_type}")


@rubric.command("create")
@click.argument("name")
@click.option(
    "--type",
    "rubric_type",
    type=click.Choice(["academic", "business", "creative", "general"]),
    default="general",
)
@click.option("--output", "-o", type=click.Path())
def rubric_create(name, rubric_type, output):
    """Create a new rubric based on a template"""
    from extracta.grading import default_rubrics

    # Get template
    template = default_rubrics.get_default_rubric(rubric_type)
    if not template:
        click.echo(f"Unknown rubric type: {rubric_type}", err=True)
        return

    # Customize the template
    template.name = name

    if output:
        # Export to file
        import json

        with open(output, "w") as f:
            json.dump(template.to_dict(), f, indent=2)
        click.echo(f"Rubric saved to {output}")
    else:
        click.echo(f"Created rubric: {name} (based on {rubric_type} template)")
        click.echo("Use --output to save to file")


@main.command()
@click.option("--host", default="127.0.0.1", help="Host to bind to")
@click.option("--port", default=8000, type=int, help="Port to bind to")
def serve(host, port):
    """Start the FastAPI server"""
    try:
        from extracta.api import create_app
        import uvicorn

        app = create_app()
        click.echo(f"Starting server on http://{host}:{port}")
        click.echo("Press Ctrl+C to stop")
        uvicorn.run(app, host=host, port=port)

    except ImportError:
        click.echo(
            "API dependencies not installed. Install with: pip install extracta[api]",
            err=True,
        )
