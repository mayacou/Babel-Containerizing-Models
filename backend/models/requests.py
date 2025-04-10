from typing import List, Optional
from pydantic import BaseModel

class TranslationRequest(BaseModel):
    pdf_file: Optional[str] = None       # Base64 encoded PDF
    docx_file: Optional[str] = None      # Base64 encoded DOCX
    source_text: Optional[str] = None    # Raw text fallback
    source_language: str
    target_languages: List[str]
