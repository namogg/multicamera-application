import tkinter as tk
from video_capture import VideoCapture
import tkinter.ttk as ttk 
from tkinter import font
import customtkinter as ctk 
from camera_viewer import MainFrame
from tkinter.ttk import *
from setting_bar import SettingBar
from config import *


ctk.set_default_color_theme("dark-blue")
class MulticamerasApp(ctk.CTk):
    def __init__(self,title = "Multicameras App",width = 1280, height = 720,main_width = 0.9,sources = 0, max_row = 2, max_columns = 3 ,*args, **kwargs):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.maxsize(width, width)
        
        self.width = width
        self.height = height
        self.create_theme()
        self.resizable(True, True)

        self.main = MainFrame(self,relx=(1-main_width), relwidth = main_width, max_columns= max_columns, max_row = max_row,sources=sources)
        self.setting_bar = SettingBar(self,relx = 0,relwidth = (1-main_width))
        
        self.mainloop()

    def create_theme(self): 
        self.tk.call("source", "Azure-ttk-theme/azure.tcl")
        self.tk.call("set_theme", "dark")



if __name__ == "__main__":

    # Thay đổi sources để chạy: (Camera id, IP, source)
    sources = [   
        (
            "Camera 1",
            "0,0,0,0",
            "data/yt5s.io-London Walk from Oxford Street to Carnaby Street.mp4",
        ),
        (
            "Camera 2",
            "0,0,0,0",
            "data/yt5s.io-London Walk from Oxford Street to Carnaby Street.mp4",
        ),
        (
            "Camera 3",
            "0,0,0,0",
            "data/yt5s.io-London Walk from Oxford Street to Carnaby Street.mp4",
        ),
        (
            "Camera 4",
            "0,0,0,0",
            "data/yt5s.io-London Walk from Oxford Street to Carnaby Street.mp4",
        ),
        (
            "Camera 5",
            "0,0,0,0",
            "data/yt5s.io-London Walk from Oxford Street to Carnaby Street.mp4",
        ),

    ]

    MulticamerasApp(sources = sources, width =APP_WIDTH, height = APP_HEIGHT)