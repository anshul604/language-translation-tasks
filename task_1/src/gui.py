import tkinter as tk
from tkinter import messagebox
from translator import translate

def perform_translation(vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary):
    """Perform translation and update GUI with results."""
    english_text = entry.get()
    french_text, hindi_text = translate(english_text, vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary)
    if french_text.startswith("Error") or hindi_text.startswith("Error"):
        messagebox.showerror("Error", f"French: {french_text}\nHindi: {hindi_text}")
    else:
        label_french_result.config(text=f"French: {french_text}")
        label_hindi_result.config(text=f"Hindi: {hindi_text}")

def create_gui(vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary):
    """Create and run the GUI."""
    global entry, label_french_result, label_hindi_result

    root = tk.Tk()
    root.title("Language Translator")

    entry = tk.Entry(root, width=40)
    entry.grid(row=0, column=1, padx=10, pady=10)

    label_english = tk.Label(root, text="Enter English Text:")
    label_english.grid(row=0, column=0, padx=10, pady=10)

    label_french_result = tk.Label(root, text="French: ")
    label_french_result.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    label_hindi_result = tk.Label(root, text="Hindi: ")
    label_hindi_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    button_translate = tk.Button(root, text="Translate", command=lambda: perform_translation(vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary))
    button_translate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()
