from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-en-da"

# Save model + tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./models/helsinkiDa") 
tokenizer.save_pretrained("./models/helsinkiDa") 

print("✅ Model saved locally to ./models/helsinkiDa") 
