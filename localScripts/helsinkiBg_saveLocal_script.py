from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-tc-big-en-bg"

# Save model + tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./models/helsinkiBg") 
tokenizer.save_pretrained("./models/helsinkiBg")

print("✅ Model saved locally to ./models/helsinkiBg") 
