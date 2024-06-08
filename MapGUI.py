import sys
import tkinter
import tkinter.messagebox
from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim

import requests

from teller import *


class App(tkinter.Tk):
    APP_NAME = "map_view_demo.py"
    WIDTH = 800
    HEIGHT = 650

    # 공공데이터 API 키
    api_key = "PKGFCGC1GAJJBXm5h13NotLREkhRZqXdj3rBL7VIoq+cZa9ub4MXTnCiZNYRk9StuDZfvgMZ7oLn3BKVZV2OPg=="

    # 시흥시 PC방 현황
    url = "https://api.odcloud.kr/api/15104288/v1/uddi:1a1728ba-a31a-4b5c-a04f-aafc37f0b10e"
    params = {
        "serviceKey": api_key,
        "page": 1,
        "perPage": 1000,
        "returnType": "JSON"
    }
    response = requests.get(url, params=params)
    items = response.json()['data']

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title(self.APP_NAME)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Return>", self.search)

        if sys.platform == "darwin":
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=0)
        # self.grid_columnconfigure(2, weight=0)
        # self.grid_rowconfigure(1, weight=1)

        self.search_bar = tkinter.Entry(self, width=90)
        self.search_bar.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky="we")
        self.search_bar.focus()

        self.search_bar_button = tkinter.Button(master=self, width=8, text="Search", command=self.search)
        self.search_bar_button.grid(row=0, column=3, pady=10, padx=10)

        self.pc_room_list = tkinter.Listbox(self, width=20, height=33)
        self.pc_room_list.grid(row=1, rowspan=2, column=0, pady=10, padx=10)

        self.pc_room_select_button = tkinter.Button(self, text='select', width=20, height=1, command=self.list_select)
        self.pc_room_select_button.grid(row=3, column=0, pady=10, padx=10)

        self.map_widget = TkinterMapView(width=600, height=600, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=3, column=1, columnspan=3, sticky="nsew")

        self.map_widget.set_address("시흥시")

        self.marker_list = []
        self.search_marker = None
        self.search_in_progress = False

        self.pc_rooms_sub = []

        self.getData()
        for pc_room in self.pc_rooms:
            self.pc_room_list.insert(tkinter.END, f"{pc_room["상호"]}")
            self.pc_rooms_sub.append(pc_room)

        today = date.today()
        current_month = today.strftime('%Y%m')

        print('[', today, ']received token :', noti.TOKEN)

        self.bot = telepot.Bot(noti.TOKEN)
        pprint(self.bot.getMe())

        self.bot.message_loop(self.manage)

        print('Listening...')

        self.mainloop()

    def search(self, event=None):
        if not self.search_in_progress:
            self.search_in_progress = True
            if self.search_marker not in self.marker_list:
                self.map_widget.delete(self.search_marker)

            self.setList()
            if self.search_marker is False:
                # address was invalid (return value is False)
                self.search_marker = None
            self.search_in_progress = False

    def on_closing(self, event=0):
        self.destroy()
        exit()

    def getData(self):
        # pc방 데이터 받기
        self.pc_rooms = []
        for item in self.items:
            if item["업종명"] == None or item["업종명"] != "인터넷컴퓨터게임시설제공업":
                continue
            pc_room = {
                "업종명": item["업종명"],
                "등록(신고)번호": item["등록(신고)번호"],
                "등록(신고)일자": item["등록(신고)일자"],
                "상호": item['상호'],
                "영업소소재지(도로명)": item["영업소소재지(도로명)"],
                "영업소소재지(지번)": item["영업소소재지(지번)"]
            }
            self.pc_rooms.append(pc_room)

    def list_select(self):
        selection = self.pc_room_list.curselection()
        if len(selection) == 0:
            return False

        name = self.pc_room_list.get(selection[0])
        for pc_room in self.pc_rooms_sub:
            if pc_room["상호"] == name:
                tad = [i for i in pc_room["영업소소재지(도로명)"].split()]
                address = tad[1] + ' ' + tad[2] + ' ' + tad[3]
                address.replace(',', '')
                position = self.geocoding(address)
                overlayText = self.geocoding_reverse(str(position[0]) + ', ' + str(position[1]))
                self.search_marker = self.map_widget.set_position(position[0], position[1], marker=True,
                                                                  text=overlayText)
                self.map_widget.set_zoom(16)

                return True

    def setList(self):
        self.pc_room_list.delete(0, tkinter.END)
        self.pc_rooms_sub = []
        word = self.search_bar.get()
        if len(word) == 0:
            for pc_room in self.pc_rooms:
                self.pc_room_list.insert(tkinter.END, f"{pc_room["상호"]}")
                self.pc_rooms_sub.append(pc_room)

            return False

        for pc_room in self.pc_rooms:
            if word in pc_room["상호"] or word in pc_room["영업소소재지(도로명)"] or word in pc_room["영업소소재지(지번)"]:
                self.pc_room_list.insert(tkinter.END, f"{pc_room["상호"]}")
                self.pc_rooms_sub.append(pc_room)

        return True

    def geocoding(self, address):
        geo_local = Nominatim(user_agent='South Korea', timeout=None)
        try:
            geo = geo_local.geocode(address)
            x, y = [geo.latitude, geo.longitude]
            return x, y
        except:
            geo = geo_local.geocode('시흥시')
            x, y = [geo.latitude, geo.longitude]
            return x, y

    def geocoding_reverse(self, lat_lng_str):
        geo_local = Nominatim(user_agent='South Korea', timeout=None)
        address = geo_local.reverse(lat_lng_str)

        return address

    def manage(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
            return

        text = msg['text']
        args = text.split(' ')

        if text.startswith('상호'):
            self.reply(chat_id, text)
        elif text.startswith('주소'):
            self.reply(chat_id, text)
        else:
            noti.sendMessage(chat_id, '모르는 명령어입니다.\n상호 [상호명], 주소 [도로명주소 or 지번주소] 중 하나의 명령을 입력하세요.')

    def reply(self, user, command):
        data = command[3:]
        msg = ''
        idx = 1
        for pc_room in self.pc_rooms:
            if data in pc_room["상호"] or data in pc_room["영업소소재지(도로명)"] or data in pc_room["영업소소재지(지번)"]:
                r = str(idx) + '. ' + pc_room["상호"] + ' / ' + pc_room["영업소소재지(도로명)"]
                idx += 1
                if len(r + msg) + 1 > noti.MAX_MSG_LENGTH:
                    noti.sendMessage(user, msg)
                    msg = r + '\n'
                else:
                    msg += r + '\n'

        if msg:
            noti.sendMessage(user, msg)
        else:
            noti.sendMessage(user, "데이터가 없습니다.")


if __name__ == "__main__":
    app = App()
