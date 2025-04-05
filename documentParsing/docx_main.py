from docx import Document
from parsers.docx_parser import parse_docx
from ocr.ocr_docx import get_image_text
from overlay.docx_overlay import overlay_docx

def translate_docx(input_path):
   # Load document
   doc = Document(input_path)
   text_map = []
   image_map = []

   # Parse entire document
   text_map = parse_docx(doc, text_map)
   text_map, image_map = get_image_text(doc, text_map, image_map)
   
   # Pull texts to send for translation
   texts_to_translate = [entry.get("text") or entry.get("ocr_text") for entry in text_map]
   
   # Add this return here so the API can send back the info for overlay later
   # return texts_to_translate, text_map, image_map
   
   # Placeholder for now
   translated_texts = [text.upper() for text in texts_to_translate]
    
   # Overlay translations
   return overlay_docx(doc, text_map, translated_texts, image_map)

# Example usage
if __name__ == "__main__":
   input_file = "parseTest.docx"
   doc = translate_docx(input_file)
   doc.save("parseTest_converted.docx")
   print(f"✅ Done.")
