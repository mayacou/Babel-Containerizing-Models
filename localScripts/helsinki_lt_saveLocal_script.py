from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-tc-big-en-lt"

# Save model + tokenizer
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

model.save_pretrained("./models/helsinki_lt") #replace modelName
tokenizer.save_pretrained("./models/helsinki_lt") #replace modelName

print("✅ Model saved locally to ./models/helsinki_lt") #replace modelName