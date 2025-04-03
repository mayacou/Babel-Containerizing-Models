from docx import Document
from parsers.docx_parser import parse_docx
from ocr.ocr_docx import get_image_text
from overlay.docx_overlay import overlay_docx

# === Load document ===
doc = Document("parseTest.docx")
text_map = []  # For batching all text
image_map = []  # To track OCR for each image

# call docx_parser
text_map = parse_docx(doc, text_map)

# call ocr_docx
text_map, image_map = get_image_text(doc, text_map, image_map)

# batch text for translation **** may change later
texts_to_translate = [entry.get("text") or entry.get("ocr_text") for entry in text_map]

# Replace with actual LLM translation later
translated_texts = [text.upper() for text in texts_to_translate]

# call docx_overlay
doc = overlay_docx(doc, text_map, translated_texts, image_map)

# === Save new DOCX ===
doc.save("parseTest_converted.docx")
print("✅ Done.")
