import os
import subprocess

def convert_docx_to_pdf(docx_path, output_pdf_path):
   subprocess.run([
      "libreoffice", "--headless", "--convert-to", "pdf", "--outdir",
      os.path.dirname(output_pdf_path), docx_path
   ], check=True)

def normalize_input_file(input_path):
   ext = os.path.splitext(input_path)[1].lower()
   if ext == ".pdf":
      return input_path
   elif ext == ".docx":
      output_pdf = os.path.splitext(input_path)[0] + "_converted.pdf"
      convert_docx_to_pdf(input_path, output_pdf)
      return output_pdf
   else:
      raise ValueError(f"Unsupported file type: {ext}")

