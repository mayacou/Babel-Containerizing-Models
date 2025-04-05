from typing import List
from pydantic import BaseModel

class TranslatedText(BaseModel):
    target_lang: str
    translated_text: str

class Translation(BaseModel):
    source_text: str
    source_lang: str
    target_langs: List[str]
    translated_texts: List[TranslatedText]