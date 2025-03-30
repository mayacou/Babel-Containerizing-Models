from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-en-sv"

# Save model + tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./models/helsinki_en_sv") #replace modelName
tokenizer.save_pretrained("./models/helsinki_en_sv") #replace modelName

print("✅ Model saved locally to ./models/helsinki_en_sv") #replace modelName