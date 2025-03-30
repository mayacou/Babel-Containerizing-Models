from transformers import MBartForConditionalGeneration, MBart50Tokenizer

# Configuration
MODEL_NAME = "facebook/mbart-large-50-one-to-many-mmt"
SAVE_PATH = "./models/mbart"

# Load model and tokenizer
model = MBartForConditionalGeneration.from_pretrained(MODEL_NAME)
tokenizer = MBart50Tokenizer.from_pretrained(MODEL_NAME)

# Save model and tokenizer
model.save_pretrained(SAVE_PATH)
tokenizer.save_pretrained(SAVE_PATH)

print(f"✅ Model saved locally to {SAVE_PATH}")
