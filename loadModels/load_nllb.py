import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_PATH = "./models/nllb_200"

_model = None
_tokenizer = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_nllb():
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        print("🔄 Loading NLLB-200 model from disk...")
        _model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        print("✅ NLLB-200 Model loaded!")
    return _model, _tokenizer, _device
