# Extracta: Modular Content Analysis Platform

## Vision

Build a **modular content analysis platform** where diverse content formats (videos, documents, images, audio, code, websites) are intelligently ingested, standardized textual representations are extracted, and consistent analysis workflows are applied.

Core principle: **Extract once, analyze many ways**
- Each content format has a dedicated **ingestion lens** that extracts standardized textual descriptions
- Extracted descriptions flow to appropriate **content analyzers** for insights and metrics
- All analyses feed into **grading and assessment** workflows

## Architecture Layers

```
┌─────────────────────────────────────────────────────────────┐
│  Orchestration Layer (CLI, API, future assessment-bench)
│  - Route content by file type
│  - Aggregate analysis results
│  - Manage workflows
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  Content Ingestion Layer (LENSES)
│  - Extract standardized textual descriptions from files
│  - Convert raw content to analyzable text representations
│  - May compose/delegate to other lenses for complex formats
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  Content Analysis Layer (ANALYZERS)
│  - Analyze textual descriptions and metadata
│  - Generate metrics, insights, quality scores
│  - Reusable across multiple content types
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  Assessment & Feedback Layer
│  - rubric_manager: Apply custom rubrics to analysis results
│  - feedback_generator: Generate detailed feedback
│  - accessibility considerations
└─────────────────────────────────────────────────────────────┘
```

---

## Layer 1: Content Ingestion Lenses

### Currently Implemented Lenses

#### video-lens
**Status:** ✅ Implemented (basic)

- **Input:** Video files (mp4, mov, avi, webm, mkv, flv, wmv, m4v)
- **Extraction:**
  - Video validation and metadata
  - Key frame extraction
  - Audio extraction from video
  - Placeholder for speech-to-text transcription
  - Placeholder for visual scene descriptions
- **Output:**
  ```json
  {
    "content_type": "video",
    "duration": 120.5,
    "resolution": "1920x1080",
    "fps": 30,
    "frames_extracted": 10,
    "transcript": "Textual transcription placeholder...",
    "frame_descriptions": [
      "Presentation slide with title and bullet points",
      "Speaker presenting to camera with good eye contact"
    ],
    "visual_summary": "Video content showing presentation slides and speaker delivery",
    "audio_quality": "Clear audio with good volume levels",
    "scene_changes": 8
  }
  ```
- **Delegate to:**
  - `text_analyzer` on transcript and descriptions

---

#### audio-lens
**Status:** ✅ Implemented (basic)

- **Input:** Audio files (mp3, wav, flac, aac, ogg, m4a, wma)
- **Extraction:**
  - Audio validation and metadata
  - Placeholder for speech-to-text transcription
  - Audio format conversion preparation
- **Output:**
  ```json
  {
    "content_type": "audio",
    "duration": 180.5,
    "sample_rate": 44100,
    "channels": 2,
    "format": "mp3",
    "transcript": "Textual transcription placeholder...",
    "audio_quality": "Good quality stereo audio"
  }
  ```
- **Delegate to:**
  - `text_analyzer` on transcript

---

#### image-lens
**Status:** ✅ Implemented (basic)

- **Input:** Image files (jpg, jpeg, png, gif, bmp, tiff, webp)
- **Extraction:**
  - Image validation and metadata
  - OCR text extraction
  - Basic visual quality assessment
- **Output:**
  ```json
  {
    "content_type": "image",
    "width": 1920,
    "height": 1080,
    "format": "JPEG",
    "extracted_text": "OCR text content from image...",
    "visual_quality": "High quality image",
    "accessibility": {
      "has_alt_text": false,
      "suggested_alt": "Image description placeholder"
    }
  }
  ```
- **Delegate to:**
  - `text_analyzer` on extracted_text
  - `image_analyzer` on visual metrics

---

#### document-lens
**Status:** ✅ Implemented (basic)

- **Input:** Document files (txt, md, rst)
- **Extraction:**
  - Text extraction
  - Basic structure analysis
