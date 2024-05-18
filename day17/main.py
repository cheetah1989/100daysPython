from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank= []
for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_Question = Question(question_text,question_answer)
    question_bank.append(new_Question)


score = 0 


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"Quiz Completed \n Final Scopre is : {quiz.score} / {quiz.question_number}")