from tkinter import *
import window_setter as ws
from PIL import ImageTk, Image
import os
import customtkinter
from utils import dash_board_model
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)
import matplotlib

matplotlib.use("TkAgg")
database = dash_board_model.DashBoardModel()
is_on = ''
buttons = []
buttons_holder = []
user_frame = []
cur_user = 0


def user_click(user):
    global cur_user

    user_frame[cur_user].pack_forget()
    user_frame[user].pack(side='top', fill=BOTH, expand=True)

    buttons[cur_user].configure(text_color='white')
    buttons_holder[cur_user].config(bg='#FE3F56')

    cur_user = user

    buttons[cur_user].configure(text_color='#FEE440')
    buttons_holder[cur_user].config(bg='#FEE440')


class DashBoard:
    def __init__(self):
        self.detailed_divider = None
        self.detailed_holder = None
        self.over_all_holder = None
        self.detailed = None
        self.over_all = None
        self.center_frame = None
        self.scrollable_frame = None
        self.right_frame = None
        self.scrollable_users = None
        self.main_frame = Tk()
        self.frequency = database.get_frequency()
        self.cnns = database.get_cnn()
        self.nlps = database.get_nlp()
        self.users = database.get_users()

    def create_frame(self):
        # self.main_frame.resizable(False, False)
        self.main_frame.config(bg='#2B2D42')
        ws.FullScreenApp(self.main_frame)
        self.main_frame.state('zoomed')

        # toolbar
        tool_bar = Frame(self.main_frame, width=0)
        tool_bar.config(bg="#EDF2F4")
        tool_bar.pack(fill=X, side="top")

        self.center_frame = Frame(self.main_frame, bg="#2B2D42")
        self.center_frame.pack(fill=BOTH, side="top", expand=True)

        # components of the toolbar
        path = Image.open("../resources/examotion.png")
        path = path.resize((200, 50), Image.LANCZOS)
        image = ImageTk.PhotoImage(path)
        logo = Label(tool_bar, image=image)
        logo.pack(side='left', padx=50, pady=10)

        # login for admin
        login_image = Image.open(os.path.abspath("../resources/logout.png"))
        login_image = login_image.resize((150, 50), Image.LANCZOS)
        login_tk = ImageTk.PhotoImage(login_image)
        login = Label(tool_bar, image=login_tk, cursor="hand2")
        login["bg"] = "#EDF2F4"
        login["border"] = "0"
        login.pack(side='right', padx=40, pady=10)

        # for sidebar
        side_bar = Frame(self.center_frame, bg="#8D99AE")
        side_bar.grid(row=0, column=0, sticky="nsew")

        self.over_all_holder = Frame(side_bar, bg="#2B2D42")
        self.over_all_holder.pack(side='top', fill=X, padx=(20, 0), pady=30)

        self.over_all_divider = Label(self.over_all_holder, text=" ", bg="#FEE440", font=("Arial", 1))
        self.over_all_divider.pack(side='left', fill=Y)

        self.over_all = Label(self.over_all_holder, text="Overall", fg="#FEE440", bg="#2B2D42", font=("Arial", 20), width=15, cursor='hand2')
        self.over_all.bind("<Button-1>", self.create_overall)
        self.over_all.pack(side='left', fill=X, expand=True, pady=10)

        self.detailed_holder = Frame(side_bar, bg="white")
        self.detailed_holder.pack(side='top', fill=X, padx=(20, 0), pady=(0, 30))
        self.scrollable_users = customtkinter.CTkScrollableFrame(side_bar, fg_color="#8D99AE")
        self.scrollable_users.pack(side='top', fill=BOTH, padx=(40, 0), pady=(0, 20))
        self.create_user()
        self.detailed_divider = Label(self.detailed_holder, text=" ", bg="#FE3F56", font=("Arial", 1))
        self.detailed_divider.pack(side='left', fill=Y)

        self.detailed = Label(self.detailed_holder, text="Detailed", fg="black", bg="white", font=("Arial", 20), cursor='hand2')
        self.detailed.bind("<Button-1>", self.detailed_click)
        self.detailed.pack(side='left', fill=X, expand=True, pady=10)

        self.create_overall(None)
        self.main_frame.mainloop()

    def create_overall(self, none):
        global is_on
        if is_on == 'Overall':
            return

        self.scrollable_users.pack_forget()
        self.over_all.config(fg="#FEE440", bg="#2B2D42")
        self.detailed.config(fg="black", bg="white")
        self.detailed_holder.config(bg="white")
        self.over_all_holder.config(bg="#2B2D42")
        self.over_all_divider.config(bg="#FEE440")
        self.detailed_divider.config(bg="#FE3F56")

        is_on = 'Overall'
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.center_frame, fg_color="#2B2D42")
        self.scrollable_frame.grid(row=0, column=1, sticky="nsew")

        self.right_frame = Frame(self.scrollable_frame, bg="#2B2D42", padx=20, pady=10)
        self.right_frame.pack(side='top', fill=BOTH, expand=True)

        # tabulation
        tabulation_holder = Frame(self.right_frame, bg="#2B2D42", height=20)
        tabulation_holder.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=20)

        tabulation_card_holder = customtkinter.CTkFrame(tabulation_holder, fg_color="#DC2F02", corner_radius=10,
                                                        height=20)
        tabulation_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

        # tabulation = Label(tabulation_card_holder, bg="white", height=20)
        # tabulation.pack(side='left', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

        y = self.frequency.keys()
        x = self.frequency.values()

        # create a figure
        figure = Figure(figsize=(1, 3), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, tabulation_card_holder)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(y, x)
        axes.set_title('Frequency of Correct Answer')
        axes.set_ylabel('Occurrence')

        figure_canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1, padx=(10, 0), pady=(0, 10))

        tabulation_label = Label(tabulation_holder, text="TABULATION", bg="#2B2D42", fg="white", font=("Arial", 25))
        tabulation_label.pack(side='top')

        # CNN results
        cnn_holder = Frame(self.right_frame, bg="#2B2D42", height=20)
        cnn_holder.grid(row=1, column=0, sticky="nsew", padx=(0, 20))

        cnn_card_holder = customtkinter.CTkFrame(cnn_holder, fg_color="#DC2F02", corner_radius=10, height=20)
        cnn_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

        # cnn = Label(cnn_card_holder, bg="white", height=20)
        # cnn.pack(side='left', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

        y_cnn = self.cnns.keys()
        x_cnn = self.cnns.values()

        # create a figure
        figure = Figure(figsize=(1, 4), dpi=65)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, cnn_card_holder)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(y_cnn, x_cnn)
        axes.set_title('Frequency of Emotion')

        figure_canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1, padx=(10, 0), pady=(0, 10))

        cnn_label = Label(cnn_holder, text="CNN", bg="#2B2D42", fg="white", font=("Arial", 25))
        cnn_label.pack(side='top')

        # nlp result
        nlp_holder = Frame(self.right_frame, bg="#2B2D42", height=20)
        nlp_holder.grid(row=1, column=1, sticky="nsew")

        nlp_card_holder = customtkinter.CTkFrame(nlp_holder, fg_color="#DC2F02", corner_radius=10, height=20)
        nlp_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

        # nlp = Label(nlp_card_holder, bg="white", height=20)
        # nlp.pack(side='left', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

        y_nlps = self.nlps.keys()
        x_nlps = self.nlps.values()

        # create a figure
        figure = Figure(figsize=(1, 3), dpi=65)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, nlp_card_holder)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(y_nlps, x_nlps)
        axes.set_title('Frequency of Emotion')

        figure_canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1, padx=(10, 0), pady=(0, 10))
        nlp_label = Label(nlp_holder, text="NLP", bg="#2B2D42", fg="white", font=("Arial", 25))
        nlp_label.pack(side='top')

        # combined cnn and nlp
        combine_holder = Frame(self.right_frame, bg="#2B2D42", height=20)
        combine_holder.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(20, 0))

        combine_card_holder = customtkinter.CTkFrame(combine_holder, fg_color="#DC2F02", corner_radius=10, height=20)
        combine_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

        combine = Label(combine_card_holder, bg="white", height=20)
        combine.pack(side='left', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

        combine_nlp = Label(combine_holder, text="COMBINATION", bg="#2B2D42", fg="white", font=("Arial", 25))
        combine_nlp.pack(side='top')

        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(1, weight=1)

        self.center_frame.grid_columnconfigure(0, weight=0)
        self.center_frame.grid_columnconfigure(1, weight=3)
        self.center_frame.grid_rowconfigure(0, weight=1)

    def create_user(self):
        global buttons
        global buttons_holder

        counter = 0
        for item in self.users:
            detailed_holder = Frame(self.scrollable_users, bg="#FE3F56")
            detailed_holder.pack(side='top', fill=X, pady=(0, 20))
            user = customtkinter.CTkButton(detailed_holder,
                                           text=f"{item['name']}",
                                           text_color="white",
                                           fg_color="#2B2D42",
                                           font=("Arial", 25),
                                           command=lambda name=counter: user_click(name))

            counter += 1
            buttons_holder.append(detailed_holder)
            buttons.append(user)
            user.pack(side='left', fill=X, expand=True, padx=(5, 0))

        buttons[cur_user].configure(text_color='#FEE440')
        buttons_holder[cur_user].config(bg='#FEE440')

    def detailed_click(self, none):
        global is_on
        global user_frame

        if is_on == 'Detailed':
            return
        is_on = 'Detailed'
        self.over_all.config(fg="black", bg="white")
        self.detailed.config(fg="#FEE440", bg="#2B2D42")
        self.detailed_holder.config(bg="#2B2D42")
        self.over_all_holder.config(bg="white")
        self.over_all_divider.config(bg="#FE3F56")
        self.detailed_divider.config(bg="#FEE440")

        # for the detailed
        self.right_frame.destroy()
        self.scrollable_users.pack(side='top', fill=BOTH, padx=(40, 0), pady=(0, 20))
        user_frame.clear()
        for item in self.users:
            right_frame = Frame(self.scrollable_frame, bg="#2B2D42", padx=20, pady=10)

            # score
            score_holder = Frame(right_frame, bg="#2B2D42")
            score_holder.grid(row=0, column=0, pady=(0, 40))

            score_label = Label(score_holder, text="SCORE:", bg="#2B2D42", fg="white", font=("Arial", 25))
            score_label.pack(side='top', anchor='w')

            score_card_holder = customtkinter.CTkFrame(score_holder, fg_color="#DC2F02", corner_radius=10, height=20)
            score_card_holder.pack(side='top', fill=BOTH, pady=10, expand=True)

            score = Label(score_card_holder, bg="white", text=f"{item['score']}/30", font=("Arial", 25), width=10, pady=10)

            score.pack(side='left', padx=(0, 10), fill=X, expand=True)

            # time
            time_holder = Frame(right_frame, bg="#2B2D42")
            time_holder.grid(row=0, column=1, pady=(0, 40))

            time_label = Label(time_holder, text="TIME:", bg="#2B2D42", fg="white", font=("Arial", 25))
            time_label.pack(side='top', anchor='w')

            time_card_holder = customtkinter.CTkFrame(time_holder, fg_color="#DC2F02", corner_radius=10, height=20)
            time_card_holder.pack(side='top', fill=BOTH, pady=10, expand=True)
            minutes = item['time'] // 60
            seconds = item['time'] % 60
            if seconds < 60:
                minutes = 0

            time_text = f"{minutes:02}:{seconds:02}"
            time = Label(time_card_holder, bg="white", text=time_text, font=("Arial", 25), width=10, pady=10)
            time.pack(side='left', padx=(0, 10), fill=X, expand=True)

            # CNN results
            cnn_holder = Frame(right_frame, bg="#2B2D42", height=20)
            cnn_holder.grid(row=1, column=0, sticky="nsew", padx=(0, 20))

            cnn_card_holder = customtkinter.CTkFrame(cnn_holder, fg_color="#DC2F02", corner_radius=10, height=20)
            cnn_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            # cnn = Label(cnn_card_holder, bg="white", height=20)
            # cnn.pack(side='left', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            y_cnn = self.cnns.keys()
            x_cnn = self.cnns.values()

            # create a figure
            figure = Figure(figsize=(1, 4), dpi=65)

            # create FigureCanvasTkAgg object
            figure_canvas = FigureCanvasTkAgg(figure, cnn_card_holder)

            # create axes
            axes = figure.add_subplot()

            # create the barchart
            axes.bar(y_cnn, x_cnn)
            axes.set_title('Frequency of Emotion')

            figure_canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1, padx=(10, 0), pady=(0, 10))

            cnn_label = Label(cnn_holder, text="CNN", bg="#2B2D42", fg="white", font=("Arial", 25))
            cnn_label.pack(side='top')

            # nlp result
            nlp_holder = Frame(right_frame, bg="#2B2D42", height=20)
            nlp_holder.grid(row=1, column=1, sticky="nsew")

            nlp_card_holder = customtkinter.CTkFrame(nlp_holder, fg_color="#DC2F02", corner_radius=10, height=20)
            nlp_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            # nlp = Label(nlp_card_holder, bg="white", height=20)
            # nlp.pack(side='left', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            y_nlps = self.nlps.keys()
            x_nlps = self.nlps.values()

            # create a figure
            figure = Figure(figsize=(1, 3), dpi=65)

            # create FigureCanvasTkAgg object
            figure_canvas = FigureCanvasTkAgg(figure, nlp_card_holder)

            # create axes
            axes = figure.add_subplot()

            # create the barchart
            axes.bar(y_nlps, x_nlps)
            axes.set_title('Frequency of Emotion')

            figure_canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1, padx=(10, 0), pady=(0, 10))
            nlp_label = Label(nlp_holder, text="NLP", bg="#2B2D42", fg="white", font=("Arial", 25))
            nlp_label.pack(side='top')

            # summary
            summary_holder = Frame(right_frame, bg="#2B2D42", height=20)
            summary_holder.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(20, 0))

            summary_card_holder = customtkinter.CTkFrame(summary_holder, fg_color="#DC2F02", corner_radius=10,
                                                         height=20)
            summary_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            summary = Frame(summary_card_holder, bg="white")
            summary.pack(side='left', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            # headers

            Label(summary, text="Question No.", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0, column=0,
                                                                                                        sticky='nsew')
            Label(summary, text="Answer", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0, column=1,
                                                                                                  sticky='nsew')
            Label(summary, text="Time", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0, column=2,
                                                                                                sticky='nsew')
            Label(summary, text="CNN", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0, column=3,
                                                                                               sticky='nsew')
            Label(summary, text="NLP", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0, column=4,
                                                                                               sticky='nsew')
            Label(summary, text="Verdict", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0, column=5,
                                                                                                   sticky='nsew')

            for i in range(3):
                Label(summary, text=i+1, font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i+1, column=0,
                                                                                                 sticky='nsew')
                Label(summary, text=item['answers'][i], font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i+1, column=1,
                                                                                                 sticky='nsew')
                Label(summary, text=item['times'][i], font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i+1, column=2,
                                                                                                  sticky='nsew')
                Label(summary, text=item['cnns'][i], font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i+1, column=3,
                                                                                                       sticky='nsew')
                Label(summary, text=item['nlps'][i], font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i+1, column=4,
                                                                                                       sticky='nsew')
                Label(summary, text="Hard", font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i+1, column=5,
                                                                                                    sticky='nsew')
            summary.columnconfigure(0, weight=1)
            summary.columnconfigure(1, weight=1)
            summary.columnconfigure(2, weight=1)
            summary.columnconfigure(3, weight=1)
            summary.columnconfigure(4, weight=1)
            summary.columnconfigure(5, weight=1)

            summary_label = Label(summary_holder, text="SUMMARY", bg="#2B2D42", fg="white", font=("Arial", 25))
            summary_label.pack(side='top')

            right_frame.grid_columnconfigure(0, weight=1)
            right_frame.grid_columnconfigure(1, weight=1)

            user_frame.append(right_frame)

        user_frame[cur_user].pack(side='top', fill=BOTH, expand=True)


DashBoard().create_frame()
