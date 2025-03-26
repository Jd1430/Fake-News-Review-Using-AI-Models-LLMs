# 📰 Fake-News-Review-Using-AI-Models-LLMs

This project is a **Streamlit-based web app** that detects **fake news** by analyzing text or extracting content from a URL using **Google Gemini AI**.

## 🚀 Features
- 🔍 **Analyze text-based news articles**
- 🌐 **Extract and analyze news from URLs**
- 🤖 **Leverages Google Gemini AI for fact-checking**
- 📊 **Provides reasoning and confidence level for fake news detection**

## Output Snapshots
- ![Screenshot 2025-03-26 145503](https://github.com/user-attachments/assets/83dc93df-f947-43d8-aaed-e7b4179d813e)
- ![Screenshot 2025-03-26 145632](https://github.com/user-attachments/assets/1d4317f1-030e-4c71-ace5-329bd29aaff3)
- ![Screenshot 2025-03-26 150313](https://github.com/user-attachments/assets/317000eb-9167-47f6-9ba7-0113bd39ece6)




## 🛠️ Installation

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
```

### Install Dependencies

Ensure you have **Python 3.7+** installed, then run:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the project directory and add your **Google Gemini API Key**:

```
GEMINI_API_KEY=your_api_key_here
```

## ▶️ Running the App

Launch the Streamlit app with:

```bash
streamlit run app.py
```

## 📂 File Structure

```
📂 fake-news-detector
│── app.py                 # Main Streamlit application
│── requirements.txt        # Dependencies
│── .env                    # API key (to be created by user)
```

## 🖼️ Usage

### 1️⃣ Enter Text
- Paste a news article into the text area.
- Click **Check News** to analyze it.
- The app will determine if the news is real or fake and provide reasoning.

### 2️⃣ Enter URL
- Provide a URL to a news article.
- The app will extract the content and analyze it using Google Gemini AI.
- Click **Check News** to see the result.

## 🔗 Contact
For any questions or collaborations, feel free to reach out:
- **GitHub**: [Jd1430](https://github.com/Jd1430)
- **Email**: jayanthdevarajgowda@gmail.com
  
💡 **Contributions are welcome!** Feel free to fork this repository and submit pull requests. 🚀
