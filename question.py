class Question:
    def __init__(self, q_number, question_text, question_answers, valid_answers=None , user_answers = None):
        self.q_number = q_number
        self.question_text = question_text
        self.question_answers = question_answers
        self.valid_answers = []
        self.user_answers = user_answers

# ask question from user
    def ask_question(self):
        print(f'{self.q_number} {self.question_text}\n')
        for answer_code, answer_text in self.question_answers.items():
            print(f'{answer_code} {answer_text}')
            self.get_user_answer()
            self.print_user_answer()
        print('\n')


# show user answer after each question : 
    def get_user_answer(self):
        #ToDo: add validator for user answer /check if code is in the valid_answers
        user_answer = input('Your answer is: ')
        return user_answer

    @property
    def user_answer_text(self):
            return self.question_answers[self.user_answers]  

    def print_user_answer(self):
        print(f'Your answer for question {self.q_number} {self.question_text} is {self.user_answers}')

          