- **Output:**
  ```json
  {
    "content_type": "document",
    "text": "Full extracted text content...",
    "word_count": 1250,
    "structure": {
      "headings": ["Introduction", "Methods", "Results"],
      "paragraphs": 15
    },
    "metadata": {
      "encoding": "utf-8",
      "format": "markdown"
    }
  }
  ```
- **Delegate to:**
  - `text_analyzer` on extracted text

---

### Future Lens Implementations

#### code-lens
**Status:** ❌ Planned

- **Input:** Code files (.py, .js, .java, .rb, etc.) or Jupyter notebooks (.ipynb)
- **Extraction:**
  - Source code as structured AST
  - Comments and docstrings
  - Function/class definitions
  - Code metrics (complexity, lines of code)
  - For notebooks: cells, outputs, visualizations
- **Output:**
  ```json
  {
    "code": "Full source code",
    "language": "python",
    "structure": {
      "functions": [{"name": "analyze_data", "complexity": 5}],
      "classes": [{"name": "Analyzer", "methods": 8}],
      "imports": ["numpy", "pandas"]
    },
    "metrics": {
      "lines_of_code": 245,
      "cyclomatic_complexity": 8,
      "maintainability_index": 75
    },
    "documentation": {
      "docstrings": 85,
      "comments": 120
    }
  }
  ```
- **Delegate to:**
  - `code_analyzer` on structure and metrics
  - `text_analyzer` on docstrings and comments

---

#### slide-lens
**Status:** ❌ Planned

- **Input:** Slide presentation files (pptx, odp, pdf with slides)
- **Extraction:**
  - Per-slide text extraction
  - Slide layout analysis
  - Embedded images and media
- **Output:**
  ```json
  {
    "slides": [
      {
        "number": 1,
        "title": "Introduction",
        "text": "Full text content on slide",
        "layout": "title_and_content",
        "images": [{"description": "Chart showing data"}]
      }
    ],
    "metadata": {
      "title": "Presentation Title",
      "slide_count": 20
    }
  }
  ```
- **Delegate to:**
  - `text_analyzer` on all extracted text
  - `image_analyzer` on slide images

---

#### web-lens
**Status:** ❌ Planned

- **Input:** Web projects (HTML/CSS/JS, React, WordPress, etc.)
- **Extraction:**
  - Source code analysis
  - Rendered content screenshots
  - Accessibility analysis
  - Performance metrics
- **Output:**
  ```json
  {
    "source_analysis": {
      "languages": ["javascript", "html", "css"],
      "framework": "react",
      "components": 15
    },
    "rendered_content": {
      "screenshots": ["homepage.png", "contact.png"],
      "pages": 5
    },
    "accessibility": {
      "wcag_score": 0.85,
      "issues": ["Missing alt text on 2 images"]
    },
    "performance": {
      "load_time": 1.2,
      "bundle_size": 245000
    }
  }
  ```
- **Delegate to:**
  - `code_lens` on source files
  - `image_analyzer` on screenshots
  - `text_analyzer` on extracted content

---

#### repo-lens
**Status:** ❌ Planned

- **Input:** GitHub repository URLs or local repo directories
- **Process:**
  1. Clone/download repository
  2. Scan file types
  3. Route files to appropriate lenses
- **Output:**
  ```json
  {
    "repository_metadata": {
      "language": "python",
      "languages": ["python", "javascript"],
      "files": 45
    },
    "analysis_by_type": {
      "code_files": {...},
      "documentation": {...},
      "images": {...}
    },
    "aggregated_metrics": {
      "total_lines_of_code": 5000,
      "test_coverage": 0.75
    }
  }
  ```
- **Delegate to:** Multiple lenses in sequence

---

## Layer 2: Content Analyzers

### Currently Implemented Analyzers

#### text-analyzer
**Status:** ✅ Implemented

**Input:** Any textual content (transcripts, extracted text, descriptions)

