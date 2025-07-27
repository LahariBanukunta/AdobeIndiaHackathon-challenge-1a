# AdobeIndiaHackathon

# Hackathon Challenge Submission - Lahari Banukunta

## 📁 Challenge - 1(a): PDF Outline Extractor
Location: `Challenge - 1(a)/`

### Run Instructions
```bash
docker build --platform linux/amd64 -t outlineextractor:abc123 ./Challenge - 1(a)
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none outlineextractor:abc123


Description
Extracts title, headings (H1, H2, H3) with page numbers from any PDF in the /input directory and outputs a structured JSON in /output.

📁 Challenge_1b: Persona-Driven Section Extractor
Location: Challenge_1b/

Run Instructions
bash
Copy
Edit
docker build --platform=linux/amd64 -t personaselector:xyz123 ./Challenge_1b
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none personaselector:xyz123
Description
Given multiple documents and a persona’s objective, this extracts and ranks the most relevant sections and sub-sections. Full details in approach_explanation.md.

