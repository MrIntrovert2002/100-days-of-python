from Day17_question_model import Question
from Day17_data import question_data
from Day17_quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i['question'], i['correct_answer']))

Quiz = QuizBrain(question_bank)
while Quiz.still_has_questions():
    Quiz.next_question()
Quiz.end_quiz()
