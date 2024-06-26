from tkinter import *
from tkinter import messagebox
import numpy as np
from statics import static
import threading
from time import sleep
import customtkinter
from PIL import Image, ImageTk
import cv2
from deepface import DeepFace
from utils import exam_page_model
import os
import pathlib
from transformers import pipeline
import random as rand
from googletrans import Translator
import random

classifier = pipeline("text-classification", model='bhadresh-savani/bert-base-uncased-emotion', return_all_scores=False)
translator = Translator()

on_pre = True
from_pre = True
is_first = True
on_post = False
pre_survey_part = 0
question_counter = 0
cur_answer = 5
pre_q_and_a_holder = []
q_and_a_holder = []
nlps = []
post_surveys = []
translations = []
pre_shuffled_question_index = []
shuffled_question_index = []

pre_answers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
answers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
           5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
           5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

pre_emotions = []
emotions = []
pre_answer_holder = []
answers_holder = []
pre_survey_answer = {}
static_answers = ['Not Confident at all', 'Slightly Confident', 'Moderately Confident', 'Very Confident',
                  'Extremely Confident']
pre_times = []
times = []
score = 0
pre_score = 0
cap = cv2.VideoCapture(0)
seconds = 3600
pre_time = 0
starting_time = seconds
get_emotion = False
final_name = ""
sad = ['Bored', 'Neutral']
statics = static.Statics()
questions = statics.get_questions()
database = exam_page_model.ExamPageModel()

# Load DEEPFACE model
model = DeepFace.build_model('Emotion')
# Define emotion labels
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
key = ['A', 'B', 'C', 'D']

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def update_item_number():
    return f"{question_counter + 1}/{len(q_and_a_holder)}"


class TimerApp:
    def __init__(self, root, timer):
        self.root = root
        self.timer = timer
        # Initialize timer variables
        self.timer_running = False

        # Update the timer display
        self.update_timer()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def update_timer(self):
        global seconds
        if self.timer_running:
            seconds -= 1
            minutes = seconds // 60
            temp_seconds = seconds % 60
            time_str = f"{minutes:02}:{temp_seconds:02}"
            self.timer.config(text=time_str)
            self.root.after(1000, self.update_timer)


def on_click(pos):
    global cur_answer
    if not on_pre:
        answer = answers_holder[question_counter]
        if not cur_answer == 5:
            answer[cur_answer - 1].configure(fg_color="#EDF2F4")

        cur_answer = pos
        answer[pos - 1].configure(fg_color="#c4c4c4")
        return

    answer = pre_answer_holder[question_counter]
    if not cur_answer == 5:
        answer[cur_answer - 1].configure(fg_color="#EDF2F4")

    cur_answer = pos
    answer[pos - 1].configure(fg_color="#c4c4c4")


def show_answer():
    global score
    global pre_score
    if not on_pre:
        correct_ans = questions[shuffled_question_index[question_counter]].get("correct") - 1
        if correct_ans == cur_answer - 1:
            score += 1

        answer = answers_holder[question_counter]
        answer[cur_answer - 1].configure(fg_color="#701313")
        answer[questions[shuffled_question_index[question_counter]].get("correct") - 1].configure(fg_color="#32a852")
        return

    correct_ans = questions[pre_shuffled_question_index[question_counter]].get("correct") - 1
    if correct_ans == cur_answer - 1:
        pre_score += 1


def radiobutton_event(counter, value):
    pre_survey_answer[counter] = static_answers[value - 1]
    print(pre_survey_answer)


class ExamPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.instructions = None
        self.scrollable_frame = None
        self.pre_feelings = None
        self.timer_class = None
        self.camera_frame = None
        self.counter = None
        self.what_do_you_feel = None
        self.post_survey = None
        self.name = None
        self.radio_var = None
        self.pre_survey = None
        self.pre_survey1 = None
        self.pre_survey2 = None
        self.pre_survey3 = None
        self.next_button = None
        self.center_frame = None
        self.controller = controller
        self.camera_thread = None
        self.is_destroy = False
        self.stopper = False

    def create_frame(self):
        # center frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, fg_color="#2B2D42")
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")

        self.center_frame = Frame(self.scrollable_frame)
        self.center_frame.pack(side='top', expand=True, fill=BOTH, padx=40)

        # for the pre-survey

        self.instructions = Label(master=self.center_frame,
                                  font=("Arial", 15),
                                  justify='left',
                                  anchor='w',
                                  bg="#2B2D42",
                                  fg="white",
                                  wraplength=800,
                                  text="Instructions:\n\nSimilarly, the emotions section can be rated on the same "
                                       "scale, with 1 representing 'Not Expressive,' 2 representing 'Slightly "
                                       "Expressive,' 3 representing 'Moderately Expressive,' 4 representing 'Very "
                                       "Expressive,' and 5 representing 'Extremely Expressive.'"
                                  )
        self.instructions.pack(side='top', fill=X, pady=20)

        self.pre_survey = customtkinter.CTkFrame(master=self.center_frame, fg_color="#8D99AE")

        name_label = customtkinter.CTkLabel(self.pre_survey, text="Name", font=("Arial", 25))
        name_label.pack(side='top', anchor='w', padx=40, pady=(60, 20))

        self.name = customtkinter.CTkEntry(self.pre_survey,
                                           placeholder_text="Name",
                                           font=("Arial", 25),
                                           height=50,
                                           corner_radius=30)

        self.name.pack(side='top', padx=40, pady=(0, 10), fill=X)

        customtkinter.CTkLabel(master=self.pre_survey,
                               text="1. How confident are you in your prior knowledge of C++ problems?",
                               font=("Arial", 25),
                               corner_radius=10,
                               justify=LEFT).pack(side='top', anchor='w', padx=30, pady=(20, 30))

        self.radio_var = IntVar(value=0)
        customtkinter.CTkRadioButton(self.pre_survey, text="Not Confident at all",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(1, 1), variable=self.radio_var, value=1,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey, text="Slightly Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(1, 2), variable=self.radio_var, value=2,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey, text="Moderately Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(1, 3), variable=self.radio_var, value=3,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey, text="Very Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(1, 4), variable=self.radio_var, value=4,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey, text="Extremely Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(1, 5), variable=self.radio_var, value=5,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))

        customtkinter.CTkLabel(master=self.pre_survey,
                               text="2. How confident are you in your current understanding of C++ problems?",
                               font=("Arial", 25),
                               corner_radius=10,
                               justify=LEFT).pack(side='top', anchor='w', padx=30, pady=(20, 30))

        self.radio_var = IntVar(value=0)
        customtkinter.CTkRadioButton(self.pre_survey, text="Not Confident at all",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(2, 1), variable=self.radio_var, value=1,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey, text="Slightly Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(2, 2), variable=self.radio_var, value=2,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey, text="Moderately Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(2, 3), variable=self.radio_var, value=3,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey, text="Very Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(2, 4), variable=self.radio_var, value=4,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey, text="Extremely Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(2, 5), variable=self.radio_var, value=5,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))

        self.pre_survey.pack(fill="both", expand=True, side='top')

        next_holder = Frame(self.center_frame)

        self.next_button = Button(next_holder, text="Next",
                                  cursor='hand2',
                                  bg="#EDF2F4",
                                  fg="black",
                                  borderwidth=0,
                                  highlightthickness=0,
                                  width=20,
                                  height=2,
                                  font=("Times", 12),
                                  command=self.goto_next
                                  )

        divider = customtkinter.CTkLabel(master=next_holder, text="", corner_radius=1, fg_color="#FE3F56", height=48,
                                         width=10)
        divider1 = customtkinter.CTkLabel(master=next_holder, text="", corner_radius=1, fg_color="#FE3F56", height=48,
                                          width=10)

        next_holder.pack(side="bottom", anchor="e", pady=20)
        divider.pack(side="right")
        self.next_button.pack(side="right")
        divider1.pack(side="right")

        self.post_survey = Frame(self.center_frame)
        self.what_do_you_feel = customtkinter.CTkTextbox(self.post_survey, height=5, font=("Arial", 10), padx=10,
                                                         pady=10)
        # generate questions
        self.get_questions()

        # right frame
        right_frame = Frame(self)
        right_frame.grid(row=0, column=1, sticky="nsew")

        # holder
        holder = Frame(right_frame, bg="#2B2D42")
        holder.grid(row=0, column=0, pady=(50, 10), padx=(0, 10), sticky='we')

        # timer and count
        timer = Label(holder, text="00:00", font=("Arial", 15), bg="#EDF2F4", fg="black", width=10)
        divider3 = customtkinter.CTkLabel(master=holder, text="", corner_radius=1, fg_color="#FE3F56", width=10,
                                          height=30)
        divider4 = customtkinter.CTkLabel(master=holder, text="", corner_radius=1, fg_color="#FE3F56", width=10,
                                          height=30)

        self.counter = Label(holder, text=update_item_number(), font=("Arial", 15), bg="#EDF2F4", fg="black", width=10)
        divider4.pack(side="right", padx=(0, 10))
        timer.pack(side="right")
        divider3.pack(side="right", padx=(0, 10))
        self.counter.pack(side="right")

        self.camera_frame = Label(right_frame, bg="black", height=20)
        self.camera_frame.grid(row=1, column=0, padx=(0, 20), sticky='we')

        right_frame.columnconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.grid_rowconfigure(0, weight=1)
        self.config(bg='#2B2D42')
        right_frame.config(bg='#2B2D42')
        self.center_frame.config(bg='#2B2D42')
        self.center_frame.grid_rowconfigure(0, weight=0)
        self.center_frame.grid_rowconfigure(1, weight=1)
        self.timer_class = TimerApp(self, timer)

    def show_next_pre_survey(self):
        self.pre_survey1 = customtkinter.CTkFrame(master=self.center_frame, fg_color="#8D99AE")
        customtkinter.CTkLabel(master=self.pre_survey1,
                               text="3. Rate your experience on coding or background on this topic of C++ problems",
                               font=("Arial", 25),
                               corner_radius=10,
                               justify=LEFT).pack(side='top', anchor='w', padx=30, pady=(20, 30))

        self.radio_var = IntVar(value=0)
        customtkinter.CTkRadioButton(self.pre_survey1, text="Not Confident at all",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(3, 1), variable=self.radio_var, value=1,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Slightly Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(3, 2), variable=self.radio_var, value=2,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Moderately Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(3, 3), variable=self.radio_var, value=3,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Very Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(3, 4), variable=self.radio_var, value=4,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Extremely Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(3, 5), variable=self.radio_var, value=5,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))

        customtkinter.CTkLabel(master=self.pre_survey1,
                               text="4. How expressive are you in showing a NEUTRAL emotion during examinations?",
                               font=("Arial", 25),
                               corner_radius=10,
                               justify=LEFT).pack(side='top', anchor='w', padx=30, pady=(20, 30))

        self.radio_var = IntVar(value=0)
        customtkinter.CTkRadioButton(self.pre_survey1, text="Not Confident at all",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(4, 1), variable=self.radio_var, value=1,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Slightly Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(4, 2), variable=self.radio_var, value=2,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Moderately Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(4, 3), variable=self.radio_var, value=3,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Very Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(4, 4), variable=self.radio_var, value=4,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Extremely Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(4, 5), variable=self.radio_var, value=5,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))

        customtkinter.CTkLabel(master=self.pre_survey1,
                               text="5. How expressive are you in showing EXCITEMENT during examinations?",
                               font=("Arial", 25),
                               corner_radius=10,
                               justify=LEFT).pack(side='top', anchor='w', padx=30, pady=(20, 30))

        self.radio_var = IntVar(value=0)
        customtkinter.CTkRadioButton(self.pre_survey1, text="Not Confident at all",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(5, 1), variable=self.radio_var, value=1,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Slightly Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(5, 2), variable=self.radio_var, value=2,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Moderately Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(5, 3), variable=self.radio_var, value=3,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Very Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(5, 4), variable=self.radio_var, value=4,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey1, text="Extremely Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(5, 5), variable=self.radio_var, value=5,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))

        self.pre_survey1.pack(fill="both", expand=True, side='top')

    def show_next_pre_survey2(self):
        self.pre_survey2 = customtkinter.CTkFrame(master=self.center_frame, fg_color="#8D99AE")
        customtkinter.CTkLabel(master=self.pre_survey2,
                               text="6. How expressive are you in showing BOREDOM during examinations?",
                               font=("Arial", 25),
                               corner_radius=10,
                               justify=LEFT).pack(side='top', anchor='w', padx=30, pady=(20, 30))

        self.radio_var = IntVar(value=0)
        customtkinter.CTkRadioButton(self.pre_survey2, text="Not Confident at all",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(6, 1), variable=self.radio_var, value=1,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Slightly Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(6, 2), variable=self.radio_var, value=2,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Moderately Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(6, 3), variable=self.radio_var, value=3,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Very Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(6, 4), variable=self.radio_var, value=4,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Extremely Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(6, 5), variable=self.radio_var, value=5,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkLabel(master=self.pre_survey2,
                               text="7. How expressive are you in showing FRUSTRATION during examinations?",
                               font=("Arial", 25),
                               corner_radius=10,
                               justify=LEFT).pack(side='top', anchor='w', padx=30, pady=(20, 30))

        self.radio_var = IntVar(value=0)
        customtkinter.CTkRadioButton(self.pre_survey2, text="Not Confident at all",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(7, 1), variable=self.radio_var, value=1,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Slightly Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(7, 2), variable=self.radio_var, value=2,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Moderately Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(7, 3), variable=self.radio_var, value=3,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Very Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(7, 4), variable=self.radio_var, value=4,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Extremely Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(7, 5), variable=self.radio_var, value=5,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))

        customtkinter.CTkLabel(master=self.pre_survey2,
                               text="8. How expressive are you in showing CONFUSION during examinations?",
                               font=("Arial", 25),
                               corner_radius=10,
                               justify=LEFT).pack(side='top', anchor='w', padx=30, pady=(20, 30))

        self.radio_var = IntVar(value=0)
        customtkinter.CTkRadioButton(self.pre_survey2, text="Not Confident at all",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(8, 1), variable=self.radio_var, value=1,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Slightly Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(8, 2), variable=self.radio_var, value=2,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Moderately Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(8, 3), variable=self.radio_var, value=3,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Very Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(8, 4), variable=self.radio_var, value=4,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        customtkinter.CTkRadioButton(self.pre_survey2, text="Extremely Confident",
                                     font=("Arial", 20),
                                     command=lambda: radiobutton_event(8, 5), variable=self.radio_var, value=5,
                                     fg_color="#EDF2F4").pack(side='top', anchor='w', padx=80, pady=(0, 40))
        self.pre_survey2.pack(fill="both", expand=True, side='top')

    def show_final_pre_survey(self):
        self.pre_survey3 = customtkinter.CTkFrame(master=self.center_frame, fg_color="#8D99AE")
        customtkinter.CTkLabel(master=self.pre_survey3,
                               text="9. How do you feel before taking an exam?",
                               font=("Arial", 25),
                               corner_radius=10,
                               justify=LEFT).pack(side='top', anchor='w', padx=30, pady=(20, 30))

        self.pre_feelings = customtkinter.CTkTextbox(master=self.pre_survey3, font=("Arial", 20), corner_radius=10,
                                                     height=300)
        self.pre_feelings.pack(side='top', anchor='w', fill=X, padx=30, pady=(10, 30))
        self.pre_survey3.pack(fill="both", expand=True, side='top')

    def start_camera_thread(self):
        self.camera_thread = threading.Thread(target=self.show_frame, args=())
        self.camera_thread.start()

    def show_next_question(self):
        global question_counter
        global starting_time
        global on_post
        global cur_answer
        global on_pre
        global seconds
        global pre_time

        if not on_pre:
            self.next_button["state"] = "normal"
            q_and_a_holder[question_counter].destroy()
            question_counter += 1
            q_and_a_holder[question_counter].pack(fill="both", expand=True, pady=10)
            self.counter.config(text=update_item_number())
            starting_time = seconds
            cur_answer = 5
            return

        pre_q_and_a_holder[question_counter].destroy()
        question_counter += 1
        (pre_q_and_a_holder[question_counter].pack(fill="both", expand=True, pady=10)
         if question_counter < 30 else q_and_a_holder[0].pack(fill="both", expand=True, pady=10))

        pre_times.append(starting_time - seconds)
        starting_time = seconds
        if question_counter == 30:
            on_pre = False
            pre_time = 3600 - seconds
            question_counter = 0
            seconds = 3600
            starting_time = seconds
            self.next_button.config(text="Next")
            print(pre_answers)
            print(pre_emotions)
            print(pre_times)
            print(pre_score)
            print(pre_time)

        self.counter.config(text=update_item_number())
        cur_answer = 5

    def goto_next(self):
        global is_first
        global on_post
        global question_counter
        global cur_answer
        global get_emotion
        global times
        global final_name
        global pre_survey_part
        global on_pre
        global seconds
        global starting_time
        global from_pre

        if question_counter == 0:
            self.instructions.config(
                text="Please choose the letter of the correct answer and place it beside "
                     "the respective number.\n\n I. Fill in the blanks.")
        if question_counter == 9:
            self.instructions.config(
                text="Please choose the letter of the correct answer and place it beside the "
                     "respective number.\n\n II. Choose the letter of the correct answer.")
        if question_counter == 19:
            self.instructions.config(
                text="Please choose the letter of the correct answer and place it beside the "
                     "respective number.\n\n III. Please choose the correct letter that "
                     "represents the output of the given C++ code below.")

        if is_first:
            if pre_survey_part == 0:
                if self.name.get() == "":
                    messagebox.showinfo("showinfo", "Sorry but name is a required field!")
                    return
                for i in range(2):
                    if i + 1 not in pre_survey_answer.keys():
                        messagebox.showinfo("showinfo", f"Sorry but question {i + 1} is a required field!")
                        return

                final_name = self.name.get()
                pre_survey_part += 1
                self.pre_survey.destroy()
                self.show_next_pre_survey()
                return

            if pre_survey_part == 1:
                i = 3
                while i < 5:
                    if i + 1 not in pre_survey_answer.keys():
                        messagebox.showinfo("showinfo", f"Sorry but question {i + 1} is a required field!")
                        return
                    i += 1

                pre_survey_part += 1
                self.pre_survey1.destroy()
                self.show_next_pre_survey2()
                return

            if pre_survey_part == 2:
                i = 5
                while i < 8:
                    if i + 1 not in pre_survey_answer.keys():
                        messagebox.showinfo("showinfo", f"Sorry but question {i + 1} is a required field!")
                        return
                    i += 1

                pre_survey_part += 1
                self.pre_survey2.destroy()
                self.show_final_pre_survey()
                self.next_button.config(text="Start Pre Exam")
                return

            if pre_survey_part == 3:
                if self.pre_feelings.get("0.0", 'end-1c') == "":
                    messagebox.showinfo("showinfo", "Sorry but your feelings is a required field!")
                    return

                pre_survey_answer[9] = self.pre_feelings.get("0.0", 'end-1c')
                self.pre_survey3.destroy()
                pre_q_and_a_holder[question_counter].pack(fill="both", expand=True, pady=10)
                is_first = False
                self.timer_class.start_timer()
                on_post = False
                self.next_button.config(text="Next")
                threading.Thread(target=self.open_get_emotion, args=()).start()

        elif question_counter < len(q_and_a_holder) and not on_post and on_pre:
            # post survey
            if cur_answer == 5:
                messagebox.showinfo("showinfo", "Sorry but you haven't choose an answer yet!")
                return
            show_answer()
            pre_answers[pre_shuffled_question_index[question_counter]] = key[cur_answer - 1]
            self.show_next_question()
            if question_counter == 29:
                self.next_button.config(text="Start Exam")
            return

        elif question_counter < len(q_and_a_holder) and not on_post:
            # post survey
            if cur_answer == 5:
                messagebox.showinfo("showinfo", "Sorry but you haven't choose an answer yet!")
                return

            show_answer()
            answers[shuffled_question_index[question_counter]] = key[cur_answer - 1]
            # show_answer_stopper.start_thread()
            self.next_button["state"] = "disabled"
            self.after(1000, self.show_next_question if not question_counter == 29 else self.show_post_survey)
            times.append(starting_time - seconds)
            if question_counter == 29:
                on_post = True
            return

        else:
            post_survey_answer = self.what_do_you_feel.get("0.0", 'end-1c')
            if len(post_survey_answer) == 0:
                messagebox.showinfo("showinfo", "Sorry but Post-Survey Feedback is a required field!")
                return
            if question_counter + 1 > len(emotions):
                temp_emotion = ["No Emotion"]
                emotions.append(temp_emotion)

            translation = translator.translate(post_survey_answer, src='tl', dest='en')
            text = translation.text
            prediction = classifier(text, )

            pred = prediction[0]["label"]
            pred_score = prediction[0]["score"]


            if pred == 'joy':
                pred = 'Excited'
            if pred == 'sadness':
                pred = sad[rand.randint(0, 1)]
            elif pred == 'anger':
                pred = 'Frustrated'
            elif pred == 'surprise':
                pred = 'Surprised'
            elif pred == 'fear':
                pred = 'Nervous'
            elif pred == 'love':
                pred = 'Excited'

            if pred_score < 0.65:
                pred = "No Emotion"

            if len(text) < 2:
                pred = "No Emotion"

            post_surveys.append(post_survey_answer)
            translations.append(text)
            nlps.append(pred)

            self.stopper = True
            self.is_destroy = True
            print(f"answers: {answers}")
            print(f"nlps:{nlps}")
            print(f"emotion:{emotions}")
            print(f"times:{times}")
            data = {
                'Bored': 0,
                'Frustrated': 0,
                'Excited': 0,
                'Neutral': 0,
                'Nervous': 0,
                'Surprised': 0,
            }

            for item in emotions:
                for emotion in item:
                    if emotion != "No Emotion":
                        data[emotion] = data[emotion] + 1

            # get the average emotion for every number
            pre_final_emotion = []
            for emotion in pre_emotions:
                pre_final_emotion.append(max(emotion, key=emotion.count))

            final_emotion = []
            for emotion in emotions:
                final_emotion.append(max(emotion, key=emotion.count))

            total_time = 3600 - seconds

            temp = ''
            pre_survey_translation = translator.translate(pre_survey_answer[9], src='tl', dest='en').text
            pre_survey_translations = ['-', '-', '-', '-', '-', '-', '-', '-', pre_survey_translation]
            print(pre_survey_translation)
            for file in os.listdir(os.getcwd() + "\\myDir"):
                temp = pathlib.Path(os.path.join(os.getcwd() + "\\myDir", file)).suffix
                temp = temp.replace('.', '')

            data_model = {
                'name': final_name,
                'answers': answers,
                'cnns': final_emotion,
                'nlps': nlps,
                'score': score,
                'time': total_time,
                'times': times,
                'from': temp,
                'post_surveys': post_surveys,
                'translations': translations,
                'pre_surveys': list(pre_survey_answer.values()),
                'pre_survey_translation': pre_survey_translations,
                'pre_exam_answers': pre_answers,
                'pre_exam_time': pre_time,
                'pre_exam_times': pre_times,
                'pre_exam_score': pre_score,
                'pre_exam_cnn': pre_emotions,
            }

            database.add_data(data_model)
            self.controller.show_frame("ShowScore", score, total_time, data)

    def show_post_survey(self):
        global on_post

        sleep(1)

        self.next_button["state"] = "normal"
        self.post_survey = customtkinter.CTkFrame(master=self.center_frame, corner_radius=10, fg_color="#8D99AE")
        prompt_label = customtkinter.CTkLabel(master=self.post_survey,
                                              text=f"What do you feel answering the examination?",
                                              font=("Arial", 25),
                                              corner_radius=10,
                                              fg_color="#EDF2F4",
                                              height=80,
                                              justify=LEFT)

        self.what_do_you_feel = customtkinter.CTkTextbox(master=self.post_survey, font=("Arial", 20), corner_radius=10,
                                                         height=300)
        prompt_label.grid(column=0, row=0, sticky="nsew", padx=40, pady=(60, 20))
        self.what_do_you_feel.grid(column=0, row=1, sticky="nsew", padx=40, pady=(0, 60))
        self.what_do_you_feel.focus_set()

        self.post_survey.columnconfigure(0, weight=1)
        self.post_survey.rowconfigure(0, weight=1)
        self.post_survey.rowconfigure(1, weight=2)

        self.timer_class.stop_timer()
        q_and_a_holder[question_counter].destroy()
        self.post_survey.pack(fill="both", expand=True)

    def get_questions(self):
        global pre_q_and_a_holder
        global q_and_a_holder
        global pre_shuffled_question_index
        global shuffled_question_index

        pre_q_and_a_holder.clear()
        q_and_a_holder.clear()

        pre_answer_holder.clear()
        answers_holder.clear()

        # for exam
        # shuffle the array while putting the index of the item in the new array
        i = 0
        while i < 30:
            has_val = False
            if i < 10:
                rand_num = random.randint(0, 9)
                for index in shuffled_question_index:
                    if rand_num == index:
                        has_val = True
                        break
            elif i < 20:
                rand_num = random.randint(10, 19)
                for index in shuffled_question_index:
                    if rand_num == index:
                        has_val = True
                        break
            else:
                rand_num = random.randint(20, 29)
                for index in shuffled_question_index:
                    if rand_num == index:
                        has_val = True
                        break
            if has_val:
                continue
            i += 1
            shuffled_question_index.append(rand_num)

        for i in range(30):
            item = questions[shuffled_question_index[i]]
            question_holder = customtkinter.CTkFrame(self.center_frame, fg_color="#8D99AE", corner_radius=10)
            if shuffled_question_index[i] >= 20:
                about_us_image = Image.open(item['question'])
                about_us_image = about_us_image.resize((400, 200), Image.LANCZOS)
                about_us_tk = ImageTk.PhotoImage(about_us_image)
                question_label = customtkinter.CTkLabel(question_holder,
                                                        text='',
                                                        font=("Helvetica", 25),
                                                        justify='center',
                                                        wraplength=600,
                                                        fg_color="#EDF2F4",
                                                        corner_radius=10,
                                                        image=about_us_tk
                                                        )
                question_label["border"] = "0"
            else:
                question = item['question']
                question_label = customtkinter.CTkLabel(question_holder,
                                                        text=f'{question}',
                                                        font=("Helvetica", 25),
                                                        justify='center',
                                                        wraplength=600,
                                                        fg_color="#EDF2F4",
                                                        corner_radius=10,
                                                        )

            answer_1 = customtkinter.CTkButton(master=question_holder,
                                               corner_radius=10,
                                               text=item.get(1),
                                               fg_color="#EDF2F4",
                                               command=lambda: on_click(1),
                                               font=("Arial", 20),
                                               text_color="black",
                                               hover_color='#c4c4c4',
                                               )

            answer_2 = customtkinter.CTkButton(master=question_holder,
                                               corner_radius=10,
                                               text=item.get(2),
                                               fg_color="#EDF2F4",
                                               command=lambda: on_click(2),
                                               font=("Arial", 20),
                                               text_color="black",
                                               hover_color='#c4c4c4',
                                               )

            answer_3 = customtkinter.CTkButton(master=question_holder,
                                               corner_radius=10,
                                               text=item.get(3),
                                               fg_color="#EDF2F4",
                                               command=lambda: on_click(3),
                                               font=("Arial", 20),
                                               text_color="black",
                                               hover_color='#c4c4c4',
                                               )

            answer_4 = customtkinter.CTkButton(master=question_holder,
                                               corner_radius=10,
                                               text=item.get(4),
                                               fg_color="#EDF2F4",
                                               command=lambda: on_click(4),
                                               font=("Arial", 20),
                                               text_color="black",
                                               hover_color='#c4c4c4',
                                               )

            question_label.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=10, pady=20, ipady=60)
            answer_1.grid(column=0, row=1, sticky="nsew", padx=10, pady=(0, 10), ipady=60)
            answer_2.grid(column=1, row=1, sticky="nsew", padx=(0, 10), pady=(0, 10), ipady=60)
            answer_3.grid(column=0, row=2, sticky="nsew", padx=10, pady=(0, 20), ipady=60)
            answer_4.grid(column=1, row=2, sticky="nsew", padx=(0, 10), pady=(0, 20), ipady=60)

            answer_1._text_label.configure(wraplength=350, justify=CENTER)
            answer_2._text_label.configure(wraplength=350, justify=CENTER)
            answer_3._text_label.configure(wraplength=350, justify=CENTER)
            answer_4._text_label.configure(wraplength=350, justify=CENTER)

            question_holder.grid_columnconfigure(0, weight=1)
            question_holder.grid_columnconfigure(1, weight=1)
            question_holder.grid_rowconfigure(0, weight=2)
            question_holder.grid_rowconfigure(1, weight=1)
            question_holder.grid_rowconfigure(2, weight=1)

            answers_holder.append([answer_1, answer_2, answer_3, answer_4])
            q_and_a_holder.append(question_holder)

        # for pre-exam
        i = 0
        while i < 30:
            has_val = False
            if i < 10:
                rand_num = random.randint(0, 9)
                for index in pre_shuffled_question_index:
                    if rand_num == index:
                        has_val = True
                        break
            elif i < 20:
                rand_num = random.randint(10, 19)
                for index in pre_shuffled_question_index:
                    if rand_num == index:
                        has_val = True
                        break
            else:
                rand_num = random.randint(20, 29)
                for index in pre_shuffled_question_index:
                    if rand_num == index:
                        has_val = True
                        break
            if has_val:
                continue
            i += 1
            pre_shuffled_question_index.append(rand_num)

        for i in range(30):
            item = questions[pre_shuffled_question_index[i]]
            question_holder = customtkinter.CTkFrame(self.center_frame, fg_color="#8D99AE", corner_radius=10)
            if pre_shuffled_question_index[i] >= 20:
                about_us_image = Image.open(item['question'])
                about_us_image = about_us_image.resize((400, 200), Image.LANCZOS)
                about_us_tk = ImageTk.PhotoImage(about_us_image)
                question_label = customtkinter.CTkLabel(question_holder,
                                                        text='',
                                                        font=("Helvetica", 25),
                                                        justify='center',
                                                        wraplength=600,
                                                        fg_color="#EDF2F4",
                                                        corner_radius=10,
                                                        image=about_us_tk
                                                        )
                question_label["border"] = "0"
            else:
                question = item['question']
                question_label = customtkinter.CTkLabel(question_holder,
                                                        text=f'{question}',
                                                        font=("Helvetica", 25),
                                                        justify='center',
                                                        wraplength=600,
                                                        fg_color="#EDF2F4",
                                                        corner_radius=10,
                                                        )

            answer_1 = customtkinter.CTkButton(master=question_holder,
                                               corner_radius=10,
                                               text=item.get(1),
                                               fg_color="#EDF2F4",
                                               command=lambda: on_click(1),
                                               font=("Arial", 20),
                                               text_color="black",
                                               hover_color='#c4c4c4',
                                               )

            answer_2 = customtkinter.CTkButton(master=question_holder,
                                               corner_radius=10,
                                               text=item.get(2),
                                               fg_color="#EDF2F4",
                                               command=lambda: on_click(2),
                                               font=("Arial", 20),
                                               text_color="black",
                                               hover_color='#c4c4c4',
                                               )

            answer_3 = customtkinter.CTkButton(master=question_holder,
                                               corner_radius=10,
                                               text=item.get(3),
                                               fg_color="#EDF2F4",
                                               command=lambda: on_click(3),
                                               font=("Arial", 20),
                                               text_color="black",
                                               hover_color='#c4c4c4',
                                               )

            answer_4 = customtkinter.CTkButton(master=question_holder,
                                               corner_radius=10,
                                               text=item.get(4),
                                               fg_color="#EDF2F4",
                                               command=lambda: on_click(4),
                                               font=("Arial", 20),
                                               text_color="black",
                                               hover_color='#c4c4c4',
                                               )

            question_label.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=10, pady=20, ipady=60)
            answer_1.grid(column=0, row=1, sticky="nsew", padx=10, pady=(0, 10), ipady=60)
            answer_2.grid(column=1, row=1, sticky="nsew", padx=(0, 10), pady=(0, 10), ipady=60)
            answer_3.grid(column=0, row=2, sticky="nsew", padx=10, pady=(0, 20), ipady=60)
            answer_4.grid(column=1, row=2, sticky="nsew", padx=(0, 10), pady=(0, 20), ipady=60)

            answer_1._text_label.configure(wraplength=350, justify=CENTER)
            answer_2._text_label.configure(wraplength=350, justify=CENTER)
            answer_3._text_label.configure(wraplength=350, justify=CENTER)
            answer_4._text_label.configure(wraplength=350, justify=CENTER)

            question_holder.grid_columnconfigure(0, weight=1)
            question_holder.grid_columnconfigure(1, weight=1)
            question_holder.grid_rowconfigure(0, weight=2)
            question_holder.grid_rowconfigure(1, weight=1)
            question_holder.grid_rowconfigure(2, weight=1)

            pre_answer_holder.append([answer_1, answer_2, answer_3, answer_4])
            pre_q_and_a_holder.append(question_holder)

    def show_frame(self):
        global get_emotion
        while True:
            if self.stopper:
                print("heyyyyyy")
                break

            _, frame = cap.read()
            frame = cv2.flip(frame, 1)

            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

            for (x, y, w, h) in faces:
                # Extract the face ROI (Region of Interest)
                face_roi = gray_frame[y:y + h, x:x + w]

                # Resize the face ROI to match the input shape of the model
                resized_face = cv2.resize(face_roi, (48, 48), interpolation=cv2.INTER_AREA)

                # Preprocess the image for DEEPFACE
                normalized_face = resized_face / 255.0
                reshaped_face = normalized_face.reshape(1, 48, 48, 1)

                # Predict emotions using the pre-trained model
                preds = model.predict(reshaped_face)
                emotion_idx = np.argmax(preds)
                emotion = emotion_labels[emotion_idx]

                # Draw rectangle around face and label with predicted emotion
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                if emotion == "sad":
                    emotion = "Bored"
                elif emotion == "angry":
                    emotion = "Frustrated"
                elif emotion == "happy":
                    emotion = "Excited"
                elif emotion == "disgust":
                    continue
                elif emotion == "neutral":
                    emotion = "Neutral"
                elif emotion == "fear":
                    emotion = "Nervous"
                elif emotion == "surprise":
                    emotion = "Surprised"

                cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

                if get_emotion:
                    if question_counter + 1 > len(emotions):
                        temp_emotion = [emotion]
                        pre_emotions.append(temp_emotion) if on_pre else emotions.append(temp_emotion)
                    else:
                        temp_emotion = emotions[question_counter]
                        temp_emotion.append(emotion)

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)

            if not self.is_destroy:
                imgtk = ImageTk.PhotoImage(image=img)
                self.camera_frame.imgtk = imgtk
                self.camera_frame.configure(image=imgtk, width=200, height=300)

            img.close()
            sleep(.01)

    def open_get_emotion(self):
        global get_emotion
        while not self.is_destroy:
            get_emotion = False
            if on_post:
                for i in range(2):
                    if self.is_destroy:
                        return
                    sleep(1)
                get_emotion = True
            sleep(.15)

    def re_init(self):
        global is_first
        global on_post
        global question_counter
        global cur_answer
        global q_and_a_holder
        global nlps
        global answers
        global pre_answers
        global pre_shuffled_question_index
        global pre_times
        global pre_q_and_a_holder
        global pre_answer_holder
        global on_pre
        global emotions
        global pre_emotions
        global answers_holder
        global times
        global score
        global cap
        global seconds
        global starting_time
        global get_emotion
        global final_name
        global post_surveys
        global translations
        global pre_survey_answer
        global shuffled_question_index
        global pre_survey_part

        self.is_destroy = False
        self.stopper = False
        is_first = True
        on_post = False
        on_pre = True
        pre_survey_part = 0
        question_counter = 0
        cur_answer = 5
        nlps = []
        pre_answers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                       5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                       5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        answers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                   5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                   5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        pre_emotions = []
        emotions = []
        pre_times = []
        times = []
        post_surveys = []
        translations = []
        pre_shuffled_question_index = []
        shuffled_question_index = []
        pre_survey_answer = {}
        score = 0
        cap = cv2.VideoCapture(0)
        seconds = 3600
        starting_time = seconds
        get_emotion = False
        final_name = ""
