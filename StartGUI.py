from tkinter import *
from tkinter import font
from tkinter import messagebox


class StartGUI():
    def __init__(self):
        self.window = Tk()
        self.window.title('TMG')
        self.window.geometry('800x600')

        self.fontstyle = font.Font(self.window, size=20, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')

        self.titleLabel = Label(self.window, text="TUKorea Maplestory GG", width=24, height=1, font=self.fontstyle,
                                bg="green", fg="cyan")
        self.titleLabel.place(x=200, y=100)

        self.BMain = Button(self.window, text="캐릭터 검색", width=12, height=1, font=self.fontstyle2,
                            command=self.pressedBMain)
        self.BMain.place(x=300, y=400)
        self.BMap = Button(self.window, text="PC방 찾기", width=12, height=1, font=self.fontstyle2,
                           command=self.pressedBMap)
        self.BMap.place(x=300, y=500)

        self.window.mainloop()

    def pressedBMain(self):
        pass

    def pressedBMap(self):
        pass
