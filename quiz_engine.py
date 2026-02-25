from quiz_questions import QUESTIONS # Importing the questions from quiz_questions

# Used from the iteratve assignment as basis for quiz

class QuizEngine:
    def __init__(self): # This means that it runs automatically when a new QuizEngine() object is made.
        self.questions = QUESTIONS
        self.index = 0
        self.score = 0
        self.results = [] # Keep Track of what question a user got right or wrong for results at the end.

    def current_question(self):
        return self.questions[self.index] # Return the question dictionary for the current index.

    def check_answer(self, choice_index: int) -> bool:
        question = self.current_question()
        correct_index = question["answer_index"]
        is_correct = (choice_index == correct_index)

    # Checks whether the chosen answer is correct. 
    # Records the result for the end screen. 
    # Returns True if correct, False if not.

        self.results.append((question["question"], is_correct)) # Stores a tuple: the question text and whether the user got it right.

        if is_correct:
            self.score += 1
        return is_correct # Update score if answer input is correct or not.

    def next_question(self) -> bool:

    # Moves to the next question. 
    # Returns True if another question exists, otherwise False.

        self.index += 1
        return self.index < len(self.questions)
    
    def correct_answer_text(self) -> str:
        q = self.current_question()
        return q["options"][q["answer_index"]] # This is important in helping the QUIZ_UI regognise that an answer selected in incorrect and to display the incorrect message.
    
    # If the boolean would return false e.g. no more questions then it will move the the ending_screen.

    def restart(self):
        self.index = 0
        self.score = 0
        self.results = [] # Restart the quiz and set th quiz index and user score to 0 again