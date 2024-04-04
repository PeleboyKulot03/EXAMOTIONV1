from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
from tkinter import messagebox
from utils import dash_board_model
from statics import static, password_hasher, globals

global_var = globals.Globals()
statics = static.Statics()
show_image = ctk.CTkImage(light_image=Image.open('../resources/show.png'), size=(40, 40))
hide_image = ctk.CTkImage(light_image=Image.open('../resources/hidden.png'), size=(40, 40))
is_show = False
ctrl = None


def button_click_event(self, controller, password):
    model = dash_board_model.DashBoardModel()
    if len(password) == 0:
        messagebox.showinfo("Credentials Required", "Sorry but password is a required field!")
        return

    if len(password) < 8:
        messagebox.showinfo("Invalid Credentials", "Please input valid password with length of minimum of 8")
        return

    if model.validate_admin(password_hasher.hash_password(password)):
        controller.show_frame('DashBoard')
        self.destroy()
        return

    messagebox.showinfo("Incorrect Password", "Sorry but the provided password is incorrect.")


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x300")
        self.configure(fg_color="#EDF2F4")

        self.login_image = Image.open("../resources/for_admin.png")
        self.login_image = self.login_image.resize((320, 80), Image.LANCZOS)
        login_tk = ImageTk.PhotoImage(self.login_image)
        self.login = Label(self, image=login_tk)
        self.login["bg"] = "#EDF2F4"
        self.login["border"] = "0"
        self.login.pack(side='top', padx=40, pady=10)
        self.login.image = login_tk

        password_holder = Frame(self, bg='#EDF2F4')
        password_holder.pack(side='top', anchor='w', fill=X, padx=40)

        password_card_holder = ctk.CTkFrame(password_holder, corner_radius=10, fg_color="#555580")
        password_card_holder.pack(side='left', fill=X, expand=True)

        self.password = ctk.CTkEntry(password_card_holder,
                                     placeholder_text="Password",
                                     font=("Arial", 25),
                                     border_width=0,
                                     corner_radius=0,
                                     height=45)
        self.password.configure(show='●')
        self.password.pack(side='left', padx=(5, 0), fill=X, expand=True)

        self.password_toggle = ctk.CTkButton(password_card_holder, width=10, text="",
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

        self.login_holder = ctk.CTkFrame(self, corner_radius=10, fg_color="#FAA307")
        self.login_holder.pack(side='top', padx=(40, 40), pady=(20, 10), fill=X)
        self.login = ctk.CTkButton(self.login_holder,
                                   text="LOGIN",
                                   font=("Helvetica", 25, "bold"),
                                   height=45,
                                   fg_color="white",
                                   hover_color="#c4c4c4",
                                   command=lambda: button_click_event(self, ctrl, self.password.get()),
                                   text_color="#000000")
        self.login.pack(side='top', padx=5, fill=X)

        self.back_to_homepage_holder = ctk.CTkFrame(self, corner_radius=10, fg_color="#FE3F56")
        self.back_to_homepage_holder.pack(side='top', padx=(40, 40), fill=X)
        self.back_to_homepage = ctk.CTkButton(self.back_to_homepage_holder,
                                              text="CANCEL",
                                              font=("Helvetica 18 bold", 25, "bold"),
                                              height=45,
                                              fg_color="white",
                                              hover_color="#c4c4c4",
                                              command=lambda: self.destroy(),
                                              text_color="#000000")

        self.back_to_homepage.pack(side='top', padx=5, fill=X)

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


class LandingPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        global ctrl
        ctrl = controller
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
        login.bind('<Button-1>', lambda e: self.open_toplevel())

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
        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)

        self.toplevel_window.focus()  # if window exists focus it
