# Calculator App

A simple calculator application with a Python Flask backend and a modern web frontend using Streamlit.

## Features
- Basic arithmetic operations: Add, Subtract, Multiply, Divide
- Web interface (Streamlit)
- Backend API (Flask) for calculations

## Requirements
- Python 3.7+
- pip

## Installation
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd <repo-directory>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### 1. Start the Backend
```sh
python backend.py
```

### 2. Run the Web App (Streamlit)
```sh
streamlit run calculator_streamlit.py
```
Visit [http://localhost:8501](http://localhost:8501) in your browser.

## Project Structure
- `backend.py` - Flask backend API
- `calculator_streamlit.py` - Streamlit web frontend
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## Optional: Desktop GUI (Legacy)
A Tkinter-based desktop GUI (`calculator_gui.py`) is also included for reference, but the main interface is the Streamlit web app.

To run the desktop GUI (optional):
```sh
python calculator_gui.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



