from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
PADX = 20
PADY = 20
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 12, "bold")



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=PADY, padx=PADX)

        self.img_true = PhotoImage(file="images/true.png")
        self.img_false = PhotoImage(file="images/false.png")

        self.lbl_progress = Label(text="Question: 1/10", bg=THEME_COLOR, foreground="white", font=SCORE_FONT)
        self.lbl_progress.grid(row=0, column=0)

        self.lbl_score = Label(text="Score: 0", bg=THEME_COLOR, foreground="white", font=SCORE_FONT)
        self.lbl_score.grid(row=0, column=1, pady=PADY, padx=PADX)

        self.canvas = Canvas(
            width=300,
            height=250,
            highlightthickness=0
        )
        self.lbl_question = self.canvas.create_text(
            150,
            125,
            width=280,
            font=QUESTION_FONT,
            text="Language",
            fill="black"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=PADY, padx=PADX, )

        self.btn_true = Button(borderwidth=0, bg=THEME_COLOR, highlightthickness=0, image=self.img_true,
                               command=self.guess_true)
        self.btn_true.grid(row=2, column=0, pady=PADY, padx=PADX)

        self.btn_false = Button(borderwidth=0, bg=THEME_COLOR, highlightthickness=0, image=self.img_false,
                                command=self.guess_false)
        self.btn_false.grid(row=2, column=1, pady=PADY, padx=PADX)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")

        if self.quiz.still_has_questions():
            self.enable_buttons()
            q_text = self.quiz.next_question()
            self.lbl_progress.config(text=f"Question: {self.quiz.question_number}/10")
            self.canvas.itemconfig(self.lbl_question, text=q_text)

        else:
            self.canvas.itemconfig(
                self.lbl_question,
                text=f"You've completed the quiz\n\nYour final score is: {self.quiz.score}/{self.quiz.question_number}",
                fill="black")

        self.lbl_score.config(text=f"Score: {self.quiz.score}")

    def disable_buttons(self):
        self.btn_true.config(state="disabled")
        self.btn_false.config(state="disabled")

    def enable_buttons(self):
        self.btn_true.config(state="active")
        self.btn_false.config(state="active")


    def guess_true(self):
        self.disable_buttons()
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def guess_false(self):
        self.disable_buttons()
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.update()
        self.window.after(1000, self.get_next_question())
