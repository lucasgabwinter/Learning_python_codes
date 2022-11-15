from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)


quiz_ = QuizBrain(question_bank)

while quiz_.still_has_questions():
    answer = quiz_.next_question()
    quiz_.compute_score(answer)

print(f"You completed the quiz. Your final "
      f"score is {quiz_.score} / {len(question_bank)}!")
