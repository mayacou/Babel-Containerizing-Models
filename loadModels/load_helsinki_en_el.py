import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_PATH = "./models/helsinki_en_el"

_model = None
_tokenizer = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_helsinki_en_el():
   global _model, _tokenizer
   if _model is None or _tokenizer is None:
      print("🔄 Loading model from disk...")
      _model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH).to(_device)
      _tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
      print("✅ Model loaded!")
   return _model, _tokenizer, _device