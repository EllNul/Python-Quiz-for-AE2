# Python-Quiz-for-Summative-AE2

## Introdcution

This is a databricks quiz and is a minimal viable product (MVP) developed for new users of databricks to test their knowledge around data modelling, the medallion architecture and other data analyst themed questions tailored to power BI developers. Part of work within the data side of Department for Education has been migrating SQL code and data within warehouse server databases to a much more modern online data store facility such as databricks that stores loud-based data within a Lakehouse architecture. This quiz has been developed to help beginner data modelers and power BI developers bridge this transition and also highlight area of improvement and knowledge gaps they might have.

The databricks quiz is a Python and Tkinter based application that consists of 15 multiple choice questions and also collects the usernames of those who have completed the quiz and the score they got. This data is stored on a local CSV file in the format of “Name”, “Score”, “Total”, “Percent”, and “Timestamp”.

These bits of information are useful to indicate which users might need some more support or time focused to learning and development to help with this transition. The quiz itself should take no longer than 15mins to complete and provide a simple solutions to help managers have a better understanding of their team’s confidence with databricks and data modelling. 

## Design

The layout of the quiz and user journey includes 3 main screens: 
-	The start screen is where the user will input their name which their score will be stored against at the end, a basic description of the theme of the quiz, and a button at the bottom which will start the quiz and go to the next screen.
-	The main quiz screen, this will consist of the 15 multiple choice questions with 4 options for each question to choose from.  Each answer will provide a pop up that says if you got the questions correct or incorrect as well as an explanation of the answer. There is also a submit and next question button at the bottom of this page too.
-	Once all questions have been answered the ending screen will appear and give you your total score and a breakdown of each questions results as well as another button if the user wishes to take the quiz again (restart).

I wanted the style of the quiz to also match the look of databricks.

<p align="center">
<img width="691" height="262" alt="image" src="https://github.com/user-attachments/assets/273cc40d-44fd-4934-95a4-d7dd5dde677a" />
</p>

This is an image of what the main home screen looks like as well as my comments relating to the colour palette which will be the main way for users to have that familiarity with the quiz and  databricks. I then pulled each colour into a colour palette and designed the wireframe of the quiz application.

<p align="center">
<img width="197" height="278" alt="image" src="https://github.com/user-attachments/assets/9b50ed3c-d2b7-427a-afe6-359bae1cb5b6" />
</p>


The image below represent a baseline for the visual appearance of the quiz and well as showcasing the navigational flow for users and planned screen layouts matching the colour palette shown above.

<p align="center">
<img width="781" height="215" alt="image" src="https://github.com/user-attachments/assets/8e9290d8-7505-4bbb-9537-887366f6872b" />
</p>

## Functional Requirements
<img width="600" alt="image" src="https://github.com/user-attachments/assets/e9cfb728-6bba-4ddf-96e0-957d28cefc61" />

## Non Functional Requirements
<img width="1174" height="678" alt="image" src="https://github.com/user-attachments/assets/a33d82ce-1a2d-42bc-b18c-f6adb8f4b0f5" />


-	Font size must be accessible
-	Message box to show  “incorrect” or “correct”
-	Message box to show  answer explanation
-	Message box to show answer must be selected before next question
-	Name input error handling 
-	Restart Button

