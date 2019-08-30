from question import Question
from section import Section

class Survey():
# define survey parameters : title, description, sections
    def __init__(self, title, description, survey_sections):
        self.title = title
        self.description = description
        self.qualify_questions = qualify_questions
        self.survey_sections = survey_sections


    def ask_if_wants_to_continue(self):
        while True:
            user_answer = input('Do you want to continue with survey?Enter yes/no to continue. ').lower()
            # Check if answer
            if user_answer== 'yes':
                return True
            elif user_answer=='no':
                print ('Appreciate you time')
                return False
            else: 
                print ('Invalid input')
                 

    

        
    

    def survey_introduction(self):
        print(f'============================ {self.title} ============================\n')
        print(f'{self.description}\n\n')   
        if self.ask_if_wants_to_continue():
            for section in self.survey_sections:
                if section.ask_qualify_question():
                    section.run_section()
        
    
    

        

        









    