import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

_model = None
_tokenizer = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_modelName():
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        print("🔄 Loading model from disk...")
        _model = AutoModelForSeq2SeqLM.from_pretrained("models/modelName").to(_device)
        _tokenizer = AutoTokenizer.from_pretrained("models/modelName")
        print("✅ Model loaded!")
    return _model, _tokenizer, _device
