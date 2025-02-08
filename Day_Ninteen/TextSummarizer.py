import nltk
import tkinter as tk
from tkinter import scrolledtext, filedialog
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from PyPDF2 import PdfReader
import string

# Download necessary components
nltk.download("punkt")
nltk.download("stopwords")

def load_file():
    """Loads text or PDF file and displays content in the text input area."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf")]
    )
    if file_path:
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
        elif file_path.endswith(".pdf"):
            content = extract_text_from_pdf(file_path)
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, content)

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            pdf = PdfReader(file)
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
    except Exception as e:
        return f"Error reading PDF: {e}"
    return text.strip()

def summarize_text():
    """Summarizes the input text by selecting the most important sentences."""
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        result_label.config(text="⚠️ Please enter some text or load a file!", fg="red")
        return

    try:
        num_sentences = int(sentence_count.get())
    except ValueError:
        result_label.config(text="⚠️ Enter a valid number!", fg="red")
        return

    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        summary_output.delete("1.0", tk.END)
        summary_output.insert(tk.END, text)
        result_label.config(text="✅ Text is already short, showing original!", fg="blue")
        return

    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english") + list(string.punctuation))

    # Remove stopwords and count word frequencies
    word_freq = Counter(word for word in words if word not in stop_words)

    # Score sentences based on word importance
    sentence_scores = {
        sent: sum(word_freq[word] for word in word_tokenize(sent.lower()) if word in word_freq)
        for sent in sentences
    }

    # Select top-scoring sentences for the summary
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary_text = " ".join(summary_sentences)

    summary_output.delete("1.0", tk.END)
    summary_output.insert(tk.END, summary_text)
    result_label.config(text="✅ Summary Generated!", fg="green")

def save_summary():
    """Saves the generated summary as a text file."""
    summary_text = summary_output.get("1.0", tk.END).strip()
    if not summary_text:
        result_label.config(text="⚠️ No summary to save!", fg="red")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Save Summary"
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(summary_text)
        result_label.config(text="✅ Summary saved!", fg="green")

# GUI Setup
root = tk.Tk()
root.title("Text Summarizer")
root.geometry("650x600")

tk.Label(root, text="Enter Text or Load a File:", font=("Arial", 12)).pack(pady=5)
text_input = scrolledtext.ScrolledText(root, height=8, width=70)
text_input.pack(pady=5)

tk.Button(root, text="Load File", command=load_file, font=("Arial", 10), bg="lightgreen").pack(pady=5)

tk.Label(root, text="Number of sentences:", font=("Arial", 12)).pack(pady=5)
sentence_count = tk.Entry(root)
sentence_count.insert(0, "3")
sentence_count.pack(pady=5)

tk.Button(root, text="Summarize", command=summarize_text, font=("Arial", 12), bg="lightblue").pack(pady=10)

tk.Label(root, text="Summary:", font=("Arial", 12)).pack(pady=5)
summary_output = scrolledtext.ScrolledText(root, height=6, width=70)
summary_output.pack(pady=5)

tk.Button(root, text="Save Summary", command=save_summary, font=("Arial", 10), bg="lightgray").pack(pady=5)

result_label = tk.Label(root, text="", fg="red")
result_label.pack()

root.mainloop()
