import tkinter as tk
import landing_page
import login_page
import dash_board
import sign_up_page
import window_setter as ws
import os
import exam_page
import show_score


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # ws.FullScreenApp(container)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (landing_page.LandingPage,
                  login_page.LoginPage,
                  dash_board.DashBoard,
                  sign_up_page.SignUp,
                  exam_page.ExamPage,
                  show_score.ShowScore):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self, )
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name, score=1, time=1, data=None):
        if page_name == "DashBoard":
            from utils import dash_board_model
            db = dash_board_model.DashBoardModel()
            for child in self.frames[page_name].scrollable_users.winfo_children():
                child.destroy()

            self.frames[page_name].users = db.get_users()
            self.frames[page_name].frequency = db.get_frequency()
            self.frames[page_name].cnns = db.get_cnn()
            self.frames[page_name].nlps = db.get_nlp()
            self.frames[page_name].create_user()
            self.frames[page_name].create_overall(None)

        elif page_name == "SignUp":
            self.frames[page_name].username.delete(0, tk.END)
            self.frames[page_name].password.delete(0, tk.END)
            self.frames[page_name].confirm_password.delete(0, tk.END)
            self.frames[page_name].username.configure(placeholder_text="Username")
            self.frames[page_name].password.configure(placeholder_text="Password")
            self.frames[page_name].confirm_password.configure(placeholder_text="Confirm Password")

        elif page_name == "LoginPage":
            self.frames[page_name].username.delete(0, tk.END)
            self.frames[page_name].password.delete(0, tk.END)
            self.frames[page_name].username.configure(placeholder_text="Username")
            self.frames[page_name].password.configure(placeholder_text="Password")

        elif page_name == "ExamPage":
            self.frames[page_name].re_enit()
            self.frames[page_name].create_frame()
            self.frames[page_name].start_camera_thread()

        elif page_name == "ShowScore":
            self.frames[page_name].score = score
            self.frames[page_name].time = time
            self.frames[page_name].data = data
            self.frames[page_name].create_frame()

        frame = self.frames[page_name]
        frame.tkraise()

    def on_close(self):
        for file in os.listdir(os.getcwd() + "\\myDir"):
            os.remove(os.path.join(os.getcwd() + "\\myDir", file))

        if not self.frames["ExamPage"].stopper:
            self.frames["ExamPage"].stopper = True
            self.frames["ExamPage"].is_destroy = True

        self.destroy()


main_frame = MainApp()
main_frame.resizable(False, False)
ws.FullScreenApp(main_frame)
main_frame.state('zoomed')

if __name__ == '__main__':
    main_frame.mainloop()
