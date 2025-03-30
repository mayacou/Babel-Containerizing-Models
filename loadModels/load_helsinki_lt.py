import torch
from transformers import MarianMTModel, MarianTokenizer

_model = None
_tokenizer = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_helsinki_lt_model():
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        print("🔄 Loading model from disk...")
        _model = MarianMTModel.from_pretrained("./models/helsinki_lt").to(_device)
        _tokenizer = MarianTokenizer.from_pretrained("./models/helsinki_lt")
        print("✅ Model loaded!")
    return _model, _tokenizer, _device
