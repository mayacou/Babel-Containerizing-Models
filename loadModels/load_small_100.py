import torch
from transformers import M2M100ForConditionalGeneration
from local_tokenizers.small_100 import SMALL100Tokenizer

MODEL_PATH = "./models/small_100"

_model = None
_tokenizer = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_small_100():
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        print("🔄 Loading model from disk...")
        _model = M2M100ForConditionalGeneration.from_pretrained(MODEL_PATH)
        _tokenizer = SMALL100Tokenizer.from_pretrained(MODEL_PATH)
        print("✅ Model loaded!")
    return _model, _tokenizer, _device
