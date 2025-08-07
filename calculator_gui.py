import tkinter as tk
import requests

BACKEND_URL = 'http://127.0.0.1:5000'

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator App')
        self.create_widgets()

    def create_widgets(self):
        self.entry_a = tk.Entry(self.root, width=10)
        self.entry_a.grid(row=0, column=0)
        self.entry_b = tk.Entry(self.root, width=10)
        self.entry_b.grid(row=0, column=2)

        self.result_label = tk.Label(self.root, text='Result: ')
        self.result_label.grid(row=1, column=0, columnspan=3)

        tk.Button(self.root, text='+', width=5, command=self.add).grid(row=0, column=1)
        tk.Button(self.root, text='-', width=5, command=self.subtract).grid(row=2, column=0)
        tk.Button(self.root, text='*', width=5, command=self.multiply).grid(row=2, column=1)
        tk.Button(self.root, text='/', width=5, command=self.divide).grid(row=2, column=2)

    def get_values(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            return a, b
        except ValueError:
            self.result_label.config(text='Result: Invalid input')
            return None, None

    def send_request(self, endpoint, a, b):
        try:
            response = requests.post(f'{BACKEND_URL}/{endpoint}', json={'a': a, 'b': b})
            data = response.json()
            if 'result' in data:
                self.result_label.config(text=f'Result: {data["result"]}')
            else:
                self.result_label.config(text=f'Result: {data.get("error", "Error")}')
        except Exception as e:
            self.result_label.config(text=f'Result: {e}')

    def add(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.send_request('add', a, b)

    def subtract(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.send_request('subtract', a, b)

    def multiply(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.send_request('multiply', a, b)

    def divide(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.send_request('divide', a, b)

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
