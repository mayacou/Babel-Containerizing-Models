import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

_model = None
_tokenizer = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_helsinkiDe():
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        print("🔄 Loading helsinkiDe from disk...")
        _model = AutoModelForSeq2SeqLM.from_pretrained("models/helsinkiDe").to(_device)
        _tokenizer = AutoTokenizer.from_pretrained("models/helsinkiDe")
        print("✅ helsinkiDe loaded!")
    return _model, _tokenizer, _device
