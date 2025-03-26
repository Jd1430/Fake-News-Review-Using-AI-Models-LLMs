import google.generativeai as genai
import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load Google Gemini API Key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)  # Set API key for Gemini

# Function to extract text from a URL
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join([p.get_text() for p in paragraphs])
    except Exception as e:
        return f"Error extracting content: {str(e)}"

# Function to check fake news using Google Gemini API
def check_fake_news(text):
    prompt = ("Analyze the following news article and determine if it is real or fake. "
              "Provide reasoning and a confidence level.\n\n" + text)
    
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Corrected model initialization
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"

# Streamlit UI
st.title("Fake News Detector")
option = st.radio("Choose input type:", ("Enter Text", "Enter URL"))

if option == "Enter Text":
    user_input = st.text_area("Paste the news article text below:")
    if st.button("Check News") and user_input:
        result = check_fake_news(user_input)
        st.write("### Analysis Result:")
        st.write(result)

elif option == "Enter URL":
    url_input = st.text_input("Enter the news article URL:")
    if st.button("Check News") and url_input:
        extracted_text = extract_text_from_url(url_input)
        if "Error" not in extracted_text:
            result = check_fake_news(extracted_text)
            st.write("### Analysis Result:")
            st.write(result)
        else:
            st.error(extracted_text)