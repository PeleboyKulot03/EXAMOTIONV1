from tkinter import *
from PIL import ImageTk, Image
import customtkinter


class Policy(Frame):
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

        center_frame = Frame(self, bg="#2B2D42")
        center_frame.pack(fill=BOTH, side="top", expand=True)

        scrollable_frame = customtkinter.CTkScrollableFrame(center_frame, corner_radius=10, fg_color="#EDF2F4")
        scrollable_frame.pack(fill=BOTH, side='top', expand=True, padx=50, pady=80)

        (Label(scrollable_frame, text="Privacy Policy", fg='black', bg='#EDF2F4', font=("Verdana", 32, 'bold'))
         .grid(column=0, row=0, pady=40, sticky='ew'))

        Label(scrollable_frame,
              text="User Registration and Data Usage Policy",
              fg='black',
              bg='#EDF2F4',
              font=("Verdana", 20, 'bold'),
              justify=LEFT).grid(column=0, row=1, sticky='w', padx=10, pady=(0, 10))
        scrollable_frame.update()
        width = scrollable_frame.winfo_width() - 50

        Label(scrollable_frame,
              text="Welcome to ExaMotion! Before you proceed with your registration, please take a moment to review our "
                   "User Registration and Data Usage Policy. By registering on our platform, you agree to the terms outlined below.",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 18),
              justify=LEFT).grid(column=0, row=2, sticky='w', padx=40, pady=10)

        Label(scrollable_frame,
              text="Data Collected:",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 20, 'bold'),
              justify=LEFT).grid(column=0, row=3, sticky='w', padx=10, pady=10)
        Label(scrollable_frame,
              text="During the registration process, we collect the following information:",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 18),
              justify=LEFT).grid(column=0, row=4, sticky='w', padx=40, pady=10)

        Label(scrollable_frame,
              text="1. Name\n"
                   "2. Birthday\n"
                   "3. Gender\n"
                   "4. City\n"
                   "5. Picture\n"
                   "6. Email",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 18),
              justify=LEFT).grid(column=0, row=5, sticky='w', padx=80, pady=10)

        Label(scrollable_frame,
              text="Purpose of Data Collection:",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 20, 'bold'),
              justify=LEFT).grid(column=0, row=6, sticky='w', padx=10, pady=10)

        Label(scrollable_frame,
              text="The main purpose of collecting this data is to enhance the user experience and improve our system's"
                   " functionality. Additionally, we use the camera for emotion capturing during examinations. This process"
                   " helps us understand the level of difficulty a student may experience during the examination",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 18),
              justify=LEFT).grid(column=0, row=7, sticky='w', padx=40, pady=10)

        Label(scrollable_frame,
              text="Why Do We Need This Data and How We Use Your Data?",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 20, 'bold'),
              justify=LEFT).grid(column=0, row=8, sticky='w', padx=10, pady=10)

        Label(scrollable_frame,
              text="Your data is needed and used for the following purposes:\n"
                   "\nCommunication: We may use your email address to send important announcements, updates, and notifications related to your account and system usage."
                   "\n\nPersonalization: Your name, gender, and city information may be used to personalize your experience on our platform, tailoring content to your preferences."
                   "\n\nEmotion Capturing: The camera may be used during examinations to capture facial expressions for the purpose of analyzing and understanding the difficulty level a student may be facing. This information is used to improve our examination system and enhance the overall learning experience."
                   "\n\nData Security: We are committed to ensuring the security and confidentiality of your data. All collected data is stored securely, and access is restricted to authorized personnel only. We employ industry-standard measures to protect your information from unauthorized access, disclosure, alteration, and destruction."
                   "\n\nSharing Your Data: We do not sell or rent your personal information to third parties.",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 18),
              justify=LEFT).grid(column=0, row=9, sticky='w', padx=40, pady=10)

        Label(scrollable_frame,
              text="Changes to the Policy:",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 20, 'bold'),
              justify=LEFT).grid(column=0, row=10, sticky='w', padx=10, pady=10)

        Label(scrollable_frame,
              text="We reserve the right to update and modify this policy. Any changes will be communicated to you through the email address provided during registration."
                   "\n\nIf you have any questions or concerns regarding this policy, please contact us at diaz.rj.bscs@gmail.com, guarin.ra.bscs@gmail.com, julian.s.bscs@gmail.com, and pangan.j.bscs@gmail.com",
              fg='black',
              bg='#EDF2F4',
              wraplength=width * 2,
              font=("Verdana", 18),
              justify=LEFT).grid(column=0, row=11, sticky='w', padx=40, pady=10)
        scrollable_frame.columnconfigure(0, weight=1)

