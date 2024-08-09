# Language Translation Project

## Overview
This project is a language translation application that translates English text into Hindi using a Naive Bayes classifier model. The application includes a GUI that allows users to input English text and receive translations in Hindi.

## Project Structure

- **data_preparation.py**: Handles loading and preparing the dataset.
- **model_training.py**: Trains the translation model and handles model saving/loading.
- **gui.py**: Defines the graphical user interface for the application.
- **main.py**: The entry point for the application that ties together data loading, model training, and GUI creation.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your dataset in the CSV format and place it in the `Desktop/task_3/data/` directory with the filename `eng_hindi.csv`.

2. Run the application:
    ```bash
    python main.py
    ```

3. Enter English text into the GUI and click "Translate" to see the Hindi translation.

## File Paths

- **Data File**: `Desktop/task_3/data/eng_hindi.csv`
- **Model File**: `Desktop/task_3/data/translation_model.pkl`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions, please contact [your_email@example.com](mailto:your_email@example.com).
