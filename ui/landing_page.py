from tkinter import *
from statics import static, rounder
import window_setter as ws
from PIL import ImageTk

statics = static.Statics()

main_frame = Tk()
main_frame.resizable(False, False)
main_frame.config(bg='black')
ws.FullScreenApp(main_frame)
main_frame.state('zoomed')


# toolbar
tool_bar = Frame(main_frame, width=0, height=200)
tool_bar.pack(fill=X, side="top")

# components of the toolbar

# logo
path = statics.get_logo()
image = ImageTk.PhotoImage(path)
logo = Label(tool_bar, image=image, width=50, height=50)
logo.pack(side='left', padx=10, pady=10)

# title
title = Label(tool_bar, text=statics.get_title(), font=("Arial", 20))
title.pack(side='left', padx=10, pady=10)

# login for admin
login = Button(tool_bar, text="login", cursor='hand2', font=("Arial", 15))
login.pack(side='right', padx=10, pady=10)

# about us
about_us = Label(tool_bar, text=statics.get_about_us(), font=("Arial", 15), cursor="hand2")
about_us.pack(side='right', padx=10, pady=10)

# policy
policy = Label(tool_bar, text=statics.get_policy(), font=("Arial", 15), cursor="hand2")
policy.pack(side='right', padx=10, pady=10)

# center frame
center_frame = Frame(main_frame, width=0, height=0)
center_frame.config(bg='skyblue')
center_frame.pack(side="top", fill=BOTH, expand=True)


def goto_exam_page():
    main_frame.destroy()
    import exam_page


# start the exam
start_exam = rounder.RoundedButton(center_frame,
                                   text="Start Exam",
                                   cursor='hand2',
                                   radius=55,
                                   btnbackground="#0078ff",
                                   btnforeground="#ffffff",
                                   borderwidth=0,
                                   highlightthickness=0,
                                   height=60,
                                   width=250,
                                   clicked=goto_exam_page
                                   )

start_exam.pack(expand=True)

main_frame.mainloop()
