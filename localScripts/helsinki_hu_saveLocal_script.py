from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-tc-big-en-hu"

# Save model + tokenizer
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

model.save_pretrained("./models/helsinki_hu") #replace modelName
tokenizer.save_pretrained("./models/helsinki_hu") #replace modelName

print("✅ Model saved locally to ./models/helsinki_hu") #replace modelName
