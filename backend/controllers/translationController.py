from fastapi import Request, HTTPException
from models.requests import TranslationRequest
from services.pdf_service import PDFService
from services.translation_service import TranslationService

async def handle_translation_request(request: Request):
    try:
        # Decode request
        request_data = await request.json()
        translation_request = TranslationRequest(**request_data)
        
        # Initialize services
        pdf_service = PDFService()
        translation_service = TranslationService()
        
        # Extract text
        text_to_translate = await extract_text_for_translation(translation_request, pdf_service)
        
        # Translate
        translation = await translation_service.translate_text(
            text_to_translate,
            translation_request.source_language,
            translation_request.target_languages
        )
        
        return translation
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def extract_text_for_translation(request: TranslationRequest, pdf_service: PDFService) -> str:
    if request.pdf_file:
        return await pdf_service.extract_text_from_pdf(request.pdf_file)
    return request.source_text