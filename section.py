from question import Question

class Section:
    
    def __init__ (self,sec_title,sec_description,question_list, qualifying_question=None):
        
        self.sec_title = sec_title
        self.sec_description = sec_description
        self.qualifying_question = qualifying_question
        self.question_list = question_list

    # check if user answer for qualify question is yes then run the section          
    def ask_qualify_question(self):
        if self.qualifying_question:
            self.qualifying_question.ask_question()    # ask if these two will work when ask_question() and get_user_answer() are methods in Question
        return self.qualifying_question.user_answer  


# run method for each section

    def run_section(self):
        print(f'============================ {self.sec_title} ============================\n')
        print(f'{self.sec_description}\n')
        for question in self.question_list:
            question.ask_question()
            question.print_user_answer()
        for question in self.question_list:
            print(f'your answer for {question.question_text} is [{question.user_answer}] {question.user_answer_text()}')
        print('Print Thank you messgae: Thanks for your time.bala bala bala....')
    


