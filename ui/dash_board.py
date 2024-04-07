from tkinter import *
from PIL import ImageTk, Image
import os
import customtkinter
from statics import globals
from utils import dash_board_model
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)
import matplotlib

matplotlib.use("TkAgg")
global_var = globals.Globals()
is_on = ''
buttons = []
buttons_holder = []
user_frame = []
cur_user = 0
is_first = True


def user_click(user):
    global cur_user
    user_frame[cur_user].pack_forget()
    user_frame[user].pack(side='top', fill=BOTH, expand=True)

    buttons[cur_user].configure(text_color='white')
    buttons_holder[cur_user].config(bg='#FE3F56')

    cur_user = user

    buttons[cur_user].configure(text_color='#FEE440')
    buttons_holder[cur_user].config(bg='#FEE440')


def get_verdict(time, cnn, nlp):
    if time < 10:
        if cnn == "Neutral" and nlp == "Neutral" or cnn == "Excited" and nlp == "Excited":
            return "Very Easy"
        if cnn == "Bored" and nlp == "Bored":
            return "Easy"
        if cnn == "Nervous" and nlp == "Nervous":
            return "Hard"
        if cnn == "Frustrated" and nlp == "Frustrated":
            return "Very Hard"
        if cnn == "Surprised" and nlp == "Surprised":
            return "Very Hard"
        else:
            return "Undetermined"

    elif time < 60:
        if cnn == "Neutral" and nlp == "Neutral":
            return "Easy"
        if cnn == "Excited" and nlp == "Excited":
            return "Balanced"
        if cnn == "Bored" and nlp == "Bored":
            return "Hard"
        if cnn == "Nervous" and nlp == "Nervous":
            return "Balanced"
        if cnn == "Frustrated" and nlp == "Frustrated":
            return "Hard"
        if cnn == "Surprised" and nlp == "Surprised":
            return "Balanced"

        else:
            return "Undetermined"

    elif time < 300:
        if cnn == "Neutral" and nlp == "Neutral":
            return "Balanced"
        if cnn == "Excited" and nlp == "Excited":
            return "Easy"
        if cnn == "Bored" and nlp == "Bored":
            return "Hard"
        if cnn == "Nervous" and nlp == "Nervous":
            return "Balanced"
        if cnn == "Frustrated" and nlp == "Frustrated":
            return "Very Hard"
        if cnn == "Surprised" and nlp == "Surprised":
            return "Balanced"

        else:
            return "Undetermined"

    elif time >= 300:
        if cnn == "Neutral" and nlp == "Neutral":
            return "Balanced"
        if cnn == "Excited" and nlp == "Excited":
            return "Easy"
        if cnn == "Bored" and nlp == "Bored":
            return "Very Hard"
        if cnn == "Nervous" and nlp == "Nervous":
            return "Hard"
        if cnn == "Frustrated" and nlp == "Frustrated":
            return "Very Hard"
        if cnn == "Surprised" and nlp == "Surprised":
            return "Balanced"

        else:
            return "Undetermined"


