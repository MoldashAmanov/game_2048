import tkinter as tk

root = tk.Tk()
root.title("2048 Макет")

# Шапка
header = tk.Frame(root)
header.pack(fill="x", padx=16, pady=(16, 6))

tk.Label(header, text='2048', font=("Arial", 36, "bold"), fg="#776e65").pack(side='left')

score = tk.Label(header, text='Счет: 0', font=("Arial", 36, 'bold'), fg="#776e65").pack(side='right', padx=10)

tk.Button(header, text='Новая игра').pack(side='right')

# Игровое поле
field = tk.Frame(root, width=400, height=400, bg='#bbada0')
field.pack(padx=16, pady=(6, 16))
field.pack_propagate(False)

tk.Label(field, text='Здесь будет поле', bg='#bbada0',
         fg='#eee4da').pack(expand=True)

root.mainloop()
