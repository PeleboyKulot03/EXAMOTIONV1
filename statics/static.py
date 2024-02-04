from PIL import Image
import os


class Statics:
    def __init__(self):
        path = os.path.abspath("../resources/examotion_logo.png")
        image_logo = Image.open(path)
        image_logo = image_logo.resize((50, 50), Image.LANCZOS)
        self.image_logo = image_logo
        self.title = "ExaMotion"
        self.about_us = "About Us"
        self.policy = "Policy"
        self.questions = [
            {
                "question": "This is a question 1",
                1: "Answer1",
                2: "Answer2",
                3: "Answer3",
                4: "Answer4",
                "correct": 1
            },
            {
                "question": "This is a question 2",
                1: "Answer1",
                2: "Answer2",
                3: "Answer3",
                4: "Answer4",
                "correct": 2
            },
            {
                "question": "This is a question 3",
                1: "Answer1",
                2: "Answer2",
                3: "Answer3",
                4: "Answer4",
                "correct": 3
            }
        ]

    def get_title(self):
        return self.title

    def get_logo(self):
        return self.image_logo

    def get_about_us(self):
        return self.about_us

    def get_policy(self):
        return self.policy

    def get_questions(self):
        return self.questions
