import fitz  # PyMuPDF
import os
import json
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def extract_headings_mupdf(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    has_text = False

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if block['type'] != 0:
                continue

            for line in block["lines"]:
                text = " ".join([span["text"] for span in line["spans"]]).strip()
                if not text:
                    continue

                has_text = True  # Some text is found

                font_sizes = [span["size"] for span in line["spans"] if "size" in span]
                fonts = [span["font"] for span in line["spans"]]
                is_bold = any("Bold" in f or "bold" in f for f in fonts)
                bbox = line["bbox"]
                height = bbox[3] - bbox[1]
                x0, y0 = bbox[0], bbox[1]

                avg_size = sum(font_sizes) / len(font_sizes) if font_sizes else 0
                is_top = y0 < 150
                is_centered = abs((bbox[0] + bbox[2]) / 2 - page.rect.width / 2) < 50

                level = None
                if avg_size > 18 or height > 24:
                    level = "H1"
                elif avg_size > 14 or height > 18:
                    level = "H2"
                elif avg_size > 12 or height > 16 or is_bold:
                    level = "H3"

                if level:
                    headings.append({
                        "level": level,
                        "text": text,
                        "page": page_num
                    })

    return headings, has_text

def extract_text_ocr(pdf_path):
    images = convert_from_path(pdf_path)
    headings = []

    for idx, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang='eng+tel')  # include other langs as needed
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Naive heading detection for OCR text
            if len(line) < 100 and line.isupper():
                level = "H1"
            elif len(line) < 80:
                level = "H2"
            elif len(line) < 60:
                level = "H3"
            else:
                continue

            headings.append({
                "level": level,
                "text": line,
                "page": idx + 1
            })

    return headings

# === Main Execution ===
input_dir = "input"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

for file_name in os.listdir(input_dir):
    if file_name.endswith(".pdf"):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".json")

        print(f"📄 Processing: {file_name}")
        headings, has_text = extract_headings_mupdf(input_path)

        if not has_text:
            print("⚠️ No text found. Falling back to OCR...")
            headings = extract_text_ocr(input_path)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(headings, f, ensure_ascii=False, indent=4)

print("✅ Extraction complete.")
