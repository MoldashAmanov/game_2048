import tkinter as tk

root = tk.Tk()
root.title('Управление стрелками')
root.geometry('400x600')

canvas = tk.Canvas(root, bg='white')
canvas.pack(fill='both', expand=True)

rect = canvas.create_rectangle(20, 0, 50, 50, fill="#f2b179")

def on_key(event):
    step = 15
    moves = {'Left': (-step, 0), 'Right': (step, 0),
             'Up': (0, -step), 'Down': (0, step)}
    dx, dy = moves.get(event.keysym, (0, 0))
    canvas.move(rect, dx, dy)

root.bind("<Key>", on_key)
root.mainloop()
