import streamlit as st
from api import fetch_news
from utils import summarize_text, analyze_sentiment, text_to_speech
from utils_hindi import summarize_text_hindi
from components import header, footer, about

# Configure page settings
st.set_page_config(page_title="News Summarization & TTS", page_icon="📰", layout="wide")

# Initialize session state for dark mode
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    """Toggle between light and dark mode"""
    if st.session_state.theme == "light":
        st.session_state.theme = "dark"
    else:
        st.session_state.theme = "light"

# Sidebar Theme Toggle Button
st.sidebar.button("🌙 Toggle Dark Mode", on_click=toggle_theme)

# Apply CSS for themes and animations
dark_mode = """
 
    <style>
        body, .main, .stApp { background-color: #121212 !important; color: white !important; }
        .header { color: #9b59b6 !important; }
        .stTextInput>div>div>input { background-color: #222; color: white !important; border-color: #9b59b6; }
        .stTextInput label, .stRadio > label, .stRadio div { color: white !important; }
        .stButton>button { background-color: #9b59b6; color: white; font-size: 1.1em; border-radius: 10px; }
        .result-box { background-color: #222; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px #555; color: white; }

          /* Fix Sidebar Background */
        [data-testid="stSidebar"] {
            background-color: #1e1e1e !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
    </style>
"""

light_mode = """
    <style>
        body, .main, .stApp { background-color: #f4f4f4 !important; color: black !important; }
        .header { color: #3498db !important; }
        .stTextInput>div>div>input { background-color: white; color: black !important; border-color: #3498db; }
        .stButton>button { background-color: #3498db; color: white; font-size: 1.1em; border-radius: 10px; }
        .result-box { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px #aaa; }
    </style>
"""

if st.session_state.theme == "dark":
    st.markdown(dark_mode, unsafe_allow_html=True)
else:
    st.markdown(light_mode, unsafe_allow_html=True)

# Header
header()

# Page Navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "About":
    about()
else:
    st.markdown('<div class="header" style="text-align:center; font-size:2.5em; font-weight:bold;">📰 News Summarization & Text-to-Speech</div>', unsafe_allow_html=True)
    st.subheader("Fetch news, analyze sentiment & listen in Hindi or English!")

    # Input Fields
    company = st.text_input("🔍 Enter Company Name:")
    language = st.radio("🌍 Select Summary Language:", ("English", "Hindi"), horizontal=True)

    if st.button("Fetch News 📰"):
        articles = fetch_news(company)

        if not articles:
            st.error("❌ No news found!")
            st.stop()

        news_data = []
        for article in articles:
            title = article['title']
            content = article['description'] or article['content'] or ""
            summary = summarize_text(content) if language == "English" else summarize_text_hindi(content)
            sentiment = analyze_sentiment(summary)
            news_data.append({"title": title, "summary": summary, "sentiment": sentiment})

        st.markdown("## 📊 News Analysis")
        for data in news_data:
            with st.container():
                st.markdown(f"<div class='result-box'><b>📰 Title:</b> {data['title']}<br>", unsafe_allow_html=True)
                st.markdown(f"<b>📄 Summary ({language}):</b> {data['summary']}<br>", unsafe_allow_html=True)
                st.markdown(f"<b>📊 Sentiment:</b> {data['sentiment']}</div>", unsafe_allow_html=True)
                st.markdown("---")

        final_summary = ' '.join([item['summary'] for item in news_data])
        audio_file = text_to_speech(final_summary, language)
        st.audio(audio_file, format='audio/mp3')

# Footer
footer()
