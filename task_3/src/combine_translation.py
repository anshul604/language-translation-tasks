import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import threading

# Define the Translation Model
class TranslationModel:
    def __init__(self):
        self.model = make_pipeline(
            CountVectorizer(),
            MultinomialNB()
        )
    
    def train(self, csv_path):
        try:
            df = pd.read_csv(csv_path)
            print("CSV file loaded successfully.")
            print("Columns in DataFrame:", df.columns)
            
            # Strip any whitespace from column names
            df.columns = df.columns.str.strip()
            
            if 'English' not in df.columns or 'Hindi' not in df.columns:
                raise ValueError("CSV file must contain 'English' and 'Hindi' columns.")
            
            # Ensure to handle missing values
            df.dropna(inplace=True)
            
            X = df['English']
            y = df['Hindi']
            print("Training with data:")
            print(X.head())  # Print a few rows for inspection
            print(y.head())  # Print a few rows for inspection
            self.model.fit(X, y)
            joblib.dump(self.model, 'translation_model.pkl')
            print("Model trained and saved successfully.")
        except Exception as e:
            print(f"Error while training the model: {e}")
    
    def predict(self, text):
        try:
            # Use the pre-loaded model
            print(f"Predicting for text: {text}")  # Debugging statement
            return self.model.predict([text])[0]
        except Exception as e:
            print(f"Error while predicting: {e}")
            return None

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

# Path to the new CSV file
csv_path = r"Desktop/task_3/data/eng_hindi.csv"  # Updated file path

# Initialize and train the model
model = TranslationModel()
model.train(csv_path)

# Load the model once at the start
model.model = joblib.load('translation_model.pkl')
print("Model loaded successfully at the start.")

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

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_thread)
        self.translate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def translate_thread(self):
        thread = threading.Thread(target=self.translate)
        thread.start()

    def translate(self):
        text = self.entry.get()
        error_message = handle_exceptions(text)
        if error_message:
            messagebox.showerror("Error", error_message)
            return

        display_error_message()

        translated_text = self.model.predict(text)
        print(f"Translated text: {translated_text}")  # Debugging statement
        if translated_text:
            self.result_label.config(text=f"Translated Text: {translated_text}")
        else:
            self.result_label.config(text="Error: Could not translate the text.")

# Create and run the GUI application
root = tk.Tk()
app = TranslationApp(root)
root.mainloop()