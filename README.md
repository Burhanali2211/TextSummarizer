# Text Summarizer

## 📌 Overview
This is a **Text Summarizer** tool built using **Python, NLTK, Tkinter, and PyPDF2**. It allows users to:
✅ Load text from a **file (.txt, .pdf) or manual input**  
✅ **Summarize** the text by extracting the most important sentences  
✅ **Customize** the summary length  
✅ **Save the summary** as a `.txt` file  

This project is designed for **quick text analysis and summarization** using **Natural Language Processing (NLP)**.

---

## 🚀 Features
✔ **Load Text from File** (Supports `.txt` and `.pdf`)  
✔ **Tokenization** using `nltk.sent_tokenize()`  
✔ **Stopword Removal** for accurate keyword extraction  
✔ **Sentence Ranking** using word frequency  
✔ **Customizable Summary Length**  
✔ **Simple GUI Interface** using `Tkinter`  
✔ **Save Summary as a .txt File**  

---

## 📂 Installation
### 1️⃣ Install Required Libraries
Make sure you have **Python 3.9+** installed, then run:
```sh
pip install nltk PyPDF2 tk
```

### 2️⃣ Download NLTK Data
Run this in Python:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 3️⃣ Run the Script
```sh
python text_summarizer.py
```

---

## 📖 Usage
1️⃣ Open the program and **enter text manually** or **load a file**  
2️⃣ **Set the number of sentences** you want in the summary  
3️⃣ Click **Summarize** to generate the output  
4️⃣ Click **Save Summary** to export it as a `.txt` file  

---

## 🛠 Troubleshooting
### ❌ `LookupError: Resource punkt_tab not found`
✅ Run the following in Python:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```
If the error persists, **delete the `nltk_data` folder** from:
```
C:\Users\<your-username>\AppData\Roaming\nltk_data
```
Then reinstall:
```sh
pip uninstall nltk
pip install nltk
```

---

## 📜 License
This project is **open-source** and available under the **MIT License**. Feel free to use and modify it! 😊

