<<<<<<< Updated upstream
def route_to_model(text, target_lang):

    if target_lang == "bg":  
        from useModels.use_helsinkiBg import translate  
        return translate(text, "en", target_lang)

    elif target_lang == "cs":
        from useModels.use_helsinkiCs import translate  
        return translate(text, "en", target_lang)

    elif target_lang == "da":
        from useModels.use_helsinkiDa import translate  
        return translate(text, "en", target_lang)

    elif target_lang == "de":
        from useModels.use_helsinkiDe import translate  
        return translate(text, "en", target_lang)

=======
import sys
import json

def translate_for_single_language(text, source_lang, target_lang):
    if target_lang in ["fr", "de"]:
        from useModels.use_example import translate
        return {"target_lang": target_lang, "translated_text": translate(text=text, source_lang="eng_Latn", target_lang=f"{target_lang}_Latn")}
>>>>>>> Stashed changes
    elif target_lang in ["tr"]:
        from useModels.use_example import translate
        return {"target_lang": target_lang, "translated_text": translate(text=text, source_lang=source_lang, target_lang=target_lang)}
    elif target_lang in ["hu"]:
        from useModels.use_helsinki_hu import translate
<<<<<<< Updated upstream
        return translate(text)
    
    elif target_lang in ["sv"]:
        from useModels.use_helsinki_en_sv import translate
        return translate(text)
    
    elif target_lang in ["et"]:
        from useModels.use_helsinki_en_et import translate
        return translate(text)
    
    elif target_lang in ["el"]:
        from useModels.use_helsinki_en_el import translate
        return translate(text)
    
    elif target_lang in ["fr"]:
        from useModels.use_helsinki_en_fr import translate
        return translate(text)
    
    elif target_lang in ["fi"]:
        from useModels.use_helsinki_en_fi import translate
        return translate(text)
    
=======
        return {"target_lang": target_lang, "translated_text": translate(text=text, source_lang=source_lang, target_lang=target_lang)}
>>>>>>> Stashed changes
    elif target_lang in ["lt"]:
        from useModels.use_helsinki_lt import translate
        return {"target_lang": target_lang, "translated_text": translate(text=text, source_lang=source_lang, target_lang=target_lang)}
    elif target_lang in ["sk"]:
        from useModels.use_helsinki_sk import translate
        return {"target_lang": target_lang, "translated_text": translate(text=text, source_lang=source_lang, target_lang=target_lang)}
    else:
        return {"target_lang": target_lang, "translated_text": "No model available for this language"}


def route_to_model(text, source_lang, target_langs):
    translated_texts = []
    for target_lang in target_langs:
        translated_texts.append(translate_for_single_language(text, source_lang, target_lang))
    
    return translated_texts

if __name__ == "__main__":
    if len(sys.argv) < 4:  # Make sure there are enough arguments
        print("Usage: python model_router.py <source_text> <source_lang> <target_lang1> <target_lang2> ...")
        sys.exit(1)

    source_text = sys.argv[1]
    source_lang = sys.argv[2]
    target_langs = sys.argv[3:]

    translated_texts = route_to_model(source_text, source_lang, target_langs)

    # Print the result as a JSON array
    print(json.dumps(translated_texts))
