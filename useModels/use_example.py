from loadModels.load_Example import load_modelName

def translate(text: str, source_lang: str, target_lang: str) -> str:
    model, tokenizer, device = load_modelName()

    tokenizer.src_lang = source_lang
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(device)
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang)

    outputs = model.generate(
        **inputs,
        num_beams=5,
        length_penalty=1.2,
        early_stopping=False,
        forced_bos_token_id=forced_bos_token_id
    )
<<<<<<< HEAD
<<<<<<< HEAD
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
=======
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
>>>>>>> a0c4262 (added mbart config)
=======
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
>>>>>>> a0c426296e806d1c03fae531f7b2029cfd039ec2
