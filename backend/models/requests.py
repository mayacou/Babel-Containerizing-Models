from typing import List, Optional
from pydantic import BaseModel

class TranslationRequest(BaseModel):
    pdf_file: Optional[str] = None  # Base64 encoded PDF content
    source_text: str
    source_language: str
    target_languages: List[str]
