from tkinter import *
from statics import static, password_hasher, globals
from tkinter import messagebox
from PIL import ImageTk, Image
from utils import login_model
import customtkinter
import tempfile
import os

global_var = globals.Globals()
statics = static.Statics()
is_show = False
show_image = customtkinter.CTkImage(light_image=Image.open('../resources/show.png'), size=(40, 40))
hide_image = customtkinter.CTkImage(light_image=Image.open('../resources/hidden.png'), size=(40, 40))
banner_image = customtkinter.CTkImage(light_image=Image.open('../resources/login_banner.png'), size=(400, 400))


def validate(username, password, controller):
    if len(username.get()) == 0:
        messagebox.showinfo("Credentials Required", "Sorry but username is a required field!")
        return

    if len(password.get()) == 0:
        messagebox.showinfo("Credentials Required", "Sorry but password is a required field!")
        return

    if login_model.LoginPageModel(username.get(), password_hasher.hash_password(password.get())).login():
        # Create a temporary file and write some data to it
        for file in os.listdir(os.getcwd() + "\\myDir"):
            os.remove(os.path.join(os.getcwd() + "\\myDir", file))

        tempfile.NamedTemporaryFile(dir='myDir', suffix=f'.{username.get()}', delete=False)
        username.delete(0, END)
        password.delete(0, END)
        controller.show_frame("LandingPage")

        return
    else:
        messagebox.showinfo("Credentials Required", "Incorrect username or password!")


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # toolbar
        tool_bar = Frame(self, width=0, height=200)
        tool_bar.config(bg="#EDF2F4")
        tool_bar.pack(fill=X, side="top")

        # components of the toolbar
        # logo
        path = Image.open("../resources/examotion.png")
        image = ImageTk.PhotoImage(path)
        logo = Label(tool_bar, image=image)
        logo.pack(side='left', padx=50, pady=10)
        logo.image = image

        # about us
        about_us_image = Image.open("../resources/about_us.png")
        about_us_image = about_us_image.resize((150, 50), Image.LANCZOS)
        about_us_tk = ImageTk.PhotoImage(about_us_image)
        about_us = Label(tool_bar, image=about_us_tk, cursor="hand2")
        about_us["bg"] = "#EDF2F4"
        about_us["border"] = "0"
        about_us.pack(side='right', padx=(20, 55), pady=10)
        about_us.image = about_us_tk
        about_us.bind('<Button-1>', lambda e: controller.show_frame('AboutUs', data="LoginPage"))

        # policy
        policy_image = Image.open("../resources/policy.png")
        policy_image = policy_image.resize((150, 50), Image.LANCZOS)
        policy_tk = ImageTk.PhotoImage(policy_image)
        policy = Label(tool_bar, image=policy_tk, cursor="hand2")
        policy["bg"] = "#EDF2F4"
        policy["border"] = "0"
        policy.pack(side='right', padx=20, pady=10)
        policy.image = policy_tk
        policy.bind('<Button-1>', lambda e: controller.show_frame('Policy', data="LoginPage"))
        # center frame
        center_frame = Frame(self, width=0, height=0, padx=100, pady=50)
        center_frame.config(bg='#8D99AE')
        center_frame.pack(side="top", fill=BOTH, expand=True)

        left_frame = customtkinter.CTkFrame(center_frame, corner_radius=10, fg_color="#2B2D42")
        left_frame.pack(side='left', fill=BOTH, expand=True)

        left_frame_label = customtkinter.CTkLabel(left_frame,
                                                  text="",
                                                  image=banner_image,
                                                  fg_color="#2B2D42")

        left_frame_label.pack(side='left', fill=BOTH, expand=True, padx=(10, 0))

        right_frame = customtkinter.CTkFrame(center_frame, corner_radius=10, fg_color="#EDF2F4")
        right_frame.pack(side='left', fill=BOTH, expand=True)

        # form
        form = Frame(right_frame, bg="#EDF2F4")
        form.pack(side='top', fill=BOTH, expand=True, padx=(0, 10))

        # login text
        login_image = Image.open("../resources/login_text.png")
        login_image = login_image.resize((250, 100), Image.LANCZOS)
        login_tk = ImageTk.PhotoImage(login_image)
        login = Label(form, image=login_tk)
        login["bg"] = "#EDF2F4"
        login["border"] = "0"
        login.pack(side='top', padx=(60, 0), pady=30)
        login.image = login_tk

        username_holder = Frame(form, bg='#EDF2F4')
        username_holder.pack(side='top', anchor='w', fill=X, padx=40, pady=10)

        username_icon = Image.open("../resources/user 1.png")
        username_icon_tk = ImageTk.PhotoImage(username_icon)
        user_icon = Label(username_holder, image=username_icon_tk)
        user_icon["bg"] = "#EDF2F4"
        user_icon["border"] = "0"
        user_icon.pack(side='left', padx=(0, 20))

        username_card_holder = customtkinter.CTkFrame(username_holder, corner_radius=10, fg_color="#555580")
        username_card_holder.pack(side='left', fill=X, padx=(10, 0), expand=True)

        self.username = customtkinter.CTkEntry(username_card_holder,
                                          placeholder_text="Username",
                                          font=("Arial", 25),
                                          border_width=0,
                                          corner_radius=0,
                                          height=55)

        self.username.pack(side='left', padx=(5, 0), fill=X, expand=True)
        user_icon.image = username_icon_tk

        password_holder = Frame(form, bg='#EDF2F4')
        password_holder.pack(side='top', anchor='w', fill=X, padx=40, pady=10)
        password_icon = Image.open("../resources/padlock 1.png")
        password_icon_tk = ImageTk.PhotoImage(password_icon)
        password_icon = Label(password_holder, image=password_icon_tk)
        password_icon["bg"] = "#EDF2F4"
        password_icon["border"] = "0"
        password_icon.pack(side='left', padx=(0, 20))
        password_icon.image = password_icon_tk

        password_card_holder = customtkinter.CTkFrame(password_holder, corner_radius=10, fg_color="#555580")
        password_card_holder.pack(side='left', fill=X, padx=(10, 0), expand=True)

        self.password = customtkinter.CTkEntry(password_card_holder,
                                               placeholder_text="Password",
                                               font=("Arial", 25),
                                               border_width=0,
                                               corner_radius=0,
                                               height=55)
        self.password.configure(show='●')
        self.password.pack(side='left', padx=(5, 0), fill=X, expand=True)

        self.password_toggle = customtkinter.CTkButton(password_card_holder, width=10, text="",
                                                       corner_radius=0,
                                                       hover=False,
                                                       border_width=0,
                                                       image=show_image,
                                                       cursor="hand2",
                                                       fg_color="#F8F9FA",
                                                       command=lambda: self.toggle())
        self.password_toggle["border"] = "0"
        self.password_toggle.pack(side='left', fill=Y)
        self.password_toggle.image = is_show

        login_holder = customtkinter.CTkFrame(form, corner_radius=10, fg_color="#FAA307")
        login_holder.pack(side='top', padx=(120, 40), pady=(30, 10), fill=X)
        login = customtkinter.CTkButton(login_holder,
                                        text="LOGIN",
                                        font=("Helvetica", 25, "bold"),
                                        height=55,
                                        fg_color="white",
                                        hover_color="#c4c4c4",
                                        command=lambda: validate(self.username, self.password, controller),
                                        text_color="#000000")
        login.pack(side='top', padx=5, fill=X)

        back_to_homepage_holder = customtkinter.CTkFrame(form, corner_radius=10, fg_color="#FE3F56")
        back_to_homepage_holder.pack(side='top', padx=(120, 40), pady=10, fill=X)
        back_to_homepage = customtkinter.CTkButton(back_to_homepage_holder,
                                                   text="SIGN UP",
                                                   font=("Helvetica 18 bold", 25, "bold"),
                                                   height=55,
                                                   fg_color="white",
                                                   hover_color="#c4c4c4",
                                                   command=lambda: controller.show_frame("SignUp"),
                                                   text_color="#000000")

        back_to_homepage.pack(side='top', padx=5, fill=X)

    def toggle(self):
        global is_show
        if is_show:
            self.password_toggle.configure(image=show_image)
            self.password.configure(show='●')
            is_show = False
            return

        self.password_toggle.configure(image=hide_image)
        self.password.configure(show='')
        is_show = True
