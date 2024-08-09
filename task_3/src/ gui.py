# gui.py
import tkinter as tk
from tkinter import messagebox
from model_training import TranslationModel
from data_preparation import load_data
from datetime import datetime
import threading

class TranslationApp:
    def __init__(self, root, model):
        self.root = root
        self.root.title("English to Hindi Translator")
        self.model = model

        self.label = tk.Label(root, text="Enter English text:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_thread)
        self.translate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def translate_thread(self):
        thread = threading.Thread(target=self.translate)
        thread.start()

    def translate(self):
        text = self.entry.get()
        error_message = self.handle_exceptions(text)
        if error_message:
            messagebox.showerror("Error", error_message)
            return

        self.display_error_message()

        translated_text = self.model.predict(text)
        if translated_text:
            self.result_label.config(text=f"Translated Text: {translated_text}")
        else:
            self.result_label.config(text="Error: Could not translate the text.")

    def handle_exceptions(self, word):
        vowels = ('a', 'e', 'i', 'o', 'u')
        if word[0].lower() in vowels:
            return "Error: Translation not available for words starting with a vowel."
        return None

    def display_error_message(self):
        now = datetime.now()
        if now.hour == 21 and now.minute <= 60:  # Between 9 PM and 10 PM IST
            messagebox.showerror("Error", "Translation service is not available between 9 PM and 10 PM IST.")
