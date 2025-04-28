from googletrans import Translator

def translate_text(text, dest_lang='hi'):
    translator = Translator()
    result = translator.translate(text, dest=dest_lang)
    return result.text
