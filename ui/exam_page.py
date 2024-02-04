from tkinter import *
from tkinter import messagebox
import window_setter as ws
from statics import static, rounder
import threading
from time import sleep
import customtkinter

# for mixing the cards
is_first = True
on_post = False
is_destroy = False
question_counter = 0
cur_answer = 5
q_and_a_holder = []
nlps = []
answers = []
answers_holder = []
score = 0
statics = static.Statics()
questions = statics.get_questions()


def set_enabled():
    for i in range(15):
        if is_destroy:
            return
        sleep(1)

    next_button["state"] = "normal"


class Stopper:
    def __init__(self):
        self.thread = threading.Thread(target=set_enabled, args=())

    def start_thread(self):
        next_button["state"] = "disabled"
        self.thread.start()


class ShowAnsStopper:
    def __init__(self):
        self.thread = threading.Thread(target=show_post_survey, args=())

    def start_thread(self):
        next_button["state"] = "disabled"
        self.thread.start()


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        # Initialize timer variables
        self.seconds = 3600
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
        if self.timer_running:
            self.seconds -= 1
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            time_str = f"{minutes:02}:{seconds:02}"
            timer.config(text=time_str)
            self.root.after(1000, self.update_timer)


def on_click(pos):
    global cur_answer
    answer = answers_holder[question_counter]
    if not cur_answer == 5:
        answer[cur_answer - 1].configure(fg_color="#EDF2F4")

    cur_answer = pos
    answer[pos - 1].configure(fg_color="#c4c4c4")


def get_questions():
    global q_and_a_holder
    for item in questions:
        question_holder = customtkinter.CTkFrame(center_frame, fg_color="#8D99AE", corner_radius=10)

        question_label = customtkinter.CTkLabel(question_holder,
                                                text=item.get("question"),
                                                font=("Helvetica", 25),
                                                justify='center',
                                                wraplength=700,
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
                                           hover_color='#c4c4c4'
                                           )

        answer_2 = customtkinter.CTkButton(master=question_holder,
                                           corner_radius=10,
                                           text=item.get(2),
                                           fg_color="#EDF2F4",
                                           command=lambda: on_click(2),
                                           font=("Arial", 20),
                                           text_color="black",
                                           hover_color='#c4c4c4'
                                           )

        answer_3 = customtkinter.CTkButton(master=question_holder,
                                           corner_radius=10,
                                           text=item.get(3),
                                           fg_color="#EDF2F4",
                                           command=lambda: on_click(3),
                                           font=("Arial", 20),
                                           text_color="black",
                                           hover_color='#c4c4c4'
                                           )

        answer_4 = customtkinter.CTkButton(master=question_holder,
                                           corner_radius=10,
                                           text=item.get(4),
                                           fg_color="#EDF2F4",
                                           command=lambda: on_click(4),
                                           font=("Arial", 20),
                                           text_color="black",
                                           hover_color='#c4c4c4'
                                           )

        question_label.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=20, pady=20)
        answer_1.grid(column=0, row=1, sticky="nsew", padx=20, pady=20)
        answer_2.grid(column=1, row=1, sticky="nsew", padx=20, pady=20)
        answer_3.grid(column=0, row=2, sticky="nsew", padx=20, pady=20)
        answer_4.grid(column=1, row=2, sticky="nsew", padx=20, pady=20)

        question_holder.grid_columnconfigure(0, weight=1)
        question_holder.grid_columnconfigure(1, weight=1)
        question_holder.grid_rowconfigure(0, weight=2)
        question_holder.grid_rowconfigure(1, weight=1)
        question_holder.grid_rowconfigure(2, weight=1)

        answers_holder.append([answer_1, answer_2, answer_3, answer_4])
        q_and_a_holder.append(question_holder)


def show_answer():
    global score
    correct_ans = questions[question_counter].get("correct") - 1
    if correct_ans == cur_answer-1:
        score += 1

    answer = answers_holder[question_counter]
    answer[cur_answer - 1].configure(fg_color="#701313")
    answer[questions[question_counter].get("correct") - 1].configure(fg_color="#32a852")


