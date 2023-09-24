import tkinter as tk
from tkinter.font import Font


def button_click(button):
    text = button.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
    elif text == "del":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


def create_button(text, row, column):
    btn = tk.Button(window, text=text, font=("typewriter", 15), padx=10, pady=10, width=5, height=2)
    btn.grid(row=row, column=column, padx=5, pady=5)
    return btn


window = tk.Tk()
window.title("Calculator")
window.geometry("500x500")
window.configure(bg="blue")

entry = tk.Entry(window, font=("typewriter", 18))
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=10)

buttons = (
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    ".", "0", "=", "/",
    "del"
)

row = 1
column = 0
button_index = 0

while button_index < len(buttons):
    button_text = buttons[button_index]
    btn = create_button(button_text, row, column)
    column += 1
    if column > 3:
        column = 0
        row += 1
    button_index += 1

for row_index in range(1, 6):
    window.grid_rowconfigure(row_index, weight=1)

for column_index in range(4):
    window.grid_columnconfigure(column_index, weight=1)

for btn in window.winfo_children():
    btn.bind("<Button-1>", lambda e, button=btn: button_click(button))

window.mainloop()