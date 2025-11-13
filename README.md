# Extracta

Modular content analysis and insight generation toolkit for research and assessment.

Extracta provides a unified interface for extracting and analyzing content from various media types including audio, video, text, images, and code. It supports both research-focused deep analysis and assessment-oriented quality evaluation.

## Features

- **Modular Architecture**: Pluggable lenses for different content types
- **Multiple Analysis Modes**: Research and assessment workflows
- **Extensible**: Easy to add new analyzers and lenses
- **CLI Interface**: Command-line tool for quick analysis
- **Python API**: Programmatic access for integration
- **Modern Python**: Built with uv, ruff, mypy, and pytest

## Installation

### From PyPI

```bash
pip install extracta
```

### From Source

```bash
git clone https://github.com/michaelborck-education/extracta.git
cd extracta
pip install -e .
```

### Optional Dependencies

Install with specific media support:

```bash
pip install extracta[audio]     # Audio processing
pip install extracta[video]     # Video processing
pip install extracta[text]      # Text analysis
pip install extracta[image]     # Image analysis
pip install extracta[code]      # Code analysis
pip install extracta[all]       # All features
```

## Usage

### Command Line

```bash
# Analyze audio file for research
extracta analyze interview.mp3 --mode research

# Assess text quality
extracta analyze essay.pdf --mode assessment --output results.json
```

### Python API

```python
from extracta import TextAnalyzer

analyzer = TextAnalyzer()
result = analyzer.analyze(text, mode="research")
print(result)
```

### Web API

Start the server:

```bash
extracta serve
# Or with custom host/port
extracta serve --host 0.0.0.0 --port 8000
```

API endpoints:

- `POST /extract` - Extract content from uploaded file
- `POST /analyze` - Extract and analyze content from uploaded file
- `GET /health` - Health check

Example with curl:

```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@sample.txt" \
  -F "mode=assessment"
```

## Development

### Setup

```bash
# Clone repository
git clone https://github.com/michaelborck-education/extracta.git
cd extracta

# Create virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -e ".[dev]"
```

### Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=extracta
```

### Linting and Type Checking

```bash
# Lint with ruff
ruff check .

# Type check with mypy
mypy extracta

# Format code
ruff format .
```

### Building and Publishing

```bash
# Build package
uv build

# Publish to PyPI
uv venv  # if not already
source .venv/bin/activate
uv pip install twine
twine upload dist/* --repository pypi
```

## Project Structure

```
extracta/
├── extracta/
│   ├── lenses/              # Content extraction modules
│   ├── analyzers/           # Content analysis modules
│   ├── grading/             # Assessment and grading
│   ├── orchestration/       # Workflow management
│   ├── shared/              # Common utilities
│   └── cli/                 # Command-line interface
├── tests/                   # Test suite
├── docs/                    # Documentation
├── examples/                # Usage examples
├── pyproject.toml           # Package configuration
└── README.md               # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run the test suite
6. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Roadmap

- [ ] Audio lens implementation
- [ ] Video lens implementation
- [ ] Image analyzer implementation
- [ ] Code analyzer implementation
- [ ] Web API interface
- [ ] GUI application