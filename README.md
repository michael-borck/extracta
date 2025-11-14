# Extracta

**Modular Content Analysis Platform** for research, assessment, and academic integrity checking.

Extracta provides a unified interface for extracting and analyzing content from diverse media types including documents, images, repositories, and web content. It supports both research-focused deep analysis and assessment-oriented quality evaluation, with specialized tools for academic integrity validation.

## ✨ Key Features

- **🧩 Modular Architecture**: Pluggable lenses and analyzers for different content types
- **📚 Academic Integrity**: Citation-reference validation, bibliography checking, URL verification
- **🔍 Multiple Analysis Modes**: Research and assessment workflows
- **📄 Rich Content Support**: Text, images, documents, repositories, presentations, spreadsheets
- **🎯 Rubric-Based Assessment**: Custom rubrics for structured evaluation
- **🤖 Intelligent Analysis**: Pattern detection, quality scoring, integrity validation
- **💻 Multiple Interfaces**: CLI, Python API, and Web API
- **🔧 Modern Python**: Built with uv, ruff, mypy, and pytest

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

Install with specific feature support:

```bash
pip install extracta[audio]     # Audio processing (faster-whisper for Apple Silicon)
pip install extracta[video]     # Video processing
pip install extracta[text]      # Enhanced text analysis (spaCy, NLTK)
pip install extracta[image]     # Image analysis with OCR
pip install extracta[code]      # Code analysis
pip install extracta[citation]  # Academic integrity (CrossRef, URL validation)
pip install extracta[api]       # Web API server (FastAPI, Uvicorn)
pip install extracta[all]       # All features
```

## Usage

### Command Line

#### Basic Content Analysis
```bash
# Analyze document for research insights
extracta analyze research_paper.pdf --mode research --output analysis.json

# Assess student submission quality
extracta analyze essay.docx --mode assessment --output feedback.json

# Analyze repository structure and content
extracta analyze https://github.com/user/repo --mode assessment
```

#### Academic Integrity Checking
```bash
# Comprehensive citation and reference validation
extracta citation analyze student_paper.pdf --output integrity_check.json

# Results include:
# - Citation-reference relationship validation
# - Bibliography padding detection
# - URL accessibility and domain reputation
# - Academic integrity scoring
# - Suspicious pattern detection
```

### Python API

#### Basic Content Analysis
```python
from extracta import TextAnalyzer

analyzer = TextAnalyzer()
result = analyzer.analyze(text_content, mode="research")
print(result)
```

#### Academic Integrity Analysis
```python
from extracta.analyzers import CitationAnalyzer, ReferenceAnalyzer, URLAnalyzer

# Citation-reference validation
citation_analyzer = CitationAnalyzer()
citation_result = citation_analyzer.analyze(document_text)

# Bibliography quality assessment
reference_analyzer = ReferenceAnalyzer()
reference_result = reference_analyzer.analyze(document_text)

# URL validation and reputation checking
url_analyzer = URLAnalyzer()
url_result = url_analyzer.analyze(document_text)

# Combined integrity score (0-100)
integrity_score = citation_result['citation_analysis']['academic_integrity_score']
print(f"Academic Integrity Score: {integrity_score}/100")
```

### Grading and Assessment

```python
from extracta.grading.rubric_manager import RubricRepository, get_default_rubric
from extracta.grading.feedback_generator import FeedbackGenerator

# Load or create a rubric
repo = RubricRepository("rubrics")
rubric = get_default_rubric("academic")  # or repo.load("my-rubric")

# Generate feedback based on analysis results
generator = FeedbackGenerator()
feedback = generator.generate_feedback(
    rubric=rubric,
    analysis_data=analysis_result,
    audience="student",
    detail="detailed"
)
```

## 🎓 Academic Integrity Features

Extracta provides comprehensive tools for detecting academic integrity issues and validating scholarly work:

### Citation Analysis
- **Citation-Reference Validation**: Ensures all references have corresponding in-text citations
- **Bibliography Padding Detection**: Identifies references without citations
- **Citation Stuffing Detection**: Flags excessive citations in single sentences
- **Style Recognition**: Supports APA, MLA, Chicago, Harvard, and Numeric styles

### Reference Validation
- **DOI Verification**: Validates Digital Object Identifiers with CrossRef API
- **URL Accessibility**: Checks if referenced URLs are accessible (404 detection)
- **Domain Reputation**: Analyzes source credibility (academic vs. commercial domains)
- **Format Validation**: Ensures proper reference formatting and completeness

### Repository Analysis
- **WordPress Detection**: Identifies WordPress projects and analyzes themes/plugins
- **Code Quality Assessment**: Evaluates repository structure and practices
- **File Type Analysis**: Comprehensive analysis of all repository contents

### Integrity Scoring
- **Academic Integrity Score**: 0-100 scale based on multiple validation criteria
- **Detailed Reporting**: Specific issues and recommendations
- **Pattern Detection**: Identifies suspicious citation and reference patterns

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
│   │   ├── audio_lens/      # Audio file processing
│   │   ├── video_lens/      # Video file processing
│   │   ├── image_lens/      # Image processing with OCR
│   │   ├── document_lens/   # Text & Office document processing
│   │   ├── presentation_lens/ # Presentation file analysis
│   │   ├── repo_lens/       # Repository-level analysis
│   │   └── base_lens.py     # Common lens interface
│   ├── analyzers/           # Content analysis modules
│   │   ├── text_analyzer/   # Text quality and readability
│   │   ├── image_analyzer/  # Image quality assessment
│   │   ├── citation_analyzer/ # Citation-reference validation
│   │   ├── reference_analyzer/ # Bibliography quality assessment
│   │   ├── url_analyzer/    # URL validation and reputation
│   │   └── base_analyzer.py # Common analyzer interface
│   ├── grading/             # Assessment and grading
│   │   ├── rubric_manager/  # Rubric creation and management
│   │   └── feedback_generator.py # AI-powered feedback
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

## 🚀 Current Status & Roadmap

### ✅ Implemented Features
- [x] **Text Analysis**: Readability, sentiment, vocabulary, quality metrics
- [x] **Image Analysis**: OCR, quality assessment, accessibility
- [x] **Document Processing**: PDF, DOCX, Office docs (PPTX, Excel, CSV)
- [x] **Citation Validation**: Citation-reference relationships, academic integrity
- [x] **Reference Analysis**: Bibliography quality, DOI validation, CrossRef integration
- [x] **URL Validation**: Accessibility checking, domain reputation, robots.txt
- [x] **Repository Analysis**: GitHub repo analysis, WordPress detection
- [x] **Rubric System**: Custom rubrics, structured assessment
- [x] **CLI Interface**: Multiple commands for different analysis types
- [x] **Web API**: REST API for integration
- [x] **Python API**: Programmatic access

### 🔄 In Development
- [ ] **Audio Lens**: Speech-to-text, audio quality analysis
- [ ] **Video Lens**: Frame analysis, transcript processing
- [ ] **Code Analyzer**: Code quality metrics, best practices
- [ ] **Screenshot Integration**: Visual URL validation
- [ ] **Wayback Machine**: Archive URL checking

### 📋 Future Enhancements
- [ ] **GUI Application**: Web-based interface
- [ ] **LMS Integration**: Canvas, Blackboard, Moodle
- [ ] **Advanced ML Models**: Fine-tuned for educational content
- [ ] **Collaborative Features**: Multi-user assessment workflows
- [ ] **Plugin Architecture**: Custom lenses and analyzers