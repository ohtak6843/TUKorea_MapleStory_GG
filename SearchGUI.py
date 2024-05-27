from tkinter import *
from tkinter import font
from tkinter import messagebox

from MapleInfo import *


class SearchGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('TMG')
        self.window.geometry('800x600')

        self.fontstyle = font.Font(self.window, size=20, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')

        self.searchE = Entry(self.window, highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.searchE.place(x=150, y=20, width=300, height=30)
        self.searchB = Button(self.window, text="검색", width=12, height=1, font=self.fontstyle2,
                              command=self.pressedSearchB())
        self.searchB.place(x=450, y=20, height=30)

        self.window.mainloop()

    def pressedSearchB(self):
        pass


SearchGUI()
