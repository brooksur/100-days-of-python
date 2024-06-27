from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizlet')
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        for row in range(3):
            self.window.grid_rowconfigure(row, weight=1)
        for col in range(2):
            self.window.grid_columnconfigure(col, weight=1)

        # Render text (score) at 0,1
        self.score_label = Label(fg='white', bg=THEME_COLOR, text="Score: 0", font=('Arial', 12))
        self.score_label.grid(row=0, column=1, sticky='nsew')

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Some Question Text", fill=THEME_COLOR, font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
