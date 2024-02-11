import tkinter as tk
import landing_page
import login_page
import dash_board
import sign_up_page
import window_setter as ws
import os


def on_close():
    for file in os.listdir(os.getcwd() + "\\myDir"):
        os.remove(os.path.join(os.getcwd() + "\\myDir", file))

    main_frame.destroy()


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        # ws.FullScreenApp(container)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (landing_page.LandingPage, login_page.LoginPage, dash_board.DashBoard, sign_up_page.SignUp):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self, )
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        if page_name == "DashBoard":
            from utils import dash_board_model
            db = dash_board_model.DashBoardModel()
            self.frames[page_name].users = db.get_users()
            self.frames[page_name].frequency = db.get_frequency()
            self.frames[page_name].cnns = db.get_cnn()
            self.frames[page_name].nlps = db.get_nlp()
            self.frames[page_name].create_user()
            self.frames[page_name].create_overall(None)
            frame = self.frames[page_name]

        elif page_name == "SignUp":
            self.frames[page_name].username.delete(0, tk.END)
            self.frames[page_name].password.delete(0, tk.END)
            self.frames[page_name].confirm_password.delete(0, tk.END)
            self.frames[page_name].username.configure(placeholder_text="Username")
            self.frames[page_name].password.configure(placeholder_text="Password")
            self.frames[page_name].confirm_password.configure(placeholder_text="Confirm Password")
            frame = self.frames[page_name]

        elif page_name == "LoginPage":
            self.frames[page_name].username.delete(0, tk.END)
            self.frames[page_name].password.delete(0, tk.END)
            self.frames[page_name].username.configure(placeholder_text="Username")
            self.frames[page_name].password.configure(placeholder_text="Password")

            frame = self.frames[page_name]

        else:
            frame = self.frames[page_name]

        frame.tkraise()


main_frame = MainApp()
main_frame.resizable(False, False)
ws.FullScreenApp(main_frame)
main_frame.state('zoomed')
main_frame.protocol("WM_DELETE_WINDOW", on_close)

if __name__ == '__main__':
    main_frame.mainloop()
