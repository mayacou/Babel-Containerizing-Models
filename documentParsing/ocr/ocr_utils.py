from PIL import Image
import pytesseract
import io

def ocr_image_bytes(image_bytes):
   image = Image.open(io.BytesIO(image_bytes))
   return pytesseract.image_to_string(image)

# bonus code
# all_blocks.sort(key=lambda b: b["bbox"][1])  # y0