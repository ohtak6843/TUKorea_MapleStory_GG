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
    hyperStat_size = (xSize // 2, ySize - 250)
    ability_size = (xSize // 2, 250)
    hyperStatlist = ['STR', 'DEX', 'INT', 'LUK', 'HP', 'MP', 'DF/TF/PP', '크리티컬 확률', '크리티컬 데미지', '방어율 무시',
                     '데미지', '보스 몬스터 공격 시 데미지 증가', '일반 몬스터 공격 시 데미지 증가', '상태 이상 내성', '공격력/마력', '획득 경험치', '아케인포스']

    def __init__(self):
        self.window = Tk()
        self.window.title('TMG')
        self.window.geometry(str(self.xSize) + 'x' + str(self.ySize))  # 화면 크기 지정
        self.windowsSize_toogle = [False, False] #0번은 하이퍼, 1번은 어빌창이 켜져있는지 확인
        self.mapleInfo = None # 초기화

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



        cImageLabel_bg = Label(self.characterInfo_frame, bg="#c9ced0", width=30, height=11)
        cImageLabel_bg.place(x=195, y=37)

        self.bar_button()

        """# 이메일 전송창
        self.mailSendE = Entry(self.window, highlightcolor='black', highlightbackground='black', highlightthickness=2)
        self.mailSendE.place(x=self.xSize//2 - 150 - 35, y=self.ySize - 35, width=300, height=30)
        self.mailSendE.insert(0,"이메일 주소 입력")
        self.mailSendB = Button(self.window, text="전송", width=12, height=1, font=self.fontstyle2,
                                command=self.pressedSendB)
        self.mailSendB.place(x=self.xSize//2 + 150 - 35, y=self.ySize - 35, width=100, height=30)"""


        # self.characterInfoSearch() # 테스트 출력
        self.window.mainloop()


    def characterInfo_print(self): # 캐릭창 배경 출력
        # 프레임 설정
        self.characterInfo_frame = Frame(self.window, width=self.characterInfo_size[0], height=self.characterInfo_size[1])
        self.characterInfo_frame.place(x=0, y=0)

        # 이미지 설정
        tempImage = Image.open("image/Character_info.png")
        tempImage = tempImage.resize((self.characterInfo_size[0], self.characterInfo_size[1]), Image.LANCZOS)
        mainImage = ImageTk.PhotoImage(tempImage, master=self.characterInfo_frame)
        self.characterInfo_label = Label(self.characterInfo_frame, image=mainImage, borderwidth=0)
        self.characterInfo_label.image=mainImage
        self.characterInfo_label.place(x=0, y=0)

    def characterInfoSearch(self): # 검색한 캐릭터 정보 출력
        if self.mapleInfo == None:
            return

        # 직업 리벨
        self.classLabel = Label(self.characterInfo_frame, text=str(self.mapleInfo.basic["character_class"]), bg='#9aa2ab', width=15)
        self.classLabel.place(x=40, y=43)

        # 유니온
        self.unionLabel = Label(self.characterInfo_frame, text=str(self.mapleInfo.union["union_level"]), bg='#c9ced0', width=5)
        self.unionLabel.place(x=115, y=135)

        # 무릉도장
        self.Mu_Lung_Dojo = Label(self.characterInfo_frame, text=str(self.mapleInfo.Mu_Lung_Dojo["dojang_best_floor"]), bg='#c9ced0', width=5)
        self.Mu_Lung_Dojo.place(x=115, y=158)

        # 인기도
        self.unionLabel = Label(self.characterInfo_frame, text=str(self.mapleInfo.popularity["popularity"]), bg='#c9ced0', width=5)
        self.unionLabel.place(x=115, y=183)


        # 길드
        self.guildLabel = Label(self.characterInfo_frame, text=str(self.mapleInfo.basic["character_guild_name"]), bg='#c9ced0', width=10)
        self.guildLabel.place(x=493  , y=182)

        # 이미지 출력
        self.cImageLabel = Label(self.characterInfo_frame, bg="#c9ced0")
        self.cImageLabel.place(x=255, y=65)

        # 이름 출력
        self.nameLabel = Label(self.characterInfo_frame, bg="#9aa2ab", text=str(self.mapleInfo.name), width=15)
        self.nameLabel.place(x=245, y=170)

        url = self.mapleInfo.basic['character_image']
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im, master=self.window)
        self.cImageLabel.configure(image=image)
        self.cImageLabel.image = image

    def bar_print(self): # 찾고자 하는 캐릭 정보를 선택하는 부분 배경 출력
        # 프레임 설정
        y = self.characterInfo_size[1]
        self.bar_frame = Frame(self.window, width=self.bar_size[0], height=self.bar_size[1])
        self.bar_frame.place(x=0, y=y)
        
        # 이미지 레이블 출력
        tempImage = Image.open("image/bar.png")
        tempImage = tempImage.resize((self.bar_size[0], self.bar_size[1]), Image.LANCZOS)
        mainImage = ImageTk.PhotoImage(tempImage, master=self.bar_frame)
        self.bar_label = Label(self.bar_frame, image=mainImage, borderwidth=0)
        self.bar_label.image = mainImage
        self.bar_label.place(x=0, y=0)

    def bar_button(self):
        bStat = Button(self.bar_frame, text="하이퍼 스탯", command=self.hyperStat_print)
        bStat.place(x=18, y=5)

        bHStat = Button(self.bar_frame, text="어빌리티", command=self.ability_UI_print)
        bHStat.place(x=100, y=5)

    def statUI_print(self): # 캐릭터 정보 출력 배경
        # 프레임 설정
        y = self.characterInfo_size[1] + self.bar_size[1]
        self.statUI_frame = Frame(self.window, width=self.stat_size[0], height=self.stat_size[1])
        self.statUI_frame.place(x=0, y=y)


        # 이미지 출력
        tempImage = Image.open("image/stat_UI.png")
        tempImage = tempImage.resize((self.stat_size[0], self.stat_size[1]), Image.LANCZOS)
        mainImage = ImageTk.PhotoImage(tempImage, master=self.window)

        self.statUI_label = Label(self.statUI_frame, image=mainImage, borderwidth=0)
        self.statUI_label.image = mainImage
        self.statUI_label.place(x=0, y=0)

    def winResize(self): # 하이퍼 스탯이나 어빌리티 창이 켜져있는지 안켜져있는지 확인 후에 윈도우 크기를 설정한다.
        if True in self.windowsSize_toogle:
            self.window.geometry(str(self.xSize+self.hyperStat_size[0]) + 'x' + str(self.ySize))
            return

        self.window.geometry(str(self.xSize) + 'x' + str(self.ySize))

    def hyperStat_print(self):
        self.windowsSize_toogle[0] = not self.windowsSize_toogle[0]
        self.winResize()

        y = self.characterInfo_size[1]
        self.hyperstatUI_frame = Frame(self.window, width=self.hyperStat_size[0], height=self.hyperStat_size[1])
        self.hyperstatUI_frame.place(x=self.stat_size[0], y=y)

        # 하이퍼 스탯
        if self.windowsSize_toogle[0]:
            tempImage = Image.open("image/hyper_stat_Ui.png")
            tempImage = tempImage.resize((self.hyperStat_size[0], self.hyperStat_size[1]), Image.LANCZOS)
            mainImage = ImageTk.PhotoImage(tempImage, master=self.hyperstatUI_frame)

            self.hyperstatUI_label = Label(self.hyperstatUI_frame, image=mainImage, borderwidth=0)
            self.hyperstatUI_label.image = mainImage
            self.hyperstatUI_label.place(x=0, y=0)

            self.hyperStatInfo()

    def ability_UI_print(self):
        self.windowsSize_toogle[1] = not self.windowsSize_toogle[1]
        self.winResize()

        self.abilityUI_frame = Frame(self.window, width=self.ability_size[0], height=self.ability_size[1])
        self.abilityUI_frame.place(x=self.stat_size[0], y=0)

        # 하이퍼 스탯
        if self.windowsSize_toogle[1]:
            tempImage = Image.open("image/Ability_UI.png")
            tempImage = tempImage.resize((self.ability_size[0], self.ability_size[1]), Image.LANCZOS)
            mainImage = ImageTk.PhotoImage(tempImage, master=self.abilityUI_frame)

            self.abilityUI_label = Label(self.abilityUI_frame, image=mainImage, borderwidth=0)
            self.abilityUI_label.image = mainImage
            self.abilityUI_label.place(x=0, y=0)

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
        if self.mapleInfo == None: # 검색된 캐릭터가 없다면 출력을 하지 않는다.
            return
        if self.windowsSize_toogle[0] == False: # 하이퍼 스탯창이 꺼져있다면 출력을 하지 않는다.
            return

        self.labels = {}
        for s in self.mapleInfo.hyperStat['hyper_stat_preset_1']:
            self.labels[s['stat_type']] = s['stat_level']

        for i, type in enumerate(self.hyperStatlist):
            t = Label(self.hyperstatUI_frame, text=str(self.labels[type]), bg="#86939f", fg="#c8d6dc", font=('',13))
            t.place(x=250, y=55+ (31 * i))



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
            self.mapleInfo = None
            messagebox.showinfo('ERROR', '존재하는 캐릭터가 없습니다.')
            return False

        self.characterInfoSearch()
        self.hyperStatInfo()
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
