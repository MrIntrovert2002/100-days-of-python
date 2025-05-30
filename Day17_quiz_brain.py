class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_no = 0
        self.score = 0
    def still_has_questions(self):
        return self.question_no < len(self.question_list)
    
    def next_question(self):
        user_ans = input(f"Q.{self.question_no+1}. {self.question_list[self.question_no].que}\nTrue or False: ")
        if user_ans == 'T' or user_ans == "True" or user_ans == "true" or user_ans == "t":
            user_ans = "True"
        if user_ans == 'F' or user_ans == "False" or user_ans =="false" or user_ans == "f":
            user_ans = "False"
        if user_ans == self.question_list[self.question_no].ans:
            print("Correct Answer.")
            self.score+=1
        else:
            print("Wrong answer")
        self.question_no += 1
        print(f"Your current score is {self.score}/{self.question_no}.\n")

    def end_quiz(self):
        print("You have completed the Quiz.")
        print((f"Your final score is {self.score}/{self.question_no}.\n"))

