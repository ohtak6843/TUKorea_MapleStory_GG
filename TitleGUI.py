from tkinter import *
from tkinter import font
from PIL import ImageTk, Image


class TitleGUI:
    xSize = 800
    ySize = 600
    def __init__(self):
        self.window = Tk()
        self.window.title('TMG')
        self.window.geometry(str(self.xSize) + 'x' + str(self.ySize)) # 화면 크기 지정

        # 배경 이미지 로드 및 출력
        self.tempImage = Image.open("image/title_image.png")
        self.tempImage = self.tempImage.resize((self.xSize, self.ySize), Image.LANCZOS)
        self.titleImage = ImageTk.PhotoImage(self.tempImage)
        self.label = Label(self.window, image=self.titleImage)
        self.label.pack()

        # 폰트 스타일
        self.fontstyle = font.Font(self.window, size=16, weight='bold', family='Consolas')

        # 버튼
        self.BMain = Button(self.window, text="캐릭터 검색", width=12, height=1, font=self.fontstyle, command=self.pressedBMain)
        self.BMain.place(x=(self.xSize / 2) - 75, y=400)
        self.BMap = Button(self.window, text="PC방 찾기", width=12, height=1, font=self.fontstyle, command=self.pressedBMap)
        self.BMap.place(x=(self.xSize / 2) - 75, y=500)
        self.window.mainloop()

    def pressedBMain(self):
        pass

    def pressedBMap(self):
        pass


if __name__ == "__main__":
    TitleGUI()
