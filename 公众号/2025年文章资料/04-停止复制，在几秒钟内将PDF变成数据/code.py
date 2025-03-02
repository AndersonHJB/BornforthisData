import os
import fitz  # PyMuPDF
import pdfplumber
import tabula
import camelot
import pytesseract
from pdf2image import convert_from_path
import pandas as pd
import cv2
import numpy as np

# Step 1: Detect if the PDF is text-based or scanned
def is_pdf_text_based(pdf_path):
    """Returns True if the PDF contains selectable text, False if scanned."""
    doc = fitz.open(pdf_path)
    return any(page.get_text("text").strip() for page in doc)

# Step 2: Extract text with PyMuPDF
def extract_text_pymupdf(pdf_path, output_dir):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    with open(os.path.join(output_dir, "extracted_text.txt"), "w") as f:
        f.write(text)
    print("[SUCCESS] Extracted text with PyMuPDF.")

# Step 3: Extract tables with Tabula
def extract_tables_tabula(pdf_path, output_dir):
    try:
        dfs = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)
        for i, df in enumerate(dfs):
            df.to_csv(os.path.join(output_dir, f"table_tabula_{i}.csv"), index=False)
        print("[SUCCESS] Extracted tables with Tabula.")
        return True
    except Exception:
        print("[WARNING] Tabula failed.")
        return False

# Step 4: Extract tables with pdfplumber if Tabula fails
def extract_tables_pdfplumber(pdf_path, output_dir):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            tables = []
            for page in pdf.pages:
                extracted_tables = page.extract_tables()
                for table in extracted_tables:
                    df = pd.DataFrame(table)
                    tables.append(df)
        for i, df in enumerate(tables):
            df.to_csv(os.path.join(output_dir, f"table_pdfplumber_{i}.csv"), index=False)
        print("[SUCCESS] Extracted tables with pdfplumber.")
        return True
    except Exception:
        print("[WARNING] pdfplumber failed.")
        return False

# Step 5: Extract tables with Camelot for complex layouts
def extract_tables_camelot(pdf_path, output_dir):
    try:
        tables = camelot.read_pdf(pdf_path, pages="1", flavor="lattice")
        for i, table in enumerate(tables):
            table.df.to_csv(os.path.join(output_dir, f"table_camelot_{i}.csv"), index=False)
        print("[SUCCESS] Extracted tables with Camelot.")
        return True
    except Exception:
        print("[WARNING] Camelot failed.")
        return False

# Step 6: Extract text from scanned PDFs using OCR
def extract_text_tesseract(pdf_path, output_dir):
    pages = convert_from_path(pdf_path, dpi=300)
    text = "\n".join([pytesseract.image_to_string(page, config="--psm 6") for page in pages])
    with open(os.path.join(output_dir, "ocr_extracted_text.txt"), "w") as f:
        f.write(text)
    print("[SUCCESS] Extracted text with OCR.")

# Step 7: Extract images using PyMuPDF
def extract_images_pymupdf(pdf_path, output_dir):
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc):
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_data = base_image["image"]
            with open(os.path.join(output_dir, f"image_{page_num}_{img_index}.png"), "wb") as f:
                f.write(image_data)
    print("[SUCCESS] Extracted images from PDF.")

# Main function to automate extraction
def auto_extract(pdf_path, output_dir="extracted_data"):
    os.makedirs(output_dir, exist_ok=True)

    if is_pdf_text_based(pdf_path):
        print("[INFO] PDF contains selectable text. Extracting with PyMuPDF...")
        extract_text_pymupdf(pdf_path, output_dir)
        if not extract_tables_tabula(pdf_path, output_dir):
            if not extract_tables_pdfplumber(pdf_path, output_dir):
                extract_tables_camelot(pdf_path, output_dir)
    else:
        print("[INFO] PDF appears to be scanned. Using OCR...")
        extract_text_tesseract(pdf_path, output_dir)
    
    # Extract images
    extract_images_pymupdf(pdf_path, output_dir)

# Run the script
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python auto_extract.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    auto_extract(pdf_path)