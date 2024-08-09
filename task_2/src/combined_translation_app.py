import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Define the Translation Model
class TranslationModel:
    def __init__(self):
        self.model = make_pipeline(
            CountVectorizer(),
            MultinomialNB()
        )
    
    def train(self, csv_file_path):
        df = pd.read_csv(csv_file_path)
        # Drop rows with missing values in 'English' or 'Hindi' columns
        df.dropna(subset=['English', 'Hindi'], inplace=True)
        X = df['English']
        y = df['Hindi']
        self.model.fit(X, y)
        joblib.dump(self.model, 'translation_model.pkl')
    
    def predict(self, text):
        model = joblib.load('translation_model.pkl')
        return model.predict([text])[0]

# Define exception handling
def handle_exceptions(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if word[0].lower() in vowels:
        return "Error: Translation not available for words starting with a vowel."
    return None

# Define error message display
def display_error_message():
    now = datetime.now()
    if now.hour == 21 and now.minute <= 60:  # Between 9 PM and 10 PM IST
        print("Error: Translation service is not available between 9 PM and 10 PM IST.")

# Path to the CSV file
csv_file_path = r"C:\Users\USER\Downloads\Dataset_English_Hindi.csv"

# Initialize and train the model
model = TranslationModel()
model.train(csv_file_path)

# Define the GUI application
class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English to Hindi Translator")
        self.model = model

        self.label = tk.Label(root, text="Enter English text:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate)
        self.translate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def translate(self):
        text = self.entry.get()
        error_message = handle_exceptions(text)
        if error_message:
            messagebox.showerror("Error", error_message)
            return

        display_error_message()

        translated_text = self.model.predict(text)
        self.result_label.config(text=f"Translated Text: {translated_text}")

# Create and run the GUI application
root = tk.Tk()
app = TranslationApp(root)
root.mainloop()
