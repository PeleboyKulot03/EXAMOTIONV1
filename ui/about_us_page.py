from tkinter import *
from PIL import ImageTk, Image
import customtkinter


class AboutUs(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.go_to = None
        # toolbar
        tool_bar = Frame(self, width=0)
        tool_bar.config(bg="#EDF2F4")
        tool_bar.pack(fill=X, side="top")

        # components of the toolbar

        # back button
        path = Image.open("../resources/back.png")
        path = path.resize((50, 50), Image.LANCZOS)
        image = ImageTk.PhotoImage(path)
        logo = Label(tool_bar, image=image, cursor='hand2')
        logo.pack(side='left', padx=50, pady=10)
        logo.bind('<Button-1>', lambda e: controller.show_frame(self.go_to))
        logo.image = image

        # banner
        logout_image = Image.open("../resources/about_us_text.png")
        logout_tk = ImageTk.PhotoImage(logout_image)
        logout = Label(tool_bar, image=logout_tk)
        logout["bg"] = "#EDF2F4"
        logout["border"] = "0"
        logout.pack(side='right', padx=40, pady=30, fill=X, expand=True)
        logout.image = logout_tk

        center_frame = customtkinter.CTkScrollableFrame(self, corner_radius=0, fg_color="#2B2D42")
        center_frame.pack(fill=BOTH, side="top", expand=True)

        frame_holder = Frame(center_frame, bg='#2B2D42')
        frame_holder.grid(column=0, row=0, sticky='nsew', padx=(80, 0), pady=(40, 10))
        Label(frame_holder, bg='#2B2D42', wraplength=600, fg='#FAA307', text="Hello, I am Rose Ann Guarin!",
              font=('Helvetica', 32, 'bold')).grid(column=0, row=0, sticky='sw', pady=(0, 10))
        Label(frame_holder, wraplength=600,
              text="I am currently a 4th year, Bachelors of Science in Computer Science student at Eulogio 'Amang' Rodriguez Institute of Science and Technology and an aspiring front end developer."
                   " I'm current 21 years old and I love doing arts and watching korean drama in my free time."
                   "\n\nHere are the list of technologies I've work with:"
                   "\nHTML, CSS, Java Script, Java, Python, C++, C, Figma",
              font=('Times New Roman', 20),
              bg='#2B2D42',
              justify=LEFT,
              foreground='white').grid(column=0, row=1, sticky='nw')
        frame_holder.rowconfigure(0, weight=1)
        frame_holder.rowconfigure(1, weight=1)

        rosy_image = Image.open("../resources/rosy.png")
        rosy_image = rosy_image.resize((500, 500), Image.LANCZOS)
        rosy_tk = ImageTk.PhotoImage(rosy_image)
        customtkinter.CTkLabel(center_frame, text='', corner_radius=10, image=rosy_tk, fg_color="#2B2D42").grid(
            column=1, row=0,
            sticky='nsew', padx=20,
            pady=(40, 0))

        frame_holder = Frame(center_frame, bg='#2B2D42')
        frame_holder.grid(column=1, row=1, sticky='nsew', padx=(0, 80), pady=(40, 10))
        Label(frame_holder, bg='#2B2D42', foreground='#FAA307',
              text="Hello, I am Shaira May Julian!",
              justify=RIGHT,
              font=('Helvetica', 32, 'bold')).grid(column=0, row=0, sticky='se', pady=(0, 10))
        Label(frame_holder, wraplength=600,
              text="I live in taguig city. 21 yrs of age 4th yr college student of EARIST manila.",
              font=('Times New Roman', 22),
              bg='#2B2D42', foreground='white', justify=RIGHT).grid(column=0, row=1, sticky='ne')

        frame_holder.rowconfigure(0, weight=1)
        frame_holder.rowconfigure(1, weight=1)

        julian_image = Image.open("../resources/julian.png")
        julian_image = julian_image.resize((500, 500), Image.LANCZOS)
        rosy_tk = ImageTk.PhotoImage(julian_image)
        customtkinter.CTkLabel(center_frame, text='', corner_radius=10, image=rosy_tk, fg_color="#2B2D42").grid(
            column=0, row=1,
            sticky='nsew', padx=20,
            pady=0)

        frame_holder = Frame(center_frame, bg='#2B2D42')
        frame_holder.grid(column=0, row=2, sticky='nsew', padx=(80, 0), pady=(40, 10))
        Label(frame_holder, bg='#2B2D42', fg='#FAA307', justify=LEFT,
              text="Hello, I am Jessica Pangan!",
              font=('Helvetica', 32, 'bold')).grid(column=0, row=0, sticky='sw', pady=(0, 10))
        Label(frame_holder, wraplength=600,
              padx=0,
              text="I am 22 years old. I currently reside in Western Bicutan, Taguig City. I am a fourth-year college student at EARIST Manila.",
              font=('Times New Roman', 22),
              bg='#2B2D42', fg='white', justify=LEFT).grid(column=0, row=1, sticky='nw')
        frame_holder.rowconfigure(0, weight=1)
        frame_holder.rowconfigure(1, weight=1)
        frame_holder.columnconfigure(0, weight=1)

        jes_image = Image.open("../resources/jes.png")
        jes_image = jes_image.resize((500, 500), Image.LANCZOS)
        rosy_tk = ImageTk.PhotoImage(jes_image)
        customtkinter.CTkLabel(center_frame, text='', corner_radius=10, image=rosy_tk, fg_color="#2B2D42").grid(
            column=1, row=2,
            sticky='nsew', padx=20,
            pady=0)

        diaz_image = Image.open("../resources/unknown.png")
        diaz_image = diaz_image.resize((500, 500), Image.LANCZOS)
        rosy_tk = ImageTk.PhotoImage(diaz_image)
        customtkinter.CTkLabel(center_frame, text='', corner_radius=10, image=rosy_tk, fg_color="#2B2D42").grid(
            column=0, row=3,
            sticky='nsew', padx=20,
            pady=0)

        frame_holder = Frame(center_frame, bg='#2B2D42')
        frame_holder.grid(column=1, row=3, sticky='nsew', padx=(0, 80), pady=(40, 10))
        Label(frame_holder, bg='#2B2D42', fg='#FAA307', justify=RIGHT,
              text="Hello, I am Richard Julius Diaz!",
              font=('Helvetica', 32, 'bold')).grid(column=0, row=0, sticky='se', pady=(0, 10))
        Label(frame_holder, wraplength=600,
              text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                   " Ultrices tincidunt arcu non sodales neque sodales ut etiam sit. Diam phasellus vestibulum lorem sed."
                   " Mattis vulputate enim nulla aliquet porttitor lacus luctus. Laoreet suspendisse interdum consectetur libero."
                   " Mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan. Semper viverra nam libero justo laoreet sit amet cursus."
                   " Purus sit amet volutpat consequat mauris nunc congue nisi vitae. Sem fringilla ut morbi tincidunt augue.",
              font=('Times New Roman', 22),
              bg='#2B2D42', fg='white', justify=RIGHT).grid(column=0, row=1, sticky='ne')
        frame_holder.rowconfigure(0, weight=1)
        frame_holder.rowconfigure(1, weight=1)

        center_frame.columnconfigure(0, weight=2)
        center_frame.columnconfigure(1, weight=1)