**Analysis:**
- Readability metrics (Flesch-Kincaid, SMOG)
- Vocabulary richness and diversity
- Sentiment analysis
- Grammar and style checking
- Content structure analysis

**Output:**
```json
{
  "readability": {
    "flesch_reading_ease": 65.5,
    "grade_level": 8.5,
    "reading_time_minutes": 3
  },
  "vocabulary": {
    "unique_words": 450,
    "vocabulary_richness": 0.78,
    "hapax_legomena": 120
  },
  "sentiment": {
    "positive_words": 45,
    "negative_words": 12,
    "sentiment_score": 0.25
  },
  "quality": {
    "grammar_issues": ["Double space found"],
    "clarity_score": 0.85
  }
}
```

---

#### image-analyzer
**Status:** ✅ Implemented (basic)

**Input:** Image data and metadata

**Analysis:**
- Basic quality metrics
- Format validation
- Accessibility considerations

**Output:**
```json
{
  "dimensions": {"width": 1920, "height": 1080},
  "quality": {"format": "JPEG", "size_mb": 2.1},
  "accessibility": {"has_alt_text": false}
}
```

---

### Future Analyzer Implementations

#### code-analyzer
**Status:** ❌ Planned

**Input:** Code structure and metrics from code-lens

**Analysis:**
- Code quality metrics (complexity, maintainability)
- Best practices adherence
- Documentation quality
- Security issues

**Output:**
```json
{
  "quality_metrics": {
    "maintainability_index": 75,
    "cyclomatic_complexity": 8,
    "code_duplication_ratio": 0.08
  },
  "best_practices": {
    "naming_conventions": 0.90,
    "documentation_completeness": 0.75
  },
  "issues": {
    "potential_bugs": [],
    "security_concerns": []
  }
}
```

---

#### accessibility-analyzer
**Status:** ❌ Planned

**Input:** Content from any lens (text, images, structure)

**Analysis:** WCAG 2.1 compliance
- Color contrast ratios
- Alt text quality
- Heading hierarchy
- Keyboard navigation

**Output:**
```json
{
  "wcag_level": "AA",
  "score": 0.85,
  "issues": [
    {
      "level": "error",
      "criterion": "1.4.3 Contrast (Minimum)",
      "suggestion": "Increase contrast ratio"
    }
  ]
}
```

---

## Layer 3: Assessment & Feedback

### Currently Implemented

#### rubric_manager
**Status:** ✅ Implemented

- Custom rubric creation and management
- Scoring scale configuration
- Assessment result calculation
- Repository for storing rubrics

#### feedback_generator
**Status:** ✅ Implemented (basic)

- Template-based feedback generation
- Audience-specific messaging
- Integration with analysis results

#### default_rubrics
**Status:** ✅ Implemented

- Academic content rubric
- Business content rubric
- Creative content rubric
- General content rubric

---

## Current Implementation Status

| Component | Status | Implementation Level |
|-----------|--------|---------------------|
| `video_lens` | ✅ | Basic extraction + textual descriptions |
| `audio_lens` | ✅ | Basic extraction + transcription prep |
| `image_lens` | ✅ | Basic extraction + OCR |
| `document_lens` | ✅ | Basic text extraction |
| `text_analyzer` | ✅ | Full readability, sentiment, vocabulary analysis |
| `image_analyzer` | ✅ | Basic quality metrics |
| `rubric_manager` | ✅ | Complete rubric system |
| `feedback_generator` | ✅ | Template-based feedback |
| `code_lens` | ❌ | Not implemented |
| `slide_lens` | ❌ | Not implemented |
| `web_lens` | ❌ | Not implemented |
| `repo_lens` | ❌ | Not implemented |
| `code_analyzer` | ❌ | Not implemented |
| `accessibility_analyzer` | ❌ | Not implemented |

## Technology Stack (Current)

### Core Dependencies
- **Python:** 3.10+
- **Build:** uv, hatchling
- **Linting:** ruff
- **Testing:** pytest
- **Types:** mypy

