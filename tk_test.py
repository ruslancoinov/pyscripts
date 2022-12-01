import tkinter as tk


# Window configuration
window = tk.Tk()
window.title('Numeral System Calculator')
window.geometry('428x480+500+300')
window.resizable(False, False)
window.config(bg='black')

#
def add_symbol():
    pass


# Window output
x, y = 10, 100
for i in range(2):
    tk.Entry().place(x=x, y=y, width=350, height=40)
    if x == 10:
        y += 100

# Buttons
buttons = ['1', '2', '3', '4', '5', 'CL', '6', '7', '8', '9', 'A', 'DEL', 'B', 'C', 'D', 'E', 'F', '0']
x, y = 10, 266

for i in range(len(buttons)):
    tk.Button(text=buttons[i], bg='white', font=('Arial', 16), command=add_symbol).place(x=x, y=y, width=68, height=68)
    x += 68
    if x == 418:
        x = 10
        y += 68

tk.Button(text='copy', bg='white', font=('Arial', 10)).place(x=375, y=200, width=38, height=40)


window.mainloop()