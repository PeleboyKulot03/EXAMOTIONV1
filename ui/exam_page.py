from tkinter import *
import window_setter as ws
from statics import static

statics = static.Statics()
main_frame = Tk()
main_frame.resizable(False, False)
main_frame.config(bg='black')
main_frame.title(statics.get_title())
ws.FullScreenApp(main_frame)

# center frame
center_frame = Frame(main_frame)
center_frame.pack(side='left', expand=True, fill="both")

# for the pre-survey
pre_survey = Frame(center_frame)
pre_survey.config(bg='black')
pre_survey.pack(fill="both", expand=True, padx=20, pady=50)

# right frame
right_frame = Frame(main_frame)
right_frame.config(width=400)
right_frame.pack(side='left', fill="y")

# timer and count
timer = Label(right_frame, text="00:00", font=("Arial", 15), bg="black", fg="white")
counter = Label(right_frame, text="1/30", font=("Arial", 15), bg="black", fg="white")
timer.grid(row=0, column=0, pady=(50, 10), sticky="W")
counter.grid(row=0, column=1, padx=10, pady=(50, 10), sticky="W")

camera_frame = Label(right_frame, bg="black", height=30, width=70)
camera_frame.grid(row=1, column=0)

main_frame.mainloop()
