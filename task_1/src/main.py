from data_preparation import load_data
from model_training import train_models
from gui import create_gui

def main():
    """Main function to load data, train models, and run the GUI."""
    data_path = r"Desktop/task_1/data/eng_fr_hindi data - Sheet1.csv"  # file path
    data = load_data(data_path)
    if data is not None:
        print("Column names in the dataset:", data.columns)

        vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary = train_models(data)

        create_gui(vectorizer_memory, model_french_memory, model_hindi_memory, vocabulary)

if __name__ == "__main__":
    main()


