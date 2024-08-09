import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle
import tkinter as tk
from tkinter import messagebox

# Load the dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path, encoding='utf-8', usecols=['English', 'French', 'Hindi'])
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    return data

# Train the models
def train_models(data):
    X = data['English']
    y_french = data['French']
    y_hindi = data['Hindi']

    vectorizer = CountVectorizer()
    X_vect = vectorizer.fit_transform(X)
    vocabulary = set(vectorizer.get_feature_names_out())

    X_train, X_test, y_train_french, y_test_french = train_test_split(X_vect, y_french, test_size=0.2, random_state=42)
    X_train, X_test, y_train_hindi, y_test_hindi = train_test_split(X_vect, y_hindi, test_size=0.2, random_state=42)

    model_french = MultinomialNB()
    model_french.fit(X_train, y_train_french)

    model_hindi = MultinomialNB()
    model_hindi.fit(X_train, y_train_hindi)

    vectorizer_memory = pickle.dumps(vectorizer)
    model_french_memory = pickle.dumps(model_french)
    model_hindi_memory = pickle.dumps(model_hindi)

    return vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary

# Function to translate text
def translate(english_text, vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary):
    if len(english_text) != 10:
        return "Error: Only words with exactly 10 letters are allowed.", ""

    if english_text.lower() not in vocabulary:
        return "Error: Word not in database.", ""

    vectorizer = pickle.loads(vectorizer_memory)
    model_french = pickle.loads(model_french_memory)
    model_hindi = pickle.loads(model_hindi_memory)

    text_vect = vectorizer.transform([english_text])

    french_text = model_french.predict(text_vect)
    hindi_text = model_hindi.predict(text_vect)

    print(f"Input: {english_text}")
    print(f"French Prediction: {french_text[0]}")
    print(f"Hindi Prediction: {hindi_text[0]}")

    return french_text[0], hindi_text[0]

# GUI
def perform_translation(vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary):
    english_text = entry.get()
    french_text, hindi_text = translate(english_text, vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary)
    if french_text.startswith("Error") or hindi_text.startswith("Error"):
        messagebox.showerror("Error", f"French: {french_text}\nHindi: {hindi_text}")
    else:
        label_french_result.config(text=f"French: {french_text}")
        label_hindi_result.config(text=f"Hindi: {hindi_text}")

def create_gui(vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary):
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

def main():
    data_path = r"Desktop/task_1/data/eng_fr_hindi data - Sheet1.csv"  #  file path
    data = load_data(data_path)
    if data is not None:
        print("Column names in the dataset:", data.columns)

        vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary = train_models(data)

        create_gui(vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary)

if __name__ == "__main__":
    main()
