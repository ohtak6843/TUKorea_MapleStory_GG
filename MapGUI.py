import sys
import tkinter
import tkinter.messagebox
from tkintermapview import TkinterMapView

import requests


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

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.search_bar = tkinter.Entry(self, width=50)
        self.search_bar.grid(row=0, column=0, pady=10, padx=10, sticky="we")
        self.search_bar.focus()

        self.search_bar_button = tkinter.Button(master=self, width=8, text="Search", command=self.search)
        self.search_bar_button.grid(row=0, column=1, pady=10, padx=10)

        self.pc_room_list = tkinter.Listbox(self, width=20, height=500)
        self.pc_room_list.grid(row=1, column=3, pady=10, padx=10)

        self.map_widget = TkinterMapView(width=600, height=600, corner_radius=0)
        self.map_widget.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.map_widget.set_address("시흥시")

        self.marker_list = []
        self.search_marker = None
        self.search_in_progress = False

        self.getData()
        for pc_room in self.pc_rooms:
            self.pc_room_list.insert(tkinter.END, f"{pc_room["상호"]}")


        self.mainloop()

    def search(self, event=None):
        if not self.search_in_progress:
            self.search_in_progress = True
            if self.search_marker not in self.marker_list:
                self.map_widget.delete(self.search_marker)

            address = self.search_bar.get()
            self.search_marker = self.map_widget.set_address(address, marker=True)
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


if __name__ == "__main__":
    app = App()
