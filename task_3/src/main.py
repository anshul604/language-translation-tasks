# main.py
from data_preparation import load_data
from model_training import TranslationModel
from gui import TranslationApp
import tkinter as tk

def main():
    """Main function to load data, train models, and run the GUI."""
    data = load_data()
    
    if data is not None:
        print("Column names in the dataset:", data.columns)
        
        model = TranslationModel()
        model.train(data)  # Train the model
        
        model.load_model()  # Load the trained model

        # Create and run the GUI application
        root = tk.Tk()
        app = TranslationApp(root, model)
        root.mainloop()

if __name__ == "__main__":
    main()
