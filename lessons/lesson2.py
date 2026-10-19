import tkinter as tk

root = tk.Tk()
root.title("Counter")
root.geometry("300x400")
value = 0

def increment():
    global value
    value += 1
    label['text'] = f"Значение {value}"

label = tk.Label(root, text="Значение: 0", font=('Arial', 24))
label.pack()

button = tk.Button(root, text='+1', command=increment)
button.pack()

root.mainloop()