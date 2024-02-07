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
                "question": "1. In C++, a _______ is a named location in memory that holds a value.",
                1: "A. Variable",
                2: "B. Function",
                3: "C. Array ",
                4: "D. Class",
                "correct": 2
            },
            {
                "question": "2. The ________ object is used to display output to the console, and cin is used to receive input from the user.",
                1: "A. file",
                2: "B. data type",
                3: "C. function",
                4: "D. cout",
                "correct": 4
            },
            # {
            #     "question": "3. The ___________ of a variable determines the kind of values it can hold and the operations that can be performed on it.",
            #     1: "A. Scope",
            #     2: "B. Data type ",
            #     3: "C. Declaration",
            #     4: "D. Assignment",
            #     "correct": 2
            # },
            # {
            #     "question": "4. The ______ statement is used for conditional execution of code based on a specified condition.",
            #     1: "A. if",
            #     2: "B. switch",
            #     3: "C. loop",
            #     4: "D. function",
            #     "correct": 1
            # },
            # {
            #     "question": "5. The _____ loop is used to execute a block of code repeatedly for a specified number of times.",
            #     1: "A. while",
            #     2: "B. do-while",
            #     3: "C. for",
            #     4: "D. switch",
            #     "correct": 3
            # },
            # {
            #     "question": "6. The _______ statement allows you to choose between several "
            #                 "\nalternatives based on the value of a variable.",
            #     1: "A. if",
            #     2: "B. for",
            #     3: "C. switch",
            #     4: "D. while",
            #     "correct": 3
            # },
            # {
            #     "question": "7.	In C++, __________ is not a fundamental data type.",
            #     1: "A. int",
            #     2: "B. float",
            #     3: "C. string",
            #     4: "D. char",
            #     "correct": 3
            # },
            # {
            #     "question": "8.	In C++, the 'new' operator is used for _________.",
            #     1: "A. Allocate memory for an object",
            #     2: "B. Deallocate memory for an object",
            #     3: "C. Create a new instance of a class",
            #     4: "D. Initialize a variable",
            #     "correct": 1
            # },
            # {
            #     "question": "9. In C++, the correct way to include the"
            #                 "\n input-output stream header file is _________.",
            #     1: "A. #include <stdio.h>",
            #     2: "B. #include <iostream>",
            #     3: "C. #include <io.h>",
            #     4: "D. #include <stdlib.h>",
            #     "correct": 2
            # },
            # {
            #     "question": "10. In C++, to declare a pointer, you use the syntax _________.",
            #     1: "A. pointer myPointer;",
            #     2: "B. ptr myPointer;",
            #     3: "C. #define myPointer*",
            #     4: "D. int *myPointer;",
            #     "correct": 4
            # },
            # {
            #     "question": "11. In C++, what is the difference between function overloading and function overriding? ",
            #     1: "A. Overriding allows multiple functions with"
            #        "\n the same name in the same scope, "
            #        "\nwhile overloading is for derived classes "
            #        "\nreplacing base class functions.",
            #     2: "B. Overloading allows multiple functions"
            #        "\n with the same name in the same scope,"
            #        "\n while overriding is for derived classes "
            #        "\nreplacing base class functions.",
            #     3: "C. Both are the same; they are used interchangeably.",
            #     4: "D. Overloading and overriding are not allowed in C++.",
            #     "correct": 2
            # },
            # {
            #     "question": "12. In C++, what does the int main() function represent?",
            #     1: "A. A loop for iterating over a sequence",
            #     2: "B. A function for mathematical calculations",
            #     3: "C. The entry point of a C++ program",
            #     4: "D. A method for printing messages to the console",
            #     "correct": 3
            # },
            # {
            #     "question": "13. Which of the following is the correct way to declare a variable in C++?",
            #     1: "A. variable x;",
            #     2: "B. int x;",
            #     3: "C. x = int;",
            #     4: "D. declare x as int;",
            #     "correct": 2
            # },
            # {
            #     "question": "14. What is the purpose of the cin object in C++?",
            #     1: "A. To output data to the console",
            #     2: "B. To handle file input",
            #     3: "C. To read input from the user",
            #     4: "D. To declare a constant variable",
            #     "correct": 3
            # },
            # {
            #     "question": "15. Which of the following is the correct syntax for a for loop in C++?",
            #     1: "A. for i = 0; i < 10; i++",
            #     2: "B. loop (i = 0; i < 10; i++)",
            #     3: "C. for (int i = 0; i < 10; i++)",
            #     4: "D. repeat (int i = 0; i < 10; i++)",
            #     "correct": 3
            # },
            # {
            #     "question": "16. What does the nullptr keyword represent in C++?",
            #     1: "A. A keyword used to define a null variable",
            #     2: "B. An alias for the ‘NULL’ keyword in C",
            #     3: "C. A constant representing zero",
            #     4: "D. A modern replacement for ‘NULL’ in C++11 and later",
            #     "correct": 4
            # },
            # {
            #     "question": "17. What is C++?",
            #     1: "A. C++ is an object oriented programming language",
            #     2: "B. C++ is a procedural programming language",
            #     3: "C. C++ supports both procedural and object oriented programming language",
            #     4: "D. C++ is a functional programming language",
            #     "correct": 3
            # },
            # {
            #     "question": "18. Which of the following is the "
            #                 "\ncorrect syntax of including a user defined header files in C++?",
            #     1: "A. #include [userdefined]",
            #     2: "B. #include “userdefined”",
            #     3: "C. #include <userdefined.h>",
            #     4: "D. #include <userdefined>",
            #     "correct": 2
            # },
            # {
            #     "question": "19. Which of the following is used for comments in C++? ",
            #     1: "A. /* comment */",
            #     2: "B. // comment */",
            #     3: "C. // comment",
            #     4: "D. both // comment or /* comment */",
            #     "correct": 4
            # },
            # {
            #     "question": "20. Which of the following is used for comments in C++? ",
            #     1: "A. VAR_1234",
            #     2: "B. $var_name",
            #     3: "C. 7VARNAME",
            #     4: "D. 7var_name",
            #     "correct": 1
            # }
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
