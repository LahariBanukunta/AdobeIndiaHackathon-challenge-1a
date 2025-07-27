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




# 📄 Challenge 1B — Persona-Driven Document Intelligence

## ✨ Overview

This solution extracts and prioritizes the most relevant sections from a set of PDF documents based on a given **persona** and their **job-to-be-done**.

---

## 🧠 Approach

1. **PDF Structure Parsing**:  
   Each document is parsed using `PyMuPDF`, extracting headings (H1, H2, H3) and text along with page numbers.

2. **Persona Understanding**:  
   The `persona` and `job description` are processed using basic NLP — extracting important terms using keyword-based or TF-IDF-like techniques.

3. **Section Relevance Scoring**:  
   Each section in the documents is scored against persona/job keywords. Top-ranked sections are selected.

4. **Sub-section Refinement**:  
   Relevant paragraphs or sentences from the top sections are further refined and ranked for detailed analysis.

5. **Output**:  
   Results are returned in a JSON format with metadata, extracted sections, and refined sub-section analysis.

---

## 📦 Models / Libraries Used

| Library       | Purpose                          |
|---------------|----------------------------------|
| PyMuPDF       | PDF parsing (text, font, layout) |
| nltk          | Tokenization, stopword removal   |
| scikit-learn  | TF-IDF / cosine similarity       |
| Python stdlib | os, json, datetime, re           |

📝 No pretrained model is used. Entire solution works **offline** and **on CPU**.

---

## 🐳 How to Build and Run

### 1. Build Docker Image

```bash
docker build --platform=linux/amd64 -t personaextractor:xyz456 .
2. Run Docker Container
bash
Copy
Edit
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  personaextractor:xyz456
Input: Place PDF files and persona config inside /input

Output: The extracted result.json will be saved to /output
