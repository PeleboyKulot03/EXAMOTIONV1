from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
from tkinter import messagebox
from utils import dash_board_model
from statics import static, password_hasher, globals

model = dash_board_model.DashBoardModel()
global_var = globals.Globals()
statics = static.Statics()


def button_click_event(controller):
    dialog = ctk.CTkInputDialog(text="Type your admin password:", title="Warning for admin only!")

    password = dialog.get_input()
    if len(password) == 0:
        messagebox.showinfo("Credentials Required", "Sorry but username is a required field!")
        return

    if len(password) < 8:
        messagebox.showinfo("Invalid Credentials", "Please input valid password with length of minimum of 8")
        return

    if model.validate_admin(password_hasher.hash_password(password)):
        controller.show_frame('DashBoard')
        return

    messagebox.showinfo("Incorrect Password", "Sorry but the provided password is incorrect.")


class LandingPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        # toolbar
        tool_bar = Frame(self, width=0, height=200)
        tool_bar.config(bg="#EDF2F4")
        tool_bar.pack(fill=X, side="top")

        # components of the toolbar
        # logo
        path = Image.open("../resources/examotion_logo.png")
        path = path.resize((60, 60), Image.LANCZOS)
        image = ImageTk.PhotoImage(path)
        logo = Label(tool_bar, width=60, height=60)
        logo.pack(side='left', padx=50, pady=10)
        logo.config(image=image)
        logo.image = image

        # login for admin
        logout_image = Image.open("../resources/logout.png")
        logout_image = logout_image.resize((150, 50), Image.LANCZOS)
        logout_tk = ImageTk.PhotoImage(logout_image)
        logout = Label(tool_bar, image=logout_tk, cursor="hand2")
        logout["bg"] = "#EDF2F4"
        logout["border"] = "0"
        logout.pack(side='right', padx=20, pady=10)
        logout.image = logout_tk
        logout.bind('<Button-1>', lambda e: controller.show_frame('LoginPage'))

        # login for admin
        login_image = Image.open("../resources/dash_board.png")
        login_image = login_image.resize((150, 50), Image.LANCZOS)
        login_tk = ImageTk.PhotoImage(login_image)
        login = Label(tool_bar, image=login_tk, cursor="hand2")
        login["bg"] = "#EDF2F4"
        login["border"] = "0"
        login.pack(side='right', padx=20, pady=10)
        login.image = login_tk
        login.bind('<Button-1>', lambda e: button_click_event(controller))

        # about us
        about_us_image = Image.open("../resources/about_us.png")
        about_us_image = about_us_image.resize((150, 50), Image.LANCZOS)
        about_us_tk = ImageTk.PhotoImage(about_us_image)
        about_us = Label(tool_bar, image=about_us_tk, cursor="hand2")
        about_us["bg"] = "#EDF2F4"
        about_us["border"] = "0"
        about_us.pack(side='right', padx=20, pady=10)
        about_us.image = about_us_tk
        about_us.bind('<Button-1>', lambda e: controller.show_frame('AboutUs', data="LandingPage"))

        # policy
        policy_image = Image.open("../resources/policy.png")
        policy_image = policy_image.resize((150, 50), Image.LANCZOS)
        policy_tk = ImageTk.PhotoImage(policy_image)
        policy = Label(tool_bar, image=policy_tk, cursor="hand2")
        policy["bg"] = "#EDF2F4"
        policy["border"] = "0"
        policy.pack(side='right', padx=20, pady=10)
        policy.image = policy_tk
        policy.bind('<Button-1>', lambda e: controller.show_frame('Policy', data="LandingPage"))

        # center frame
        center_frame = Frame(self, width=0, height=0)
        center_frame.config(bg='#2B2D42')
        center_frame.pack(side="top", fill=BOTH, expand=True)

        label = Image.open("../resources/heading.png")
        label = label.resize((600, 200), Image.LANCZOS)
        label_tk = ImageTk.PhotoImage(label)
        label_image = Label(center_frame, image=label_tk, width=600)
        label_image["bg"] = "#2B2D42"
        label_image["border"] = "0"
        label_image.pack(side="top", pady=(90, 0))
        label_image.image = label_tk

        button = Image.open("../resources/start_exam.png")
        button = button.resize((400, 60), Image.LANCZOS)
        start_image_tk = ImageTk.PhotoImage(button)
        start_image = Label(center_frame, image=start_image_tk, cursor="hand2")
        start_image["bg"] = "#2B2D42"
        start_image["border"] = "0"
        start_image.pack(side="top", pady=(70, 0))
        start_image.image = start_image_tk
        start_image.bind('<Button-1>', lambda e: controller.show_frame('ExamPage'))

        border = Image.open('../resources/border_bottom.png')
        border = border.resize((600, 400), Image.LANCZOS)

        # Convert the Image object into a TkPhoto object
        border_tk = ImageTk.PhotoImage(border)

        border_bottom = Label(center_frame, image=border_tk)
        border_bottom["bg"] = "#2B2D42"
        border_bottom["border"] = "0"
        border_bottom.pack(side="bottom", anchor="sw")
        border_bottom.image = border_tk
