from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = ""

# Save model + tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./models/modelName") #replace modelName
tokenizer.save_pretrained("./models/modelName") #replace modelName

print("✅ Model saved locally to ./models/modelName") #replace modelName
