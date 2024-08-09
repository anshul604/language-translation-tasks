import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def train_models(data):
    """Train translation models and return pickled models and vectorizer."""
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

