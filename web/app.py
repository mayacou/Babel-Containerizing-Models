def route_to_model(text, target_lang):
    if target_lang in ["fr", "de"]:
        from useModels.use_example import translate
        return translate(text, "eng_Latn", f"{target_lang}_Latn")

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
