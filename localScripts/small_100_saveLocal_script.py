# load_small100.py
import torch
from transformers import M2M100ForConditionalGeneration

# come back to tokenzier

MODE_NAME = "alirezamsh/small100"
SAVE_PATH = "./models/small_100"
    
# Load model and tokenizer
model = M2M100ForConditionalGeneration.from_pretrained(MODE_NAME)
tokenizer = SMALL100Tokenizer.from_pretrained(MODE_NAME)
    
# Save model and tokenizer
model.save_pretrained(SAVE_PATH)
tokenizer.save_pretrained(SAVE_PATH)

print(f"✅ Model saved locally to {SAVE_PATH}")

