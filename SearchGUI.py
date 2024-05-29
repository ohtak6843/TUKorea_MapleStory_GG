from tkinter import *
from tkinter import font
from tkinter import messagebox
import tkinter.ttk

from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk

from MapleInfo import *


class SearchGUI:
    xSize = 700
    ySize = 850

    def __init__(self):
        self.window = Tk()
        self.window.title('TMG')
        self.window.geometry(str(self.xSize) + 'x' + str(self.ySize))  # 화면 크기 지정

        # 폰트 스타일
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')

        # 검색창
        self.searchE = Entry(self.window, highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.searchE.place(x=150, y=20, width=300, height=30)
        self.searchB = Button(self.window, text="검색", width=12, height=1, font=self.fontstyle2,
                              command=self.pressedSearchB)
        self.searchB.place(x=450, y=20, height=30)

        # 이름 출력
        self.nameLabel = Label(self.window, text="이름: ", width=24, height=1, font=self.fontstyle2,
                               highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.nameLabel.place(x=10, y=120)

        # 레벨 출력
        self.levelLabel = Label(self.window, text="레벨: ", width=24, height=1, font=self.fontstyle2,
                                highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.levelLabel.place(x=10, y=160)

        # 서버 출력
        self.serverLabel = Label(self.window, text="서버: ", width=24, height=1, font=self.fontstyle2,
                                 highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.serverLabel.place(x=10, y=200)

        # 이미지 출력
        self.cImageLabel = Label(self.window, highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.cImageLabel.place(x=self.xSize - 170, y=100, width=160, height=160)

        self.createNoteBook()

        # 이메일 전송창
        self.searchE = Entry(self.window, highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.searchE.place(x=150, y=self.ySize - 50, width=300, height=30)
        self.searchB = Button(self.window, text="전송", width=12, height=1, font=self.fontstyle2,
                              command=self.pressedSendB)
        self.searchB.place(x=450, y=self.ySize - 50, height=30)

        self.window.mainloop()

    # 노트북 생성 함수
    def createNoteBook(self):
        # 노트북
        self.notebook = tkinter.ttk.Notebook(self.window, width=self.xSize - 20, height=int(self.ySize / 2) + 50)
        self.notebook.place(x=10, y=int(self.ySize / 2) - 100)

        # 첫번째 탭
        self.frame1 = Frame(self.window)
        self.notebook.add(self.frame1, text="스탯")

        # 두번째 탭
        self.frame2 = Frame(self.window)
        self.notebook.add(self.frame2, text="하이퍼스탯")

        # 세번째 탭
        self.frame3 = Frame(self.window)
        self.notebook.add(self.frame3, text="어빌리티")

        # 네번째 탭
        self.frame4 = Frame(self.window)
        self.notebook.add(self.frame4, text="성장치")

    def statInfo(self):
        # self.frame1
        self.labels = {}
        for s in self.mapleInfo.stat['final_stat']:
            self.labels[s['stat_name']] = Label(self.frame1, text=s['stat_name'] + " : " + str(s['stat_value']),
                                                width=33)

        i = 0
        j = 0
        for s, k in self.labels.items():
            k.grid(row=i, column=j)
            i += 1
            if i == 15:
                i = 0
                j += 1

    def hyperStatInfo(self):
        self.labels = {}
        for s in self.mapleInfo.hyperStat['hyper_stat_preset_1']:
            self.labels[s['stat_type']] = Label(self.frame2,
                                                text=s['stat_type'] + " : " + str(s['stat_level']) + "Lv   효과 : " + str(
                                                    s['stat_increase']))

        for s, k in self.labels.items():
            k.pack()

    def abilityInfo(self):
        self.labels = {}
        for s in self.mapleInfo.ability['ability_info']:
            self.labels[s['ability_value']] = Label(self.frame3, text=s['ability_value'])

        for s, k in self.labels.items():
            k.pack()

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
        image = ImageTk.PhotoImage(im, master=self.window)
        self.cImageLabel.configure(image=image)
        self.cImageLabel.image = image

        self.statInfo()
        self.hyperStatInfo()
        self.abilityInfo()
        return True

    def pressedSendB(self):
        pass


if __name__ == "__main__":
    SearchGUI()
