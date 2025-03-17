from textblob import TextBlob
from gtts import gTTS
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 2)
    return ' '.join([str(sentence) for sentence in summary])

def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

def text_to_speech(text, language):
    lang_code = "en" if language == "English" else "hi"
    tts = gTTS(text=text, lang=lang_code)
    tts.save("output.mp3")
    return "output.mp3"
