from tkinter import *
from tkinter import font
from tkinter import messagebox

from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk

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
                              command=self.pressedSearchB)
        self.searchB.place(x=450, y=20, height=30)

        self.nameLabel = Label(self.window, text="이름: ", width=24, height=1, font=self.fontstyle2,
                               highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.nameLabel.place(x=10, y=120)
        self.levelLabel = Label(self.window, text="레벨: ", width=24, height=1, font=self.fontstyle2,
                                highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.levelLabel.place(x=10, y=160)
        self.serverLabel = Label(self.window, text="서버: ", width=24, height=1, font=self.fontstyle2,
                                 highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.serverLabel.place(x=10, y=200)
        self.cImageLabel = Label(self.window, highlightcolor='black', highlightbackground='black',
                                 highlightthickness=2)
        self.cImageLabel.place(x=500, y=100, width=160, height=160)

        self.window.mainloop()

    def pressedSearchB(self):
        self.mapleInfo = MapleInfo(self.searchE.get())
        if self.mapleInfo.ocid == None:
            messagebox.showinfo('ERROR', '존재하는 캐릭터가 없습니다.')
            return False
        self.nameLabel.configure(text="이름: " + self.mapleInfo.name)
        self.levelLabel.configure(text="레벨: " + str(self.mapleInfo.basic['character_level']))
        self.serverLabel.configure(text="서버: " + self.mapleInfo.basic['world_name'])
        url = self.mapleInfo.basic['character_image']
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        self.cImageLabel.configure(image=image)

        return True


if __name__ == "__main__":
    SearchGUI()
