from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while not quiz.is_complete():
    quiz.next_question()

quiz.report()

