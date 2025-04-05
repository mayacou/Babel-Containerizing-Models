import torch
from transformers import MarianMTModel, MarianTokenizer

# DEBUG
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'helsinki_lt')
print(f"Model path: {model_path}")


MODEL_PATH = "./models/helsinki_lt"

_model = None
_tokenizer = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_helsinki_lt_model():
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        print("🔄 Loading model from disk...")
        _model = MarianMTModel.from_pretrained(MODEL_PATH).to(_device)
        _tokenizer = MarianTokenizer.from_pretrained(MODEL_PATH)
        print("✅ Model loaded!")
    return _model, _tokenizer, _device
