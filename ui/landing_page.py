from tkinter import *
from statics import static, rounder
import window_setter as ws
from PIL import ImageTk, Image
import os

statics = static.Statics()

main_frame = Tk()
main_frame.resizable(False, False)
main_frame.config(bg='#2B2D42')
ws.FullScreenApp(main_frame)
main_frame.state('zoomed')


# toolbar
tool_bar = Frame(main_frame, width=0, height=200)
tool_bar.config(bg="#EDF2F4")
tool_bar.pack(fill=X, side="top")

# components of the toolbar
# logo
path = statics.get_logo()
path = path.resize((60, 60), Image.LANCZOS)
image = ImageTk.PhotoImage(path)
logo = Label(tool_bar, image=image, width=60, height=60)
logo.pack(side='left', padx=50, pady=10)

# login for admin
login_image = Image.open(os.path.abspath("../resources/login.png"))
login_image = login_image.resize((150, 50), Image.LANCZOS)
login_tk = ImageTk.PhotoImage(login_image)
login = Label(tool_bar, image=login_tk, cursor="hand2")
login["bg"] = "#EDF2F4"
login["border"] = "0"
login.pack(side='right', padx=20, pady=10)

# about us
about_us_image = Image.open(os.path.abspath("../resources/about_us.png"))
about_us_image = about_us_image.resize((150, 50), Image.LANCZOS)
about_us_tk = ImageTk.PhotoImage(about_us_image)
about_us = Label(tool_bar, image=about_us_tk, cursor="hand2")
about_us["bg"] = "#EDF2F4"
about_us["border"] = "0"
about_us.pack(side='right', padx=20, pady=10)

# policy
policy_image = Image.open(os.path.abspath("../resources/policy.png"))
policy_image = policy_image.resize((150, 50), Image.LANCZOS)
policy_tk = ImageTk.PhotoImage(policy_image)
policy = Label(tool_bar, image=policy_tk, cursor="hand2")
policy["bg"] = "#EDF2F4"
policy["border"] = "0"
policy.pack(side='right', padx=20, pady=10)


# center frame
center_frame = Frame(main_frame, width=0, height=0)
center_frame.config(bg='#2B2D42')
center_frame.pack(side="top", fill=BOTH, expand=True)


def goto_exam_page(event=None):
    main_frame.destroy()
    import exam_page


main_frame.update()
label = Image.open(os.path.abspath("../resources/heading.png"))
label = label.resize((600, 200), Image.LANCZOS)
label_tk = ImageTk.PhotoImage(label)
label_image = Label(center_frame, image=label_tk, width=600)
label_image["bg"] = "#2B2D42"
label_image["border"] = "0"
label_image.pack(side="top", pady=(90, 0))


button = Image.open(os.path.abspath("../resources/start_exam.png"))
button = button.resize((400, 60), Image.LANCZOS)
start_image_tk = ImageTk.PhotoImage(button)
start_image = Label(center_frame, image=start_image_tk, cursor="hand2")
start_image["bg"] = "#2B2D42"
start_image["border"] = "0"

start_image.pack(side="top", pady=(70, 0))

start_image.bind('<Button-1>', goto_exam_page)

main_frame.update()
border = Image.open('../resources/border_bottom.png')
border = border.resize((600, 400), Image.LANCZOS)

# Convert the Image object into a TkPhoto object
border_tk = ImageTk.PhotoImage(border)

border_bottom = Label(center_frame, image=border_tk)
border_bottom["bg"] = "#2B2D42"
border_bottom["border"] = "0"
border_bottom.pack(side="bottom", anchor="sw")

main_frame.mainloop()
