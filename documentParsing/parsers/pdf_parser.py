import fitz
from ocr.ocr_utils import ocr_image_bytes  # you’ll create this

def extract_text_blocks_combined(pdf_path):
    doc = fitz.open(pdf_path)
    all_pages = []

    for page in doc:
        # 1. Extract embedded text blocks
        embedded_blocks = []
        for b in page.get_text("blocks"):
            x0, y0, x1, y1, text, *_ = b
            if text.strip():
                embedded_blocks.append({
                    "text": text.strip(),
                    "bbox": (x0, y0, x1, y1),
                    "source": "embedded"
                })

        # 2. Extract and OCR any image blocks
        ocr_blocks = []
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            ocr_text = ocr_image_bytes(image_bytes)
            if ocr_text.strip():
                # Placeholder bbox if needed
                ocr_blocks.append({
                    "text": ocr_text.strip(),
                    # TODO: Use actual image position if needed: page.get_image_bbox(xref)
                    "bbox": (50, 50 + img_index * 50, 400, 100 + img_index * 50),
                    "source": "ocr"
                })

        # 3. Merge both block types
        all_blocks = embedded_blocks + ocr_blocks
        all_pages.append(all_blocks)

    return all_pages
