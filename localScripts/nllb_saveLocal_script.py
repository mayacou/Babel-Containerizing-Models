from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Model name and path
MODEL_NAME = "facebook/nllb-200-distilled-600M"
SAVE_PATH = "./models/nllb_200"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Save model and tokenizer
model.save_pretrained(SAVE_PATH)
tokenizer.save_pretrained(SAVE_PATH)

print(f"✅ NLLB-200 Model and tokenizer saved locally to {SAVE_PATH}")
