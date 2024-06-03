from tkinter import *
from tkinter import font
from tkinter import messagebox
import tkinter.ttk

from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from MapleInfo import *


class SearchGUI:
    xSize = 600
    ySize = 850
    characterInfo_size = (xSize, 250)
    bar_size = (xSize, 30)
    stat_size = (xSize, ySize - 250 - 30)

    def __init__(self):
        self.window = Tk()
        self.window.title('TMG')
        self.window.geometry(str(self.xSize) + 'x' + str(self.ySize))  # 화면 크기 지정

        self.characterInfo_print()
        self.bar_print()
        self.statUI_print()

        # 폰트 스타일
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')

        # 검색창
        self.searchE = Entry(self.window, highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.searchE.place(x=self.xSize//2 - 100 - 15, y=3, width=200, height=30)
        self.searchE.insert(0,"캐릭터 명 입력")
        self.searchB = Button(self.window, text="검색", width=12, height=1, font=self.fontstyle2,
                              command=self.pressedSearchB)
        self.searchB.place(x=self.xSize//2 + 100 - 15, y=3,width=100, height=30)


        """# 이메일 전송창
        self.mailSendE = Entry(self.window, highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.mailSendE.place(x=self.xSize//2 - 150 - 35, y=self.ySize - 35, width=300, height=30)
        self.mailSendE.insert(0,"이메일 주소 입력")
        self.mailSendB = Button(self.window, text="전송", width=12, height=1, font=self.fontstyle2,
                                command=self.pressedSendB)
        self.mailSendB.place(x=self.xSize//2 + 150 - 35, y=self.ySize - 35, width=100, height=30)"""



        self.window.mainloop()


    def characterInfo_print(self): # 캐릭창 배경 출력
        tempImage = Image.open("image/Character_info.png")
        tempImage = tempImage.resize((self.xSize, self.characterInfo_size[1]), Image.LANCZOS)
        titleImage = ImageTk.PhotoImage(tempImage, master=self.window)

        self.characterInfo_label = Label(self.window, image=titleImage, borderwidth=0)
        self.characterInfo_label.image=titleImage
        self.characterInfo_label.place(x=0, y=0)

    def bar_print(self): # 찾고자 하는 캐릭 정보를 선택하는 부분 배경 출력
        tempImage = Image.open("image/bar.png")
        tempImage = tempImage.resize((self.xSize, self.bar_size[1]), Image.LANCZOS)
        titleImage = ImageTk.PhotoImage(tempImage, master=self.window)
        self.bar_label = Label(self.window, image=titleImage, borderwidth=0)
        self.bar_label.image = titleImage
        y = self.characterInfo_size[1]
        self.bar_label.place(x=0, y=y)

    def statUI_print(self): # 캐릭터 정보 출력 배경
        tempImage = Image.open("image/stat_UI.png")
        tempImage = tempImage.resize((self.xSize, self.stat_size[1]), Image.LANCZOS)
        titleImage = ImageTk.PhotoImage(tempImage, master=self.window)

        self.statUI_label = Label(self.window, image=titleImage, borderwidth=0)
        self.statUI_label.image = titleImage
        y = self.characterInfo_size[1] + self.bar_size[1]
        self.statUI_label.place(x=0, y=y)

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

    def historyInfo(self):
        maxLevel = 300

        width = self.notebook['width']
        height = self.notebook['height']
        self.levelHistoryC.delete('graph')

        barWidth = 40

        # 1월 데이터
        nowLevel = MapleInfo(self.mapleInfo.basic['character_name'], '2024-01-01').basic['character_level']
        self.levelHistoryC.create_text(width // 2 - 200, height - 50, text='2024-01-01', tags='graph')
        self.levelHistoryC.create_text(width // 2 - 200, height - 20 - 0.9 * nowLevel * (height / maxLevel) - 10, text=nowLevel, tags='graph')
        self.levelHistoryC.create_rectangle(width // 2 - 200 - barWidth // 2, height - 20 - 0.9 * nowLevel * (height / maxLevel),
                                width // 2 - 200 + barWidth // 2, height - 60, tags='graph')

        # 2월 데이터
        nowLevel = MapleInfo(self.mapleInfo.basic['character_name'], '2024-02-01').basic['character_level']
        self.levelHistoryC.create_text(width // 2 - 100, height - 50, text='2024-02-01', tags='graph')
        self.levelHistoryC.create_text(width // 2 - 100, height - 20 - 0.9 * nowLevel * (height / maxLevel) - 10, text=nowLevel, tags='graph')
        self.levelHistoryC.create_rectangle(width // 2 - 100 - barWidth // 2, height - 20 - 0.9 * nowLevel * (height / maxLevel),
                                width // 2 - 100 + barWidth // 2, height - 60, tags='graph')

        # 3월 데이터
        nowLevel = MapleInfo(self.mapleInfo.basic['character_name'], '2024-03-01').basic['character_level']
        self.levelHistoryC.create_text(width // 2, height - 50, text='2024-03-01', tags='graph')
        self.levelHistoryC.create_text(width // 2, height - 20 - 0.9 * nowLevel * (height / maxLevel) - 10, text=nowLevel, tags='graph')
        self.levelHistoryC.create_rectangle(width // 2 - barWidth // 2, height - 20 - 0.9 * nowLevel * (height / maxLevel),
                                width // 2 + barWidth // 2, height - 60, tags='graph')

        # 4월 데이터
        nowLevel = MapleInfo(self.mapleInfo.basic['character_name'], '2024-04-01').basic['character_level']
        self.levelHistoryC.create_text(width // 2 + 100, height - 50, text='2024-04-01', tags='graph')
        self.levelHistoryC.create_text(width // 2 + 100, height - 20 - 0.9 * nowLevel * (height / maxLevel) - 10, text=nowLevel, tags='graph')
        self.levelHistoryC.create_rectangle(width // 2 + 100 - barWidth // 2, height - 20 - 0.9 * nowLevel * (height / maxLevel),
                                width // 2 + 100 + barWidth // 2, height - 60, tags='graph')

        # 5월 데이터
        nowLevel = MapleInfo(self.mapleInfo.basic['character_name'], '2024-05-01').basic['character_level']
        self.levelHistoryC.create_text(width // 2 + 200, height - 50, text='2024-05-01', tags='graph')
        self.levelHistoryC.create_text(width // 2 + 200, height - 20 - 0.9 * nowLevel * (height / maxLevel) - 10, text=nowLevel, tags='graph')
        self.levelHistoryC.create_rectangle(width // 2 + 200 - barWidth // 2, height - 20 - 0.9 * nowLevel * (height / maxLevel),
                                width // 2 + 200 + barWidth // 2, height - 60, tags='graph')

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
        self.historyInfo()
        return True

    def pressedSendB(self):
        to_email = self.mailSendE.get()
        if self.mapleInfo.ocid == None:
            messagebox.showinfo('ERROR', '캐릭터를 검색하세요')
            return
        if len(to_email) == 0:
            messagebox.showinfo('ERROR', '이메일을 입력하세요')
            return

        # 이메일 설정
        from_email = "ohtak6843@gmail.com"  # 보내는 이메일 주소
        password = "btlh gzhn xlrp ygya"  # 앱 비밀 번호

        # 보낼 내용
        body = ''
        for s in self.mapleInfo.stat['final_stat']:
            body += s['stat_name'] + " : " + str(s['stat_value']) + '\n'

        # 이메일 메시지 설정
        subject = "메이플 캐릭터 검색 결과"

        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        # SMTP 세션 설정 및 이메일 보내기
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(from_email, password)
            text = message.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            messagebox.showinfo("성공", "이메일이 성공적으로 전송되었습니다.")
        except smtplib.SMTPException as e:
            messagebox.showerror("오류", f"이메일을 보내는 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    SearchGUI()
