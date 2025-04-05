# TODO make pdf service
from typing import Optional

class PDFService:
    async def extract_text_from_pdf(self, pdf_content: Optional[str]) -> str:
        """
        Extracts text from a base64-encoded PDF file using pdfminer (no subprocesses).
        """
        if not pdf_content:
            return ""
        
        try:

            return None
        except Exception as e:
            raise Exception(f"PDF extraction failed: {str(e)}")