def show_post_survey():
    global post_survey
    global on_post
    global what_do_you_feel

    sleep(1)

    next_button["state"] = "normal"
    post_survey = customtkinter.CTkFrame(master=center_frame, corner_radius=10, fg_color="#8D99AE")
    prompt_label = customtkinter.CTkLabel(master=post_survey,
                                          text=f"What do you feel answering question number {question_counter + 1}?",
                                          font=("Arial", 25),
                                          corner_radius=10,
                                          fg_color="#EDF2F4",
                                          justify=LEFT)

    what_do_you_feel = customtkinter.CTkTextbox(master=post_survey, font=("Arial", 20), corner_radius=10)
    prompt_label.grid(column=0, row=0, sticky="nsew", padx=40, pady=(60, 20))
    what_do_you_feel.grid(column=0, row=1, sticky="nsew", padx=40, pady=(0, 60))
    what_do_you_feel.focus_set()

    post_survey.columnconfigure(0, weight=1)
    post_survey.rowconfigure(0, weight=1)
    post_survey.rowconfigure(1, weight=2)

    on_post = False
    timer_class.stop_timer()
    q_and_a_holder[question_counter].destroy()
    post_survey.pack(fill="both", expand=True, padx=20, pady=50)


def goto_next():
    show_answer_stopper = ShowAnsStopper()
    stopper = Stopper()
    global timer_class
    global is_first
    global on_post
    global question_counter
    global post_survey
    global what_do_you_feel
    global cur_answer

    if is_first:
        pre_survey.destroy()
        q_and_a_holder[question_counter].pack(fill="both", expand=True, padx=20, pady=10)
        next_button.config(text="Next")
        is_first = False
        timer_class.start_timer()
        # stopper.start_thread()
        on_post = True

    elif question_counter < len(q_and_a_holder) - 1 and not on_post:
        post_survey_answer = what_do_you_feel.get("0.0", 'end-1c')
        if len(post_survey_answer) == 0:
            messagebox.showinfo("showinfo", "Sorry but Post-Survey Feedback is a required field!")
            return
        cur_answer = 5
        nlps.append(post_survey_answer)
        post_survey.destroy()
        timer_class.start_timer()
        q_and_a_holder[question_counter].destroy()
        question_counter = question_counter + 1
        q_and_a_holder[question_counter].pack(fill="both", expand=True, padx=20, pady=10)
        # next_button["state"] = "disabled"
        # stopper.start_thread()
        counter.config(text=update_item_number())
        on_post = True

    elif question_counter < len(q_and_a_holder) and on_post:
        # post survey
        if cur_answer == 5:
            messagebox.showinfo("showinfo", "Sorry but you haven't choose an answer yet!")
            return

        print(question_counter)
        show_answer()
        answers.append(cur_answer)
        show_answer_stopper.start_thread()

    else:
        post_survey_answer = what_do_you_feel.get("0.0", 'end-1c')
        if len(post_survey_answer) == 0:
            messagebox.showinfo("showinfo", "Sorry but Post-Survey Feedback is a required field!")
            return

        nlps.append(post_survey_answer)
        print(f"answers{answers}")
        print(f"nlps:{nlps}")
        print(f"score:{score}")
        main_frame.destroy()
        import show_score


def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())


main_frame = Tk()
main_frame.resizable(False, False)
main_frame.config(bg='black')
main_frame.title(statics.get_title())
ws.FullScreenApp(main_frame)
main_frame.state('zoomed')

timer_class = TimerApp(main_frame)

# center frame
center_frame = Frame(main_frame)
center_frame.grid(row=0, column=0, sticky="nsew")

# for the pre-survey

instructions = customtkinter.CTkLabel(master=center_frame,
                                      font=("Arial", 20),
                                      text_color="white",
                                      wraplength=1100,
                                      height=100,
                                      justify='left',
                                      text="Instructions:\n\nSimilarly, the emotions section can be rated on the same scale, with 1 representing 'Not Expressive,' 2 representing 'Slightly Expressive,' 3 representing 'Moderately Expressive,' 4 representing 'Very Expressive,' and 5 representing 'Extremely Expressive.'"
                                      )
instructions.pack(fill='x', padx=40, pady=20)

pre_survey = customtkinter.CTkFrame(master=center_frame, fg_color="#8D99AE")
prompt_label_pre = customtkinter.CTkLabel(master=pre_survey,
                                          text=f"What do you feel answering question number {question_counter + 1}?",
                                          font=("Arial", 25),
                                          corner_radius=10,
                                          fg_color="#EDF2F4",
                                          justify=LEFT)

prompt_label_pre.grid(column=0, row=0, sticky="nsew", padx=40, pady=(60, 20))

