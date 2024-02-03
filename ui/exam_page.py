from tkinter import *
import window_setter as ws
from statics import static

# for mixing the cards
is_first = True
on_post = False
question_counter = 0


# def get_questions():

def goto_next():
    if is_first:
        pre_survey.destroy()


statics = static.Statics()
main_frame = Tk()
main_frame.resizable(False, False)
main_frame.config(bg='black')
main_frame.title(statics.get_title())
ws.FullScreenApp(main_frame)
main_frame.state('zoomed')

# center frame
center_frame = Frame(main_frame)
center_frame.grid(row=0, column=0, sticky="nsew")

# for the pre-survey
pre_survey = Frame(center_frame)
pre_survey.config(bg='black')
# pre_survey.pack(fill="both", expand=True, padx=20, pady=50)

question_holder = Frame(center_frame)
question_holder.config(bg='black')
question_holder.pack(fill="both", expand=True, padx=20, pady=50)

questionLabel = Label(question_holder,
                      text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris molestie leo vitae augue lacinia, a dignissim neque ultricies. Donec ut ex risus. Nunc at quam ultricies, congue nibh tempor, imperdiet metus. Vestibulum mi enim, finibus eget lacus quis, fringilla gravida erat. Etiam erat dolor, venenatis cursus est ut, hendrerit ullamcorper nunc.",
                      font=("Helvetica", 15),
                      justify='center',
                      wraplength=500,
                      height='10'
                      )

questionLabel.grid(column=0, row=0, sticky="nsew")
question_holder.grid_columnconfigure(0, weight=1)

# right frame
right_frame = Frame(main_frame)
right_frame.grid(row=0, column=1, sticky="nsew")

# holder
holder = Frame(right_frame)
holder.grid(row=0, column=0, pady=(50, 10), padx=(0, 10), sticky='we')

# timer and count
timer = Label(holder, text="00:00", font=("Arial", 15), bg="black", fg="white", width=10)
counter = Label(holder, text="1/30", font=("Arial", 15), bg="black", fg="white", width=10)
timer.pack(side="right", padx=10)
counter.pack(side="right")

camera_frame = Label(right_frame, bg="black", height=30)
camera_frame.grid(row=1, column=0, padx=(0, 20), sticky='we')

next_button = Button(right_frame, text="Next",
                     cursor='hand2',
                     bg="black",
                     fg="#ffffff",
                     borderwidth=0,
                     highlightthickness=0,
                     height=2,
                     font=("Times", 12)
                     )

next_button.grid(row=2, column=0, padx=(0, 20), pady=10, sticky='we')
right_frame.columnconfigure(0, weight=1)

main_frame.grid_columnconfigure(0, weight=3)
main_frame.grid_columnconfigure(1, weight=2)
main_frame.rowconfigure(0, weight=1)
main_frame.mainloop()
