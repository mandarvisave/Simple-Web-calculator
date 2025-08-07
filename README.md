# Calculator App

A simple calculator application with a Python Flask backend and two frontends:
- A desktop GUI using Tkinter
- A web app using Streamlit

## Features
- Basic arithmetic operations: Add, Subtract, Multiply, Divide
- Web interface (Streamlit) and desktop GUI (Tkinter)
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

### 3. (Optional) Run the Desktop GUI
```sh
python calculator_gui.py
```

## Project Structure
- `backend.py` - Flask backend API
- `calculator_gui.py` - Tkinter desktop GUI
- `calculator_streamlit.py` - Streamlit web frontend
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
