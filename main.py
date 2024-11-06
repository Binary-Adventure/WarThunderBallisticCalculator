from tkinter import Tk, N, S, E, W, Frame, Canvas
from math import sqrt


while ...:
    meters = input('Введи метраж квадратов карты: ')

    try:
        meters = int(meters)
        break

    except ValueError:
        print('\n ! Введите числовое значение\n')



win = Tk()
win.iconbitmap('icon.ico')
win.title(" ")
win.geometry('350x350')
win.attributes('-topmost', 10)
win.attributes('-alpha', 0.45)
win.resizable(False, False)
win.wm_attributes("-transparentcolor", "white")

frame = Frame(win, bd=1, bg="white")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

canvas = Canvas(frame, bd=0, bg="gray")
canvas.grid(row=0, column=0, sticky=N+S+E+W)
frame.pack(fill="both", expand=1)



def first_touch(event):
    global x1, y1
    x1, y1 = event.x, event.y

    try:
        canvas.delete(win.oval, win.line)

    except AttributeError:
        pass

    win.oval = canvas.create_oval(
        x1, y1,
        x1, y1,
        outline='lime',
        width=4
    )

def second_touch(event):
    x2, y2 = event.x, event.y

    win.line = canvas.create_line(
        x1, y1,
        x2, y2,
        fill='lime',
        arrow='last'
    )

    win.title(int(sqrt((x2 - x1)**2 + (y2 - y1)**2) / 45 * meters))

canvas.bind('<ButtonPress-1>', first_touch)
canvas.bind('<ButtonRelease-1>', second_touch)

win.mainloop()
