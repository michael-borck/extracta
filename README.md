# Extracta

> **Deprecated.** This package is no longer maintained.
> For document text extraction use [markitdown](https://github.com/microsoft/markitdown) directly.
> Existing installs continue to work but no further updates will be published.

<!-- BADGES:START -->
[![edtech](https://img.shields.io/badge/-edtech-4caf50?style=flat-square)](https://github.com/topics/edtech) [![academic-integrity](https://img.shields.io/badge/-academic--integrity-blue?style=flat-square)](https://github.com/topics/academic-integrity) [![ai-analysis](https://img.shields.io/badge/-ai--analysis-blue?style=flat-square)](https://github.com/topics/ai-analysis) [![api](https://img.shields.io/badge/-api-blue?style=flat-square)](https://github.com/topics/api) [![citation-analysis](https://img.shields.io/badge/-citation--analysis-blue?style=flat-square)](https://github.com/topics/citation-analysis) [![cli-tool](https://img.shields.io/badge/-cli--tool-blue?style=flat-square)](https://github.com/topics/cli-tool) [![content-analysis](https://img.shields.io/badge/-content--analysis-blue?style=flat-square)](https://github.com/topics/content-analysis) [![modular-architecture](https://img.shields.io/badge/-modular--architecture-blue?style=flat-square)](https://github.com/topics/modular-architecture) [![plagiarism-detection](https://img.shields.io/badge/-plagiarism--detection-blue?style=flat-square)](https://github.com/topics/plagiarism-detection) [![python](https://img.shields.io/badge/-python-3776ab?style=flat-square)](https://github.com/topics/python)
<!-- BADGES:END -->

**Modular Content Analysis Platform** for research, assessment, and academic integrity checking.

Extracta provides a unified interface for extracting and analyzing content from diverse media types including documents, images, repositories, and web content. It supports both research-focused deep analysis and assessment-oriented quality evaluation, with specialized tools for academic integrity validation.

## ✨ Key Features

- **🧩 Modular Architecture**: Pluggable lenses and analyzers for different content types
- **📚 Academic Integrity**: Citation-reference validation, bibliography checking, URL verification, AI conversation analysis
- **🤖 AI Conversation Analysis**: Cognitive intent classification for AI-assisted learning assessment
- **🔍 Multiple Analysis Modes**: Research and assessment workflows
- **📄 Rich Content Support**: Text, images, documents, repositories, presentations, spreadsheets, AI conversations
- **🎯 Rubric-Based Assessment**: Custom rubrics for structured evaluation
- **🛡️ Security First**: Input sanitization, URL validation, malicious content detection
- **🧠 Intelligent Analysis**: Pattern detection, quality scoring, integrity validation, learning pattern recognition
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
pip install extracta[conversation]  # AI conversation analysis (Gemini default)
pip install extracta[openai]    # OpenAI LLM provider
pip install extracta[claude]    # Anthropic Claude LLM provider
pip install extracta[openrouter] # OpenRouter unified API
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

# AI conversation cognitive intent analysis (with different LLM providers)
extracta citation conversation chatgpt_export.json --provider gemini --output analysis.json
extracta citation conversation chat.json --provider claude --model claude-3-sonnet-20240229
extracta citation conversation chat.json --provider openai --model gpt-4
extracta citation conversation chat.json --provider openrouter --model anthropic/claude-3-haiku

# Results include:
# - Citation-reference relationship validation
# - Bibliography padding detection
# - URL accessibility and domain reputation
# - AI conversation learning pattern analysis
# - Academic integrity scoring
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
from extracta.analyzers import CitationAnalyzer, ReferenceAnalyzer, URLAnalyzer, ConversationAnalyzer

# Citation-reference validation
citation_analyzer = CitationAnalyzer()
citation_result = citation_analyzer.analyze(document_text)

# Bibliography quality assessment
reference_analyzer = ReferenceAnalyzer()
reference_result = reference_analyzer.analyze(document_text)

# URL validation and reputation checking
url_analyzer = URLAnalyzer()
url_result = url_analyzer.analyze(document_text)

# AI conversation cognitive intent analysis (with different providers)
conversation_analyzer = ConversationAnalyzer(provider="claude", model="claude-3-sonnet-20240229")
conversation_result = conversation_analyzer.analyze(conversation_json_data)

# Or use OpenAI
conversation_analyzer = ConversationAnalyzer(provider="openai", model="gpt-4")
conversation_result = conversation_analyzer.analyze(conversation_json_data)

# Combined integrity score
integrity_score = citation_result['citation_analysis']['academic_integrity_score']
learning_quality = conversation_result['conversation_analysis']['learning_assessment']['learning_quality_score']
print(f"Academic Integrity Score: {integrity_score}/100")
print(f"AI Learning Quality Score: {learning_quality}/100")
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

### AI Conversation Analysis
- **Cognitive Intent Classification**: Uses configurable LLM to classify user prompts as Delegation vs. Scaffolding
- **Multi-Provider Support**: Gemini, OpenAI GPT, Anthropic Claude, OpenRouter unified API
- **Learning Pattern Recognition**: Analyzes conversation flow for active learning behaviors
- **Session Quality Scoring**: Provides learning quality assessment (0-100)
- **Platform Support**: ChatGPT, Claude, Bard, and generic conversation formats

### Security & Privacy
- **Input Sanitization**: Detects and prevents malicious content, hidden text, and LLM jailbreaks
- **URL Protection**: SSRF prevention with academic domain whitelisting
- **Content Validation**: Size limits, encoding validation, and integrity checking
- **Privacy First**: No data persistence, user-controlled processing, ephemeral analysis
- **Safe Processing**: Static analysis only, no code execution or external script running

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
- [x] **AI Conversation Analysis**: Cognitive intent classification, learning pattern recognition
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
- [ ] **URL Conversation Input**: Direct analysis of conversations from URLs (ChatGPT share links, etc.)
- [ ] **GUI Application**: Web-based interface
- [ ] **LMS Integration**: Canvas, Blackboard, Moodle
- [ ] **Advanced ML Models**: Fine-tuned for educational content
- [ ] **Collaborative Features**: Multi-user assessment workflows
- [ ] **Plugin Architecture**: Custom lenses and analyzers