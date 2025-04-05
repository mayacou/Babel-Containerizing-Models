from fastapi import APIRouter, FastAPI
from controllers.translationController import handle_translation_request

def setup_routes(app: FastAPI):
    router = APIRouter()
    router.add_api_route("/api/translate", handle_translation_request, methods=["POST"])
    app.include_router(router)