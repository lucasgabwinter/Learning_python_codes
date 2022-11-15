class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def compute_score(self, answer):
        if answer.lower() == self.question_list[self.question_number-1].answer.lower():
            self.score += 1
            print("Correct!")
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("Wrong answer.")
        print("\n")
