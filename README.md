![Screenshot (1208)](https://github.com/user-attachments/assets/335a5420-cb2f-41d3-ba4d-55c1e82bd02a)
![Screenshot (1207)](https://github.com/user-attachments/assets/9130caaa-2524-448c-8455-996901a0bb63)
![Screenshot (1213)](https://github.com/user-attachments/assets/d6d13264-2621-4a23-aeff-118533d0dd88)
![Screenshot (1212)](https://github.com/user-attachments/assets/c939a4e5-dbcb-466b-8138-3b86bc003638)


# 📰 NewsWhizz - Smart News Summarization & TTS  

![NewsWhizz Banner](https://your-image-link.com)  <!-- Add a relevant banner image -->

## 📌 Overview  
**NewsWhizz** is a **news summarization and text-to-speech application** that fetches real-time news, generates concise summaries in **English & Hindi**, and provides **sentiment analysis**. It features a **dark & light mode toggle** for a better user experience.  

🔗 **Live Demo:** [Deployed App Link](https://huggingface.co/spaces/Rachuachar/NewsWhiz)  
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

