import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.value = 0
        root.title("Counter")
        self._build_ui()

    def _build_ui(self):
        self.label = tk.Label(self.root, text="Значение: 0",
                              font=("Arial", 24))
        self.label.pack(pady=20)
        tk.Button(self.root, text='+1',
                  command=self.increment).pack()
        tk.Button(self.root, text='0',
                  command=self.reset).pack()

    def increment(self):
        self.value += 1
        self.label['text'] = f"Значение: {self.value}"

    def reset(self):
        self.value = 0
        self.label['text'] = f"Значение: {self.value}"

if __name__ == "__main__":
    root = tk. Tk()
    app = CounterApp(root)
    root.mainloop()