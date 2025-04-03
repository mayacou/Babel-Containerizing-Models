import pytesseract
from PIL import Image
from io import BytesIO

def get_image_text(doc, text_map, image_map):
   
   # === Step 3: Extract images and OCR ===
   for rel in doc.part._rels.values():
      if "image" in rel.target_ref:
         img_data = rel.target_part.blob
         image = Image.open(BytesIO(img_data))
         ocr_text = pytesseract.image_to_string(image).strip()

         if ocr_text:
            image_map.append({
               "image_blob": img_data,
               "ocr_text": ocr_text
            })

            # Add placeholder to text_map to translate and caption later
            text_map.append({
               "type": "ocr_image",
               "ocr_text": ocr_text
            })
   
   return text_map, image_map