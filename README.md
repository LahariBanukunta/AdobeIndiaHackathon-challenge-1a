# 🧠 Connecting the Dots Through Docs 

This repository contains solutions for:

- 📘 **Challenge 1A**: PDF Outline Extractor
- 📄 **Challenge 1B**: Persona-Driven Document Intelligence

---

## 📘 Challenge 1A — PDF Outline Extractor

### ✅ Your Approach

We extract a structured outline from each PDF by:
- Using `PyMuPDF` to parse each page's text blocks, font sizes, and positions.
- Classifying heading levels (H1, H2, H3) dynamically based on font size patterns (relative ranking).
- Detecting the title using the largest, topmost, centered text on the first page.
- Structuring the output in a clean JSON format with heading levels and page numbers.

### ✅ Models or Libraries Used
- **PyMuPDF** (for PDF parsing)
- **NumPy** (for heading sorting and logic)
- Python standard libraries: `os`, `re`, `json`, `collections`

### ✅ How to Build and Run

```bash
# Build Docker image
docker build --platform=linux/amd64 -t pdfoutliner:abc123 .

# Run container (assumes /input and /output mounted)
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdfoutliner:abc123


