import fitz  # PyMuPDF

def overlay_translated_text(input_pdf, translated_blocks_per_page, output_pdf):
    doc = fitz.open(input_pdf)

    for page_index, page in enumerate(doc):
        translated_blocks = translated_blocks_per_page[page_index]
        for block in translated_blocks:
            x0, y0, x1, y1 = block["bbox"]
            text = block["text"]

            # 1. Draw white rectangle to "erase" original text
            rect = fitz.Rect(x0, y0, x1, y1)
            page.draw_rect(rect, fill=(1, 1, 1), color=None)

            # 2. Estimate font size based on height
            height = y1 - y0
            font_size = min(max(height * 0.7, 6), 14)  # keeps it between 6 and 14pt

            # 3. Insert wrapped text using textbox
            page.insert_textbox(
                rect,
                text,
                fontsize=font_size,
                fontname="helv",  # Helvetica (default), or "Times-Roman"
                align=0,  # 0 = left, 1 = center, 2 = right, 3 = justify
            )

    doc.save(output_pdf)
    print(f"✅ Overlay saved to: {output_pdf}")
