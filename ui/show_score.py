from tkinter import *
import window_setter as ws
from PIL import ImageTk, Image


class ShowScore:
    def __init__(self, score, time, nlps):
        self.score = score
        self.nlps = nlps
        self.time = time

    def create_frame(self):
        main_frame = Tk()
        main_frame.resizable(False, False)
        ws.FullScreenApp(main_frame)
        main_frame.state('zoomed')
        main_frame.config(bg='#2B2D42')

        left_frame = Frame(main_frame, bg="#2B2D42")
        banner = Image.open("../resources/Done.png")
        banner_tk = ImageTk.PhotoImage(banner)
        banner_image = Label(left_frame, image=banner_tk)
        banner_image["bg"] = "#2B2D42"
        banner_image["border"] = "0"
        banner_image.pack(side="left", anchor="s", padx=20)
        left_frame.grid(row=0, column=0, sticky="nsew")

        right_frame = Frame(main_frame, bg="#2B2D42")
        score_holder = Frame(right_frame, bg="#2B2D42")

        score_holder.grid(row=0, column=0, sticky="nsew")
        score_label = Label(score_holder, text="SCORE:", font=("Roboto", 20), fg="white", bg="#2B2D42")
        score_label.grid(row=0, column=0, sticky="nsew")

        right_frame.grid(row=0, column=1, sticky="nsew", pady=100)
        right_frame.columnconfigure(0, weight=1)

        main_frame.grid_columnconfigure(0, weight=0)
        main_frame.grid_columnconfigure(1, weight=3)

        main_frame.rowconfigure(0, weight=1)
        main_frame.mainloop()

