# main.py

from utils.file_utils import normalize_input_file
from parsers.pdf_parser import extract_text_blocks_combined
from overlay.pdf_overlay import overlay_translated_text
import os

def run_overlay_test(input_path):
    # Normalize input (.docx → .pdf if needed)
    normalized_pdf = normalize_input_file(input_path)

    print(f"📄 Processing: {normalized_pdf}")

    # Extract blocks (embedded text + OCR)
    all_blocks = extract_text_blocks_combined(normalized_pdf)

    print("🔍 Block extraction complete. Pages:", len(all_blocks))

    # Instead of translating, just re-overlay the same text
    # (Use this to test alignment, visibility, bbox fit, etc.)
    translated_blocks = []
    for page in all_blocks:
        new_page = []
        for block in page:
            new_page.append({
                "text": block["text"],  # No translation — just reuse
                "bbox": block["bbox"]
            })
        translated_blocks.append(new_page)

    # Save final overlay test output
    base_name = os.path.splitext(os.path.basename(normalized_pdf))[0]
    output_path = os.path.join("output", f"{base_name}_overlay_test.pdf")
    overlay_translated_text(normalized_pdf, translated_blocks, output_path)

    print("✅ Overlay test complete.")

if __name__ == "__main__":
    # Replace this with your actual input file path
    input_file = "examples/sample.pdf"  # or .docx
    run_overlay_test(input_file)