radio_var = IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(pre_survey, text="CTkRadioButton 1",
                                             font=("Arial", 20),
                                             command=radiobutton_event, variable=radio_var, value=1, fg_color="#EDF2F4")
radiobutton_2 = customtkinter.CTkRadioButton(pre_survey, text="CTkRadioButton 2",
                                             font=("Arial", 20),
                                             command=radiobutton_event, variable=radio_var, value=2, fg_color="#EDF2F4")
radiobutton_3 = customtkinter.CTkRadioButton(pre_survey, text="CTkRadioButton 3",
                                             font=("Arial", 20),
                                             command=radiobutton_event, variable=radio_var, value=1, fg_color="#EDF2F4")
radiobutton_4 = customtkinter.CTkRadioButton(pre_survey, text="CTkRadioButton 4",
                                             font=("Arial", 20),
                                             command=radiobutton_event, variable=radio_var, value=2, fg_color="#EDF2F4")

radiobutton_1.grid(column=0, row=1, sticky="nsew", padx=40)
radiobutton_2.grid(column=0, row=2, sticky="nsew", padx=40)
radiobutton_3.grid(column=0, row=3, sticky="nsew", padx=40)
radiobutton_4.grid(column=0, row=4, sticky="nsew", padx=40)

pre_survey.grid_rowconfigure(0, weight=2)
pre_survey.grid_rowconfigure(1, weight=1)
pre_survey.grid_rowconfigure(2, weight=1)
pre_survey.grid_rowconfigure(3, weight=1)
pre_survey.grid_rowconfigure(4, weight=1)

pre_survey.grid_columnconfigure(0, weight=1)

pre_survey.pack(fill="both", expand=True, padx=40, pady=20)

next_holder = Frame(center_frame)

next_button = Button(next_holder, text="Start Exam",
                     cursor='hand2',
                     bg="#EDF2F4",
                     fg="black",
                     borderwidth=0,
                     highlightthickness=0,
                     width=20,
                     height=2,
                     font=("Times", 12),
                     command=goto_next
                     )

divider = customtkinter.CTkLabel(master=next_holder, text="", corner_radius=1, fg_color="#FE3F56", height=48, width=10)
divider1 = customtkinter.CTkLabel(master=next_holder, text="", corner_radius=1, fg_color="#FE3F56", height=48, width=10)

next_holder.pack(side="bottom", anchor="e", padx=(0, 40), pady=20)
divider.pack(side="right")
next_button.pack(side="right")
divider1.pack(side="right")

post_survey = Frame(center_frame)
what_do_you_feel = customtkinter.CTkTextbox(post_survey, height=5, font=("Arial", 10), padx=10, pady=10)
# generate questions
get_questions()

# right frame
right_frame = Frame(main_frame)
right_frame.grid(row=0, column=1, sticky="nsew")

# holder
holder = Frame(right_frame, bg="#2B2D42")
holder.grid(row=0, column=0, pady=(50, 10), padx=(0, 10), sticky='we')

# timer and count
timer = Label(holder, text="00:00", font=("Arial", 15), bg="#EDF2F4", fg="black", width=10)
divider3 = customtkinter.CTkLabel(master=holder, text="", corner_radius=1, fg_color="#FE3F56", width=10, height=30)
divider4 = customtkinter.CTkLabel(master=holder, text="", corner_radius=1, fg_color="#FE3F56", width=10, height=30)


def update_item_number():
    return f"{question_counter + 1}/{len(q_and_a_holder)}"


def on_close():
    global is_destroy
    is_destroy = True
    main_frame.destroy()


counter = Label(holder, text=update_item_number(), font=("Arial", 15), bg="#EDF2F4", fg="black", width=10)
divider4.pack(side="right", padx=(0, 10))
timer.pack(side="right")
divider3.pack(side="right", padx=(0, 10))
counter.pack(side="right")

camera_frame = Label(right_frame, bg="black", height=20)
camera_frame.grid(row=1, column=0, padx=(0, 20), sticky='we')

right_frame.columnconfigure(0, weight=1)

main_frame.grid_columnconfigure(0, weight=3)
main_frame.grid_columnconfigure(1, weight=2)
main_frame.rowconfigure(0, weight=1)
main_frame.protocol("WM_DELETE_WINDOW", on_close)
main_frame.config(bg='#2B2D42')
right_frame.config(bg='#2B2D42')
center_frame.config(bg='#2B2D42')
main_frame.mainloop()
