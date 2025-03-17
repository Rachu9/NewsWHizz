import streamlit as st

def header():
    """Displays the header section."""
    st.markdown("""
        <style>
            .header-container {
                text-align: center;
                font-size: 2.2em;
                font-weight: bold;
                color: #3498db;
            }
        </style>
        <div class="header-container">📰 News Summarization & TTS</div>
    """, unsafe_allow_html=True)

def footer():
    """Displays the footer section."""
    st.markdown("""
        <hr>
        <p style="text-align:center; color:gray;">© 2025 News TTS App | Created by Rachana</p>
    """, unsafe_allow_html=True)

def about():
    """Displays the About page."""
    st.title("📌 About This App")
    st.write("""
        The News Summarization & Text-to-Speech App allows users to:
        - Fetch **real-time news** about any company
        - Get **AI-generated summaries** in English and Hindi
        - Perform **sentiment analysis** to classify news as Positive, Negative, or Neutral
        - Convert summaries into **speech (TTS)** for better accessibility
        - Use **Dark Mode & Light Mode** for a customizable experience
        
        **Technologies Used:**  
        - Python, Streamlit, BeautifulSoup, TextBlob, gTTS, Sumy, Google Translate API
    """)
