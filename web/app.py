def route_to_model(text, target_lang):
<<<<<<< HEAD
<<<<<<< HEAD
    if target_lang in ["de"]:
        from useModels.use_example import translate
        return translate(text, "eng_Latn", f"{target_lang}_Latn")

    elif target_lang in ["fr"]:
        from useModels.use_helsinki_en_fr import translate
        return translate(text)
    
    elif target_lang in ["et"]:
        from useModels.use_helsinki_en_et import translate
        return translate(text)

    elif target_lang in ["el"]:
        from useModels.use_helsinki_en_el import translate
        return translate(text)
    
    elif target_lang in ["fi"]:
        from useModels. use_helsinki_en_fi import translate
        return translate(text)

=======
=======
>>>>>>> a0c426296e806d1c03fae531f7b2029cfd039ec2
    if target_lang in ["fr", "de"]:
        from useModels.use_example import translate
        return translate(text, "eng_Latn", f"{target_lang}_Latn")

<<<<<<< HEAD
>>>>>>> a0c4262 (added mbart config)
=======
>>>>>>> a0c426296e806d1c03fae531f7b2029cfd039ec2
    elif target_lang in ["tr"]:
        from useModels.use_example import translate
        return translate(text, "en", target_lang)

    else:
        return "❌ No model available for this language"


if __name__ == "__main__":
    # ✏️ Get user input
    text = input("Enter text to translate: ")
    target_lang = input("Enter target language code (e.g., fr, de, es): ")

    # 🌍 Translate text using the routed model
    translation = route_to_model(text, target_lang)

    print("✅ Translation:", translation)
