import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def normalize_input_file(input_path):
    ext = os.path.splitext(input_path)[1].lower()
    if ext not in [".pdf", ".docx"]:
        raise ValueError(f"Unsupported file type: {ext}")
    return input_path, ext

def write_text_to_pdf(text, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Use a small margin
    x = 50
    y = height - 50
    line_height = 12

    for line in text.splitlines():
        if y < 50:  # start a new page
            c.showPage()
            y = height - 50

        c.drawString(x, y, line)
        y -= line_height

    c.save()
