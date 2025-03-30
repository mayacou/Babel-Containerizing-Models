from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-sk"

# Save model + tokenizer
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

model.save_pretrained("./models/helsinki_sk") #replace modelName
tokenizer.save_pretrained("./models/helsinki_sk") #replace modelName

print("✅ Model saved locally to ./models/helsinki_sk") #replace modelName
