# TODO make docx service
from typing import Optional

class DOCXService:
    async def extract_text_from_docx(self, docx_content: Optional[str]) -> str:
        """
        Extracts text from a base64-encoded docx file.
        """
        if not docx_content:
            return ""
        
        try:

            return None
        except Exception as e:
            raise Exception(f"DOCX extraction failed: {str(e)}")