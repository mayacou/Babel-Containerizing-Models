import pdfplumber
from ..utils.file_utils import write_text_to_pdf
def extract_embedded_text(pdf_path):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n\n"
    return full_text

def convert_pdf_to_clean_text_pdf(input_path, output_path):
    text = extract_embedded_text(input_path)
    write_text_to_pdf(text, output_path)