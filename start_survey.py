from question import Question
from section import Section
from keep_answers import answer_dictionary
from survey import Survey

def main():
# create objects of questions and sections for servey    
    qualify1 = Question('1', 'Question 1 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})
    qualify2 = Question('2', 'Question 2 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})
    qualify3 = Question('3', 'Question 3 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})

    q4 = Question('1', 'Question1 Section1 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})
    q5 = Question('2', 'Question2 Section1 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})
    q6 = Question('3', 'Question3 Section1 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})

    q7 = Question('1', 'Question1 Section2 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})
    q8 = Question('2', 'Question2 Section2 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})
    q9 = Question('3', 'Question3 Section2 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})

    q10 = Question('1', 'Question1 Section3 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})
    q11 = Question('2', 'Question2 Section3 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})
    q12 = Question('3', 'Question3 Section3 12 text? ', {'a': 'AnswerA', 'b': 'AnswerB', 'c': 'AnswerC'})

    section_a = Section('SectionA Title', 'Here is some info about what we covered in section_a', [q4, q5, q6], qualify1)
    section_b = Section('SectionB Title', 'Here is some info about what we covered in section_b', [q7, q8, q9], qualify2)
    section_c = Section('SectionC Title', 'Here is some info about what we covered in section_c', [q10, q11, q12], qualify3)
    
    my_survey = Survey('SheCodes Survey', 'This is a placeholder for Description on Survey', [section_a, section_b, section_c])
    my_survey.survey_introduction()

# start 

if __name__ == "__main__":
    main()