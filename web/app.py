import sys
import json

def translate_for_single_language(text, source_lang, target_lang):
    if target_lang in ["fr", "de"]:
        from useModels.use_example import translate
        return {"target_lang": target_lang, "translated_text": translate(text, "eng_Latn", source_lang, f"{target_lang}_Latn")}
    elif target_lang in ["tr"]:
        from useModels.use_example import translate
        return {"target_lang": target_lang, "translated_text": translate(text = text,  source_lang=source_lang, target_lang=target_lang)}
    elif target_lang in ["hu"]:
        from useModels.use_helsinki_hu import translate
        return {"target_lang": target_lang, "translated_text": translate(text)}
    elif target_lang in ["lt"]:
        from useModels.use_helsinki_lt import translate
        return {"target_lang": target_lang, "translated_text": translate(text)}
    elif target_lang in ["sk"]:
        from useModels.use_helsinki_sk import translate
        return {"target_lang": target_lang, "translated_text": translate(text)}
    else:
        return {"target_lang": target_lang, "translated_text": "No model available for this language"}

def route_to_model(text, source_lang, target_langs):
    translated_texts = []
    for target_lang in target_langs:
        translated_texts.append(translate_for_single_language(text, source_lang, target_lang))
    
    return translated_texts

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python model_router.py <source_text> <source_lang> <target_lang1> <target_lang2> ...")
        sys.exit(1)

    source_text = sys.argv[1]
    source_lang = sys.argv[2]
    target_langs = sys.argv[3:]

    translated_texts = route_to_model(source_text, source_lang, target_langs)

    print(json.dumps(translated_texts))
