import os
from utils.file_utils import normalize_input_file

# PDF imports
from parsers.pdf_parser import convert_pdf_to_clean_text_pdf
# from overlay.pdf_clean import write_clean_pdf_with_images
import fitz  # PyMuPDF

# DOCX imports
from docx import Document
from parsers.docx_parser import parse_docx
from ocr.ocr_docx import get_image_text
from overlay.docx_overlay import overlay_docx

def run_pdf_pipeline(pdf_path):
    print(f"📄 Processing PDF: {pdf_path}")

    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join("output", f"{base_name}_plaintext.pdf")

    convert_pdf_to_clean_text_pdf(pdf_path, output_path)

    print(f"✅ Done: {output_path}")


def run_docx_pipeline(docx_path):
    print(f"📄 Processing DOCX: {docx_path}")
    
    doc = Document(docx_path)
    text_map = []
    image_map = []

    text_map = parse_docx(doc, text_map)
    text_map, image_map = get_image_text(doc, text_map, image_map)

    texts_to_translate = [entry.get("text") or entry.get("ocr_text") for entry in text_map]

    # Placeholder translation (mock)
    translated_texts = [text.upper() for text in texts_to_translate]

    updated_doc = overlay_docx(doc, text_map, translated_texts, image_map)

    base_name = os.path.splitext(os.path.basename(docx_path))[0]
    output_path = os.path.join("output", f"{base_name}_translated.docx")
    updated_doc.save(output_path)
    print(f"✅ DOCX saved: {output_path}")


if __name__ == "__main__":
    input_file = "./parseTest.pdf"  # or "./parseTest.docx"
    os.makedirs("output", exist_ok=True)

    normalized_input, ext = normalize_input_file(input_file)

    if ext == ".pdf":
        run_pdf_pipeline(normalized_input)
    elif ext == ".docx":
        run_docx_pipeline(normalized_input)
