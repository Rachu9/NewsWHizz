from googletrans import Translator
from utils import summarize_text

def summarize_text_hindi(text):
    summary = summarize_text(text)
    translator = Translator()
    return translator.translate(summary, dest='hi').text
