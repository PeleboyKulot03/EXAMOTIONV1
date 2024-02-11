import tkinter as tk
import window_setter as ws
from PIL import ImageTk, Image
import landing_page, login_page


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        # ws.FullScreenApp(container)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (landing_page.LandingPage, login_page.LoginPage, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class LandingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # toolbar
        tool_bar = tk.Frame(self, width=0, height=200)
        tool_bar.config(bg="black")
        tool_bar.pack(fill=tk.X, side="top")

        # components of the toolbar
        # logo
        path = Image.open("../resources/examotion_logo.png")
        path = path.resize((60, 60), Image.LANCZOS)
        image = ImageTk.PhotoImage(path)
        logo = tk.Label(tool_bar, width=60, height=60)
        logo.pack(side='left', padx=50, pady=10)
        logo.config(image=image)
        logo.image = image

        # login for admin
        login_image = Image.open("../resources/login.png")
        login_image = login_image.resize((150, 50), Image.LANCZOS)
        login_tk = ImageTk.PhotoImage(login_image)
        login = tk.Label(tool_bar, image=login_tk, cursor="hand2")
        # login["bg"] = "#EDF2F4"
        login["border"] = "0"
        login.pack(side='right', padx=20, pady=10)
        # login.bind('<Button-1>', go_to_login)

        # about us
        about_us_image = Image.open("../resources/about_us.png")
        about_us_image = about_us_image.resize((150, 50), Image.LANCZOS)
        about_us_tk = ImageTk.PhotoImage(about_us_image)
        about_us = tk.Label(tool_bar, image=about_us_tk, cursor="hand2")
        about_us["bg"] = "#EDF2F4"
        about_us["border"] = "0"
        about_us.pack(side='right', padx=20, pady=10)

        # policy
        policy_image = Image.open("../resources/policy.png")
        policy_image = policy_image.resize((150, 50), Image.LANCZOS)
        policy_tk = ImageTk.PhotoImage(policy_image)
        policy = tk.Label(tool_bar, image=policy_tk, cursor="hand2")
        policy["bg"] = "#EDF2F4"
        policy["border"] = "0"
        policy.pack(side='right', padx=20, pady=10)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


main_frame = SampleApp()
main_frame.resizable(False, False)
ws.FullScreenApp(main_frame)
main_frame.state('zoomed')
main_frame.mainloop()
