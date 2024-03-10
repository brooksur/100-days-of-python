class QuizBrain:
    def __init__(self, questions):
        self.index = 0
        self.questions = questions
        self.answers = []

    def next_question(self):
        num = self.index + 1
        cur = self.questions[self.index]
        ans = input(f"Q.{num}: {cur.text} (True/False)? ")
        self.answers.append(1 if ans == cur.answer else 0)
        self.index += 1

    def is_complete(self):
        return len(self.questions) == len(self.answers)

    def num_correct(self):
        correct_answers = 0

        for ans in self.answers:
            correct_answers += ans

        return correct_answers

    def report(self):
        correct_answers = self.num_correct()
        perc = round(100 * (len(self.questions) / correct_answers), 2)

        print(f'Contrats! You have completed the quiz\n'
              f'Out of {len(self.questions)} questions,\n'
              f'You got {correct_answers} correct answers\n'
              f'As a percentage, this is {perc}%. Good job!')