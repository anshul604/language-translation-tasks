import pickle

def translate(english_text, vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary):
    """Translate English text to French and Hindi using the trained models."""
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

    return french_text[0], hindi_text[0]

