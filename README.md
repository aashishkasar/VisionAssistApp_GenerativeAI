# VisionAssist

VisionAssist is an AI-powered application designed to assist visually impaired individuals. It provides:
- Scene descriptions using Google Gemini API
- Text extraction from images using Tesseract OCR
- Text-to-speech conversion using pyttsx3

## 🚀 Features
- **Scene Understanding**: Describes objects and their purposes.
- **Text Extraction**: Extracts text from images.
- **Text-to-Speech**: Reads extracted text aloud.

## 🛠 Installation
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

## 🔍 Tesseract OCR
Tesseract OCR is an open-source Optical Character Recognition (OCR) engine used for text extraction from images. It helps in converting printed or handwritten text in images into machine-readable text. 

### **How to Install Tesseract OCR**
#### **For Windows:**
1. Download the installer from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install and note the installation path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`)
3. Set the path in your Python script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

#### **For macOS/Linux:**
```bash
sudo apt install tesseract-ocr  # Ubuntu/Debian
brew install tesseract          # macOS (Homebrew)
```

## ▶️ Usage
Run the Streamlit app:
```bash
streamlit run app.py
```

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📧 Contact
For any inquiries, feel free to reach out!

---
© 2025 Aashish