### Lens Implementations
- **video_lens:** ffmpeg-python, pydantic
- **audio_lens:** ffmpeg-python
- **image_lens:** Pillow, pytesseract
- **document_lens:** Built-in text processing
- **CLI:** Click
- **API:** FastAPI, Uvicorn

### Future Additions
- **code_lens:** AST parsing, tree-sitter, radon
- **web_lens:** Selenium/Playwright, BeautifulSoup
- **repo_lens:** GitPython, GitHub API
- **ML/AI:** faster-whisper (audio), vision models (images)

### Analyzers
- **text_analyzer:** Built-in algorithms (expand to spaCy, NLTK)
- **image_analyzer:** Pillow (expand to OpenCV, scikit-image)
- **code_analyzer:** radon, pylint, flake8 (planned)
- **accessibility_analyzer:** axe-core, webaim (planned)

---

## Development Roadmap

### Phase 1: Core Content Types ✅ (Current)
**Completed:**
- Video, audio, image, document ingestion
- Text analysis with comprehensive metrics
- Basic rubric-based assessment
- CLI and API interfaces
- Published to PyPI

**Deliverable:** Functional content analysis for basic use cases

### Phase 2: Enhanced Analysis (Next)
**Goals:**
- Improve existing analyzers with ML models
- Add code analysis capabilities
- Enhanced feedback generation
- Better OCR and transcription

**Timeline:** 1-2 months

### Phase 3: Extended Content Types
**Add:**
- `code_lens` and `code_analyzer`
- `slide_lens` for presentations
- `web_lens` for web projects
- `repo_lens` for repositories

**Timeline:** 2-3 months

### Phase 4: Advanced Features
**Add:**
- `accessibility_analyzer`
- Multi-artifact portfolio assessment
- Parallel processing optimization
- Plugin architecture

**Timeline:** 3-4 months

### Phase 5: Integration & Scale
**Add:**
- LMS integrations (Canvas, Blackboard)
- GitHub Classroom integration
- Distributed processing
- Advanced ML models

**Timeline:** 4-6 months

---

## Key Design Principles

### 1. Lens Granularity
- **One lens per content type** (video_lens, audio_lens, etc.)
- **Textual output standardization** - all lenses produce analyzable text
- **Separation of concerns** - ingestion vs analysis

### 2. Analyzer Reusability
- **Format-agnostic analyzers** - text_analyzer works on any text source
- **Composable analysis** - combine multiple analyzers per content type
- **Extensible metrics** - easy to add new analysis dimensions

### 3. Configuration Management
- **Shared config system** - extracta/shared/config.py
- **Environment overrides** - customizable via env vars
- **Sensible defaults** - works out-of-the-box

### 4. Clean Architecture
- **Lens → Textual Description → Analyzer → Assessment**
- **No circular dependencies** - strict layer separation
- **Testable components** - each layer independently testable

### 5. Pragmatic Scope
- **In scope:** Content extraction, analysis, assessment
- **Out of scope:** UI, course management, advanced integrations
- **Future:** Integration with broader assessment platforms

---

## Future Considerations

### Scalability
- Parallel lens processing for batch analysis
- Caching of extracted content
- Cloud deployment options
- Distributed processing for heavy ML models

### Extensibility
- Plugin system for custom lenses/analyzers
- Domain-specific rubric templates
- Custom analysis metrics
- Third-party integrations

### ML Enhancements
- Fine-tuned models for educational content
- Multi-modal analysis (text + images + audio)
- Predictive feedback and suggestions
- Automated rubric generation

---

## Glossary

- **Lens:** Content ingestion component that extracts standardized textual descriptions
- **Analyzer:** Reusable analysis tool that processes textual descriptions into metrics
- **Rubric:** Structured scoring criteria with weights and scales
- **Assessment:** Application of rubrics to analysis results
- **Feedback:** Generated guidance based on assessment results
- **Extracta:** Modular content analysis platform for diverse formats