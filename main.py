from tkinter import Tk, N, S, E, W, SUNKEN, BOTH, Frame, Canvas
from math import sqrt


while ...:
    meters = input('Введи метраж квадратов карты: ')

    try:
        meters = int(meters)
        break

    except ValueError:
        print('\n ! Введите числовое значение\n')


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title(' ')
        self.iconbitmap('icon.ico')
        self.geometry('350x350')
        self.attributes('-topmost', 10)
        self.attributes('-alpha', 0.45)
        self.resizable(False,False)


    def show(self):
        frame = Frame(self, bd=2, relief=SUNKEN)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        canvas = Canvas(frame, bd=0, bg='gray')
        self.w = canvas
        canvas.grid(row=0, column=0, sticky=N+S+E+W)
        frame.pack(fill=BOTH, expand=1)

        canvas.bind('<ButtonPress-1>', self.first_touch)
        canvas.bind('<ButtonRelease-1>', self.second_touch)

        self.mainloop()


    def first_touch(self, event):
        self.x1 = event.x
        self.y1 = event.y

        try:
            self.w.delete(self.oval, self.line)

        except AttributeError:
            pass

        self.oval = self.w.create_oval(
            self.x1, self.y1,
            self.x1, self.y1,
            outline='lime',
            width=4
        )


    def second_touch(self, event):
        self.x2 = event.x
        self.y2 = event.y

        self.line = self.w.create_line(
            self.x1, self.y1,
            self.x2, self.y2,
            fill='lime',
            arrow='last'
        )

        self.title(int(sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2) / 45 * meters))

        

if __name__ == '__main__':
    Window().show()