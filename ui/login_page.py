from tkinter import *
from statics import static
import window_setter as ws
import customtkinter

statics = static.Statics()

main_frame = Tk()
main_frame.resizable(False, False)
main_frame.config(bg='#2B2D42')
ws.FullScreenApp(main_frame)
main_frame.state('zoomed')


center_frame = customtkinter.CTkFrame(main_frame, fg_color="#8D99AE")
center_frame.pack(side='top', expand=True, fill=X, padx=300)

username_label = customtkinter.CTkLabel(center_frame, text="Username", font=("Arial", 25))
username_label.pack(side='top', anchor='w', padx=100, pady=10)

username = customtkinter.CTkEntry(center_frame,
                                  placeholder_text="CTkEntry",
                                  font=("Arial", 25),
                                  height=50,
                                  corner_radius=20)

username.pack(side='top', padx=100, pady=(0, 10), fill=X)

password_label = customtkinter.CTkLabel(center_frame, text="Password", font=("Arial", 25))
password_label.pack(side='top', anchor='w', padx=100, pady=10)

password = customtkinter.CTkEntry(center_frame,
                                  placeholder_text="CTkEntry",
                                  font=("Arial", 25),
                                  height=50,
                                  corner_radius=20)

password.pack(side='top', padx=100, pady=(0, 10), fill=X)

login = customtkinter.CTkButton(center_frame, text="Login", font=("Arial", 25), height=50)
login.pack(side='top', padx=100, pady=10, fill=X)

main_frame.mainloop()
