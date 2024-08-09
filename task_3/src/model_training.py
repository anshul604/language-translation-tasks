# model_training.py
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

class TranslationModel:
    def __init__(self):
        self.model = make_pipeline(
            CountVectorizer(),
            MultinomialNB()
        )
    
    def train(self, df):
        try:
            print("Training with data:")
            print(df['English'].head())  # Print a few rows for inspection
            print(df['Hindi'].head())    # Print a few rows for inspection
            
            X = df['English']
            y = df['Hindi']
            self.model.fit(X, y)
            joblib.dump(self.model, 'Desktop/task_3/data/translation_model.pkl')  # Save path
            print("Model trained and saved successfully.")
        except Exception as e:
            print(f"Error while training the model: {e}")

    def load_model(self, path='Desktop/task_3/data/translation_model.pkl'):
        try:
            self.model = joblib.load(path)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading the model: {e}")

    def predict(self, text):
        try:
            return self.model.predict([text])[0]
        except Exception as e:
            print(f"Error while predicting: {e}")
            return None
