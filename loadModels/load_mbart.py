import torch
from transformers import MBartForConditionalGeneration, MBart50Tokenizer


MODEL_PATH = "./models/mbart"

_model = None
_tokenizer = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_mbart():
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        print("🔄 Loading model from disk...")
        _model = MBartForConditionalGeneration.from_pretrained(MODEL_PATH)
        _tokenizer = MBart50Tokenizer.from_pretrained(MODEL_PATH)
        print("✅ Model loaded!")
    return _model, _tokenizer, _device
