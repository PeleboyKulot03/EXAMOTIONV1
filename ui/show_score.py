from tkinter import *
import window_setter as ws
from PIL import ImageTk, Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import matplotlib

matplotlib.use("TkAgg")

matplotlib.rcParams['toolbar'] = 'None'


class ShowScore(Frame):
    def __init__(self, parent, controller, score=1, time=1, data=None):
        Frame.__init__(self, parent)
        self.controller = controller
        self.score = score
        self.time = time
        self.data = data
        self.config(bg='#2B2D42')

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

    def create_frame(self):
        left_frame = Frame(self, bg="#2B2D42")
        banner = Image.open("../resources/Done.png")
        banner_tk = ImageTk.PhotoImage(banner)
        banner_image = Label(left_frame, image=banner_tk)
        banner_image["bg"] = "#2B2D42"
        banner_image["border"] = "0"
        banner_image.pack(side="left", anchor="s", padx=20)
        banner_image.image = banner_tk

        left_frame.grid(row=0, column=0, sticky="nsew")

        right_frame = Frame(self, bg="#2B2D42", padx=30)

        # for timer and score
        upper_portion = Frame(right_frame, bg="#2B2D42", pady=40)
        upper_portion.pack(side='top', fill=X, anchor="n")

        score_holder = Frame(upper_portion, bg="#2B2D42")
        score_holder.pack(side='left', fill=X, anchor='n', expand=True)

        score_label = Label(score_holder, text="SCORE:", font=("Roboto", 20), fg="white", bg="#2B2D42")
        score_temp_holder = Frame(score_holder, bg="#2B2D42")
        divider = Label(score_temp_holder, text=" ", font=("Roboto", 20), fg="white", bg="#FE3F56")

        score_text = f"{self.score}/30"
        score = Label(score_temp_holder, text=score_text, font=("Roboto", 20), fg="black", bg="white", width=10)
        divider.pack(side="left")
        score.pack(side="left", expand=True, fill=X)

        score_label.grid(row=0, column=0, sticky="w")
        score_temp_holder.grid(row=1, column=0, sticky="nsew")

        timer_holder = Frame(upper_portion, bg="#2B2D42")
        timer_holder.pack(side='left', fill=X, anchor='n', expand=True)

        time_temp_holder = Frame(timer_holder, bg="#2B2D42")
        divider_time = Label(time_temp_holder, text=" ", font=("Roboto", 20), fg="white", bg="#FE3F56")

        minutes = self.time // 60
        seconds = self.time % 60
        if seconds < 60:
            minutes = 0

        time_text = f"{minutes:02}:{seconds:02}"
        time = Label(time_temp_holder, text=time_text, font=("Roboto", 20), fg="black", bg="white", width=10)
        divider_time.pack(side="left")
        time.pack(side="left", expand=True, fill=X)

        timer_label = Label(timer_holder, text="TIME:", font=("Roboto", 20), fg="white", bg="#2B2D42")
        timer_label.grid(row=0, column=0, sticky="w")
        time_temp_holder.grid(row=1, column=0, sticky="nsew")

        # for charts and back to homepage
        lower_portion = Frame(right_frame, bg="#2B2D42")
        lower_portion.pack(side='top', expand=True, anchor="n", fill=BOTH)

        chart_label = Label(lower_portion, text="CHART", font=("Roboto", 20), fg="white", bg="#2B2D42", pady=20)
        chart_label.pack(side='top', anchor='n', fill=X)
        chart_holder = Frame(lower_portion)

        languages = []
        popularity = []
        if self.data is not None:
            languages = self.data.keys()
            popularity = self.data.values()

        # create a figure
        figure = Figure(figsize=(1, 3), dpi=100)
        figure.canvas.header_visible = False
        figure.canvas.footer_visible = False
        figure.canvas.toolbar_visible = False

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, chart_holder)
        figure_canvas.header_visible = False
        figure_canvas.footer_visible = False
        figure_canvas.toolbar_visible = False

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, chart_label)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Emotions while taking the exam')
        axes.set_ylabel('Occurrence')

        figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        chart_holder.pack(side='top', anchor='n', expand=True, fill=X)

        chart_divider = Label(chart_holder, font=("Arial", 1), bg="#FAA307")
        chart_divider.pack(side='top', anchor='n', fill=X)

        button = Image.open("../resources/back_to_homepage.png")
        button = button.resize((400, 60), Image.LANCZOS)
        start_image_tk = ImageTk.PhotoImage(button)
        start_image = Label(lower_portion, image=start_image_tk, cursor="hand2", pady=20)
        start_image["bg"] = "#2B2D42"
        start_image["border"] = "0"
        start_image.pack(side='top', anchor='n', expand=True)
        start_image.image = start_image_tk
        start_image.bind('<Button-1>', self.goto_landing_page)

        right_frame.grid(row=0, column=1, sticky="nsew", pady=100)
        right_frame.columnconfigure(0, weight=1)

    def goto_landing_page(self, event=None):
        self.controller.show_frame("LandingPage")
