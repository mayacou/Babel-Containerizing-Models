from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-tc-big-en-et"

# Save model + tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./models/helsinki_en_et") #replace modelName
tokenizer.save_pretrained("./models/helsinki_en_et") #replace modelName

print("✅ Model saved locally to ./models/helsinki_en_et") #replace modelName