class DashBoard(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        database = dash_board_model.DashBoardModel()
        self.right_frame = None
        self.scrollable_frame = None
        self.frequency = database.get_frequency()
        self.cnns = database.get_cnn()
        self.nlps = database.get_nlp()
        self.users = database.get_users()

        # toolbar
        tool_bar = Frame(self, width=0)
        tool_bar.config(bg="#EDF2F4")
        tool_bar.pack(fill=X, side="top")

        self.center_frame = Frame(self, bg="#2B2D42")
        self.center_frame.pack(fill=BOTH, side="top", expand=True)

        # components of the toolbar
        path = Image.open("../resources/back.png")
        path = path.resize((50, 50), Image.LANCZOS)
        image = ImageTk.PhotoImage(path)
        logo = Label(tool_bar, image=image, cursor='hand2')
        logo.pack(side='left', padx=50, pady=10)
        logo.bind('<Button-1>', lambda e: controller.show_frame("LandingPage"))
        logo.image = image

        # login for admin
        logout_image = Image.open(os.path.abspath("../resources/dash_board_text.png"))
        logout_tk = ImageTk.PhotoImage(logout_image)
        logout = Label(tool_bar, image=logout_tk)
        logout["bg"] = "#EDF2F4"
        logout["border"] = "0"
        logout.pack(side='right', padx=40, pady=10, fill=X, expand=True)
        logout.image = logout_tk

        # for sidebar
        side_bar = Frame(self.center_frame, bg="#8D99AE")
        side_bar.grid(row=0, column=0, sticky="nsew")

        self.over_all_holder = Frame(side_bar, bg="#2B2D42")
        self.over_all_holder.pack(side='top', fill=X, padx=(20, 0), pady=30)

        self.over_all_divider = Label(self.over_all_holder, text=" ", bg="#FEE440", font=("Arial", 1))
        self.over_all_divider.pack(side='left', fill=Y)

        self.over_all = Label(self.over_all_holder, text="Overall", fg="#FEE440", bg="#2B2D42", font=("Arial", 20),
                              width=15, cursor='hand2')
        self.over_all.bind("<Button-1>", self.create_overall)
        self.over_all.pack(side='left', fill=X, expand=True, pady=10)

        self.detailed_holder = Frame(side_bar, bg="white")
        self.detailed_holder.pack(side='top', fill=X, padx=(20, 0), pady=(0, 30))
        self.scrollable_users = customtkinter.CTkScrollableFrame(side_bar, fg_color="#8D99AE")
        self.scrollable_users.pack(side='top', fill=BOTH, padx=(40, 0), pady=(0, 20), expand=True)
        self.detailed_divider = Label(self.detailed_holder, text=" ", bg="#FE3F56", font=("Arial", 1))
        self.detailed_divider.pack(side='left', fill=Y)

        self.detailed = Label(self.detailed_holder, text="Detailed", fg="black", bg="white", font=("Arial", 20),
                              cursor='hand2')
        self.detailed.bind("<Button-1>", self.detailed_click)
        self.detailed.pack(side='left', fill=X, expand=True, pady=10)

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

        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(1, weight=1)

        self.center_frame.grid_columnconfigure(0, weight=0)
        self.center_frame.grid_columnconfigure(1, weight=3)
        self.center_frame.grid_rowconfigure(0, weight=1)

    def create_user(self):
        global buttons
        global buttons_holder

        counter = 0
        buttons.clear()
        buttons_holder.clear()
        for item in self.users:
            print(item)
            detailed_holder = Frame(self.scrollable_users, bg="#FE3F56")
            detailed_holder.pack(side='top', fill=X, pady=(0, 20))
            user = customtkinter.CTkButton(detailed_holder,
                                           text=f"{item['name']}",
                                           text_color="white",
                                           fg_color="#2B2D42",
                                           font=("Arial", 25),
                                           command=lambda name=counter: user_click(name))
            user._text_label.configure(wraplength=200)
            counter += 1
            buttons_holder.append(detailed_holder)
            buttons.append(user)
            user.pack(side='left', fill=X, expand=True, padx=(5, 0))

        if len(buttons) > 0:
            buttons[cur_user].configure(text_color='#FEE440')
            buttons_holder[cur_user].config(bg='#FEE440')

    def detailed_click(self, none):
        global is_on
        global user_frame

        # if is_first:
        #     users = database.get_users()
        #     self.create_user()
        #     is_first = False

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
        self.scrollable_users.pack(side='top', fill=BOTH, padx=(40, 0), pady=(0, 20), expand=True)
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

            score = Label(score_card_holder, bg="white", text=f"{item['score']}/30", font=("Arial", 25), width=10,
                          pady=10)

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
            if item['time'] < 60:
                minutes = 0

            time_text = f"{minutes:02}:{seconds:02}"
            time = Label(time_card_holder, bg="white", text=time_text, font=("Arial", 25), width=10, pady=10)
            time.pack(side='left', padx=(0, 10), fill=X, expand=True)

            data = {
                'Bored': 0,
                'Frustrated': 0,
                'Excited': 0,
                'Neutral': 0,
                'Nervous': 0,
                'Surprised': 0,
            }

            for emotion in item['cnns']:
                if not emotion == "No Emotion":
                    data[emotion] = data[emotion] + 1

            # CNN results
            cnn_holder = Frame(right_frame, bg="#2B2D42", height=20)
            cnn_holder.grid(row=1, column=0, sticky="nsew", padx=(0, 20))

            cnn_card_holder = customtkinter.CTkFrame(cnn_holder, fg_color="#DC2F02", corner_radius=10, height=20)
            cnn_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            y_cnn = data.keys()
            x_cnn = data.values()

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

            data = {
                'Bored': 0,
                'Frustrated': 0,
                'Excited': 0,
                'Neutral': 0,
                'Nervous': 0,
                'Surprised': 0,
            }

            for emotion in item['nlps']:
                if not emotion == "No Emotion":
                    data[emotion] = data[emotion] + 1

            y_nlps = data.keys()
            x_nlps = data.values()

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

            # pre survey
            pre_survey_holder = Frame(right_frame, bg="#2B2D42", height=20)
            pre_survey_holder.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(20, 0))

            pre_survey_label = Label(pre_survey_holder, text="Pre-Survey", bg="#2B2D42", fg="white", font=("Arial", 25))
            pre_survey_label.pack(side='top', pady=10)

            pre_survey_card_holder = customtkinter.CTkFrame(pre_survey_holder, fg_color="#DC2F02", corner_radius=10,
                                                            height=20)
            pre_survey_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            pre_survey = Frame(pre_survey_card_holder, bg="white")
            pre_survey.pack(side='left', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            # headers
            Label(pre_survey, text="Question No.", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0,
                                                                                                           column=0,
                                                                                                           sticky='nsew')
            Label(pre_survey, text="Answer", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0, column=1,
                                                                                                     sticky='nsew')
            Label(pre_survey, text="Translation", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0,
                                                                                                          column=2,
                                                                                                          sticky='nsew')

            for i in range(9):
                Label(pre_survey, text=i + 1, font=("Arial", 18), wraplength=300, borderwidth=1, relief="solid").grid(
                    row=i + 1,
                    column=0,
                    sticky='nsew')
                Label(pre_survey, text=item['pre_surveys'][i], wraplength=300, font=("Arial", 18), borderwidth=1,
                      relief="solid").grid(
                    row=i + 1, column=1,
                    sticky='nsew')
                Label(pre_survey, text=item['pre_survey_translation'][i], wraplength=300, font=("Arial", 18),
                      borderwidth=1,
                      relief="solid").grid(
                    row=i + 1, column=2,
                    sticky='nsew')



            pre_survey.columnconfigure(0, weight=1)
            pre_survey.columnconfigure(1, weight=1)
            pre_survey.rowconfigure(0, weight=1)
            pre_survey.rowconfigure(2, weight=1)

            # summary
            summary_holder = Frame(right_frame, bg="#2B2D42", height=20)
            summary_holder.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(20, 0))

            summary_label = Label(summary_holder, text="SUMMARY", bg="#2B2D42", fg="white", font=("Arial", 25))
            summary_label.pack(side='top', pady=10)

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
            Label(summary, text="Remarks", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0, column=4,
                                                                                                   sticky='nsew')

            for i in range(30):
                Label(summary, text=i + 1, font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i + 1, column=0,
                                                                                                   sticky='nsew')
                Label(summary, text=item['answers'][i], font=("Arial", 18), borderwidth=1, relief="solid").grid(
                    row=i + 1, column=1,
                    sticky='nsew')
                Label(summary, text=item['times'][i], font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i + 1,
                                                                                                              column=2,
                                                                                                              sticky='nsew')
                # Label(summary, text=item['cnns'][i], font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i + 1,
                #                                                                                              column=3,
                #                                                                                              sticky='nsew')

                # verdict = get_verdict(item['times'][i], item['cnns'][i], item['nlps'][i])
                #
                # Label(summary, text=verdict, font=("Arial", 18), borderwidth=1, relief="solid").grid(row=i + 1,
                #                                                                                      column=4,
                #                                                                                      sticky='nsew')
            summary.columnconfigure(0, weight=1)
            summary.columnconfigure(1, weight=1)
            summary.columnconfigure(2, weight=1)
            summary.columnconfigure(3, weight=1)
            summary.columnconfigure(4, weight=1)

            # post survey
            post_survey_holder = Frame(right_frame, bg="#2B2D42", height=20)
            post_survey_holder.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=(20, 0))

            post_survey_label = Label(post_survey_holder, text="Post-Survey", bg="#2B2D42", fg="white",
                                      font=("Arial", 25))
            post_survey_label.pack(side='top', pady=10)

            post_survey_card_holder = customtkinter.CTkFrame(post_survey_holder, fg_color="#DC2F02", corner_radius=10,
                                                             height=20)
            post_survey_card_holder.pack(side='top', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            post_survey = Frame(post_survey_card_holder, bg="white")
            post_survey.pack(side='left', fill=BOTH, padx=(10, 0), pady=(0, 10), expand=True)

            # headers
            Label(post_survey, text="Answer", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0, column=0,
                                                                                                      sticky='nsew')
            Label(post_survey, text="Translation", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0,
                                                                                                           column=1,
                                                                                                           sticky='nsew')
            Label(post_survey, text="Emotion", font=("Arial", 20), borderwidth=1, relief="solid").grid(row=0,
                                                                                                           column=2,
                                                                                                           sticky='nsew')

            # answers
            Label(post_survey, text=item['post_surveys'][0], wraplength=300, font=("Arial", 18), borderwidth=1,
                  relief="solid").grid(
                row=1, column=0,
                sticky='nsew')
            Label(post_survey, text=item['translations'][0], wraplength=300, font=("Arial", 18), borderwidth=1,
                  relief="solid").grid(
                row=1, column=1,
                sticky='nsew')
            Label(post_survey, text=item['nlps'][0], wraplength=300, font=("Arial", 18), borderwidth=1,
                  relief="solid").grid(
                row=1, column=2,
                sticky='nsew')

            post_survey.columnconfigure(0, weight=1)
            post_survey.columnconfigure(1, weight=1)
            post_survey.columnconfigure(2, weight=1)
            post_survey.rowconfigure(0, weight=1)
            post_survey.rowconfigure(1, weight=1)
            post_survey.rowconfigure(2, weight=1)

            right_frame.grid_columnconfigure(0, weight=1)
            right_frame.grid_columnconfigure(1, weight=1)

            user_frame.append(right_frame)

        if len(user_frame) > 0:
            user_frame[cur_user].pack(side='top', fill=BOTH, expand=True)