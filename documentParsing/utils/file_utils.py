import os
import platform
import subprocess
import shutil

from utils.logger import log_info, log_success, log_error

def convert_docx_to_pdf(docx_path, output_pdf_path):
    # Choose correct CLI command
    if platform.system() == "Windows":
        soffice_cmd = r"C:\Program Files\LibreOffice\program\soffice.exe"
    elif platform.system() == "Darwin":
         soffice_cmd = r"/Applications/LibreOffice.app/Contents/MacOS/soffice"
    else:
        soffice_cmd = "libreoffice"

    # Ensure CLI is available
    if not (os.path.isfile(soffice_cmd) or shutil.which(soffice_cmd)):
        log_error(f"LibreOffice CLI not found: {soffice_cmd}")
        raise EnvironmentError("LibreOffice CLI not found")

    output_dir = os.path.dirname(output_pdf_path)
    os.makedirs(output_dir, exist_ok=True)

    log_info(f"Starting DOCX to PDF conversion")
    log_info(f"Input DOCX: {docx_path}")
    log_info(f"Target folder: {output_dir}")

    # Run LibreOffice command
    subprocess.run([
        soffice_cmd,
        "--headless", "--convert-to", "pdf",
        "--outdir", output_dir,
        docx_path
    ], check=True)

    # LibreOffice will create: output_dir / [docx_basename].pdf
    base_name = os.path.splitext(os.path.basename(docx_path))[0]
    actual_path = os.path.join(output_dir, base_name + ".pdf")

    if not os.path.exists(actual_path):
        log_error(f"LibreOffice did not create expected file: {actual_path}")
        raise FileNotFoundError(f"No file found at: {actual_path}")

    # Rename to match desired output filename
    if actual_path != output_pdf_path:
        if os.path.exists(output_pdf_path):
            os.remove(output_pdf_path)
            log_info(f"Deleted existing file: {output_pdf_path}")
        os.rename(actual_path, output_pdf_path)
        log_info(f"Renamed {actual_path} → {output_pdf_path}")

    log_success(f"Converted: {docx_path} → {output_pdf_path}")
    return output_pdf_path


def normalize_input_file(input_path):
    ext = os.path.splitext(input_path)[1].lower()
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    if ext == ".pdf":
        return input_path
    elif ext == ".docx":
        output_pdf = os.path.join(output_dir, base_name + "_converted.pdf")
        return convert_docx_to_pdf(input_path, output_pdf)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
