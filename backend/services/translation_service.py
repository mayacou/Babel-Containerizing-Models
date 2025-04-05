from typing import List 
from scripts.model_router import route_to_model
from models.traslation import Translation, TranslatedText  

class TranslationService:
    async def translate_text(
        self, 
        source_text: str, 
        source_lang: str, 
        target_langs: List[str] 
    ) -> Translation:
        try:
            translated_texts = route_to_model(source_text, source_lang, target_langs)
            return Translation(
                source_text=source_text,
                source_lang=source_lang,
                target_langs=target_langs,
                translated_texts=[TranslatedText(**t) for t in translated_texts]
            )
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}")