from tkinter import *
from tkinter import messagebox
from tkintermapview import TkinterMapView


class MapGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('TMG')
        self.window.geometry('800x800')

        self.gmap_widget = TkinterMapView(self.window, width=750, height=600)
        self.gmap_widget.pack(fill='both')

        self.gmap_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                         max_zoom=22)  # google normal

        self.marker = self.gmap_widget.set_address("KFC 10421 South Western Avenue", marker=True)
        self.marker.set_text(text="My Favorite KFC")
        self.gmap_widget.set_zoom(12)

        self.window.mainloop()


if __name__ == "__main__":
    MapGUI()
