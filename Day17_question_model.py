class Question:
    def __init__(self, text, answer):
        self.que = text
        self.ans = answer
    def ask(self):
        print(self.que)
    def check(self, input):
        if input == self.ans:
            print("You are correct!")
        else:
            print("Wrong Answer.")
    def print_data(self):
        print(f"\nQuestion: {self.que}\nAnswer: {self.ans}.")