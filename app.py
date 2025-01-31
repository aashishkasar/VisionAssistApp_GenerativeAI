import streamlit as st
from PIL import Image
import pyttsx3
import pytesseract
import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI

# Configure Tesseract OCR Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set API Key for Google Generative AI
GEMINI_API_KEY = " "  # Replace with your valid API key 
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# Initialize Google Generative AI
llm = GoogleGenerativeAI(model="gemini-1.5-pro", api_key=GEMINI_API_KEY)

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Add Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f7f9fc;
        }
        .main-title {
            font-size: 42px;
            font-weight: 600;
            text-align: center;
            color: #4A90E2;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 18px;
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        .section-title {
            font-size: 22px;
            font-weight: 600;
            margin-top: 30px;
            margin-bottom: 15px;
            color: #333;
        }
        button {
            background-color: #4A90E2 !important;
            color: white !important;
            border-radius: 5px !important;
        }
        footer {
            text-align: center;
            margin-top: 50px;
            color: #777;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Information
st.sidebar.title("ℹ️ About VisionAssist")
st.sidebar.info(
    "VisionAssist is an AI-powered application designed to assist visually impaired individuals. "
    "It provides scene descriptions, text extraction from images, and text-to-speech conversion. "
    "Built using Streamlit and powered by Google Gemini API."
)

# Application Title and Subtitle
st.markdown('<div class="main-title">VisionAssist</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI for Scene Understanding, Text Extraction, and Speech for the Visually Impaired</div>',
    unsafe_allow_html=True,
)

# Function Definitions
def extract_text(image):
    """Extract text from an image using Tesseract OCR."""
    return pytesseract.image_to_string(image)


def text_to_speech(text):
    """Convert text to speech using pyttsx3."""
    engine.say(text)
    engine.runAndWait()


def generate_scene_description(prompt, image_data):
    """Generate a scene description using Google Generative AI."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([prompt, image_data[0]])
    return response.text


# Input Prompt for Scene Understanding
input_prompt = """
You are an AI assistant helping visually impaired individuals by describing the scene in the image. Provide:
1. A list of detected items and their purposes.
2. An overall description of the image.
3. Suggestions or precautions for visually impaired users.
"""

# Image Upload Section
st.markdown('<div class="section-title">📤 Upload an Image</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Features Section
st.markdown('<div class="section-title">⚙️ Features</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

scene_button = col1.button("🔍 Describe Scene")
ocr_button = col2.button("📝 Extract Text")
tts_button = col3.button("🔊 Text-to-Speech")

# Process User Actions
if uploaded_file:
    # Prepare image data for Google Generative AI
    image_data = [{"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}]

    # Describe Scene
    if scene_button:
        with st.spinner("Generating scene description..."):
            try:
                description = generate_scene_description(input_prompt, image_data)
                st.markdown('<div class="section-title">🔍 Scene Description</div>', unsafe_allow_html=True)
                st.write(description)
            except Exception as e:
                st.error(f"Error generating scene description: {e}")

    # Extract Text
    if ocr_button:
        with st.spinner("Extracting text..."):
            try:
                extracted_text = extract_text(image)
                st.markdown('<div class="section-title">📝 Extracted Text</div>', unsafe_allow_html=True)
                st.text_area("Extracted Text", extracted_text, height=200)
            except Exception as e:
                st.error(f"Error extracting text: {e}")

    # Text-to-Speech
    if tts_button:
        with st.spinner("Converting text to speech..."):
            try:
                extracted_text = extract_text(image)
                if extracted_text.strip():
                    text_to_speech(extracted_text)
                    st.success("✅ Text-to-Speech completed!")
                else:
                    st.warning("No text found in the image.")
            except Exception as e:
                st.error(f"Error converting text to speech: {e}")

# Footer
st.markdown(
    """
    <footer>
        <p>Powered by <strong>Google Gemini API</strong> | Built with ❤️ using Streamlit</p>
        <p>&copy; 2025 Aashish</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
