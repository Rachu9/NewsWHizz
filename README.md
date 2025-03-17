# 📰 NewsWhizz - Smart News Summarization & TTS  

![NewsWhizz Banner](https://your-image-link.com)  <!-- Add a relevant banner image -->

## 📌 Overview  
**NewsWhizz** is a **news summarization and text-to-speech application** that fetches real-time news, generates concise summaries in **English & Hindi**, and provides **sentiment analysis**. It features a **dark & light mode toggle** for a better user experience.  

🔗 **Live Demo:** [Deployed App Link](https://your-deployment-link.com)  
🔗 **GitHub Repository:** [NewsWhizz](https://github.com/Rachu9/NewsWHizz)  

---

## 🚀 Features  
✅ **Fetch Real-Time News** – Retrieves the latest news using News API.  
✅ **AI-Based Summarization** – Generates concise summaries using NLP.  
✅ **Sentiment Analysis** – Classifies news as **Positive, Negative, or Neutral**.  
✅ **Multi-Language Support** – Summarization available in **English & Hindi**.  
✅ **Text-to-Speech (TTS)** – Converts summaries into **audio (MP3 format)**.  
✅ **Dark & Light Mode** – Customizable UI for better readability.  
✅ **User-Friendly UI** – Built with **Streamlit** for a smooth experience.  

---

## 🛠️ Technology Stack  

| **Component**         | **Technology Used**       |
|----------------------|------------------------|
| **Frontend (UI)**     | Streamlit (Python-based) |
| **Backend (Processing)** | Python |
| **News Fetching**     | News API (via `requests`) |
| **Summarization**     | `sumy` (LSA algorithm) |
| **Sentiment Analysis** | `TextBlob` |
| **Translation (Hindi)** | `deep-translator` |
| **Text-to-Speech** | `gTTS (Google Text-to-Speech)` |
| **Deployment** | Hugging Face Spaces / Streamlit Cloud |
| **Version Control** | Git & GitHub |

---

## 📌 Installation & Setup  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Rachu9/NewsWHizz.git
cd NewsWHizz
2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed. Then, install all required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Application
bash
Copy
Edit
streamlit run app.py
📍 The app will launch in your browser at http://localhost:8501 🎉
![Uploading Screenshot (1212).png…]()
![Screenshot (1211)](https://github.com/user-attachments/assets/623ad302-4c53-439a-b5a6-29f8b2b3e361)
![Screenshot (1208)](https://github.com/user-attachments/assets/e6ed9236-459a-4485-9f02-9040d738a2e8)
![Screenshot (1207)](https://github.com/user-attachments/assets/b47ac5f7-65da-4929-853a-c72dec0c1f6f)