### Tech Stack Outline
-	[Python 3](https://docs.python.org/3/) — core programming language
-	[Tkinter](https://docs.python.org/3/library/tkinter.html) — desktop graphical user interface
-	[csv](https://docs.python.org/3/library/csv.html) — local data storage in CSV format
-	[re](https://docs.python.org/3/library/re.html) — regular expressions for input validation
-	[datetime](https://docs.python.org/3/library/datetime.html) — timestamp generation
-	[unittest](https://docs.python.org/3/library/unittest.html) — automated unit testing
-	[Path](https://docs.python.org/3/library/pathlib.html)  — where the results will be stored
-	[Message box](https://docs.python.org/3/library/tkinter.messagebox.html) — message window visual

## Code Design
<p align="center">
<img width="1113" height="760" alt="image" src="https://github.com/user-attachments/assets/cd259829-98d2-461e-936f-7d6dd175646b" />
</p>
Here is the code design I made in <a href="https://app.diagrams.net/">draw.io</a>. This showcases the 9 different files that will be present within the code. They consist of:

- Quiz Engine – Code that manages everything that isn’t the user interface (UI) such as keeping track of the score, pulling the questions, question index, question explanations and checking if the selected answer is correct.
- Quiz App – Links all the UI elements and Quiz Engine together, this is also where you run the main quiz application. (run this bit of code and it will run the entire quiz)

#### All the Tkinter graphical code:
- Quiz UI – This is the main graphical interface and is responsible for overall design of each page, it also creates the start and end pages to switch between the three different views. It interacts with the quiz engine through the quiz app as well as any pop-up messages.
- Start screen – All the graphics for the start screen, also including some error handling for the username.
- Ending screen – Graphics for ending page that showcases the users score and if they would like to restart the quiz.

#### Extras
- Messages – All the pop-up messages for correct or incorrect answers including errors.
- Quiz Questions – All the questions, options, answers and explanations.
- Test Quiz – This includes all the unittest scripts that specifically targets the quiz engine testing for bugs/ errors in the scoring, switching question, incorrect/ correct answers etc.
- Tk.Tk – This provides all the support the for Tkinter module. Code that uses or is connected to Tkinter must call on this through root.tk to become the main application window and is connected to Quiz UI, Start screen, End screen, and the quiz engine.

## Development and Testing

#### First Developing the quiz engine

The QuizEngine is an object‑oriented Python class that acts as the core logic layer for the quiz application. The main responcibilities of this code is managing the current quiz state by: tracking user progress, verifying answers, and preparing data for the UI layer. This is utalising OOP principles such as encapsulation to build the fields and user attributes, state management to hold and update these attribute values such as score, and method‑driven interactions so that things such as score are only updated when check_answer runs.

The constructor (__init__) automatically runs when creating a new QuizEngine object.
It sets up the quiz’s internal state, including the question list, index tracking, score counter, and answer history.

```python
class QuizEngine:
    def __init__(self):  # This means that it runs automatically when a new QuizEngine() object is made.
        self.questions = QUESTIONS
        self.index = 0
        self.score = 0
        self.results = []  # Keep Track of what question a user got right or wrong for results at the end.
```

#### Answer Checking
This method verifies if the user's choice is correct, updates the score, and records the result.

```python
def check_answer(self, choice_index: int) -> bool:
    question = self.current_question()
    correct_index = question["answer_index"]
    is_correct = (choice_index == correct_index)

    self.results.append((question["question"], is_correct))

    if is_correct:
        self.score += 1
    return is_correct
```
This section of the code pulls from another file called quiz questions. 
Quiz Questions is layed out in a way where it supplies the question, options, answer in the form of an answer_index as well as an explaination which contains the reasoning behind the answers.
It is formatted like the example below.
```python
QUESTIONS = [
{
"question": "Q1: In Databricks, which layer should data analysts generally query for reporting?",
"options": ["Bronze", "Silver", "Gold", "Raw"],   
        "answer_index": 2,
        "explanation": "Gold contains curated, business-ready tables (facts/dimensions) designed for analytics and BI consumption."
},
```

#### Moving to the next question
This controls the progression of the quiz, it does this by utalising the quiz index to check if there is another question.
This also helps as part of the UI will want to know if there is any more questions, if the boolian is set to false it will move to the ending screen.

```python
    def next_question(self) -> bool:

    # Moves to the next question. 
    # Returns True if another question exists, otherwise False.

        self.index += 1
        return self.index < len(self.questions)
```
#### Restart option

An option to restart the quiz, setting the index, score to 0 and clearing all the results. (Replay feature without having to close the app)

```python
    def restart(self):
        self.index = 0
        self.score = 0
        self.results = [] # Restart the quiz and set th quiz index and user score to 0 again
```
## Engine Testing using Test Driven Development (TDD)

While building the engine, at the same time I also built the testing script so that any continusous intergation(CI) within the engine was also matched with test driven development (TDD). Test Driven development is used here to make sure that the porject itself behaves as it is supposed to throughout development, this mean that I can make changes to the engine and the questions without the worry of regression (when one fix breaks another element accidently). The test that are carried out include:

#### Smoke Test
```python
class TestSmoke(unittest.TestCase):

    def test_unittest_runs(self):
        self.assertTrue(True) # True is always true so should always pass

    def test_questions_load(self):
        self.assertGreater(len(QUESTIONS), 0) # Make sure that questions is imported correctly, file isn't empty or broken
```
For testing I used a module called unittest, the smoke test is designed to make sure unittest framework itself is working before running any real tests. This helps identify any environmental errors such as problems with running python within visual studio code or any broken file paths. Here the basic tests include: Testing that True is True (which should always pass) as well as if the questions are being imported correctly which creates a reliable starting point for the test driven development.

#### Testing quiz engine
```python
class TestQuizEngine(unittest.TestCase): # Testing the quiz engine
    def setUp(self):
        self.engine = QuizEngine() # Creates fresh engine, dosen't interfere with other tests

    def test_initial_state(self):
        self.assertEqual(self.engine.index, 0)
        self.assertEqual(self.engine.score, 0)
        self.assertEqual(self.engine.results, []) 
```
#### Testing correct answers

```python
def test_correct_answer_increments_score(self):
    q = self.engine.current_question()
    correct = q["answer_index"]

    result = self.engine.check_answer(correct)

    self.assertTrue(result)
    self.assertEqual(self.engine.score, 1)
    self.assertEqual(len(self.engine.results), 1)
```
#### Testing incorrect answers
```python
def test_incorrect_answer_does_not_increment_score(self):
    q = self.engine.current_question()
    wrong = (q["answer_index"] + 1) % len(q["options"])

    result = self.engine.check_answer(wrong)

    self.assertFalse(result)
    self.assertEqual(self.engine.score, 0)
    self.assertEqual(len(self.engine.results), 1)
```
#### Testing Restart
```python
def test_restart_resets(self):
    self.engine.check_answer(self.engine.current_question()["answer_index"])
    self.engine.next_question()
    self.engine.restart()

    self.assertEqual(self.engine.index, 0)
    self.assertEqual(self.engine.score, 0)
    self.assertEqual(self.engine.results, [])
```

