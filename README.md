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

https://github.com/EllNul/Python-Quiz-for-AE2/blob/main/Images/Code%20Design.png


This includes

start_screen.py

Quiz_ui.py

ending_screen.py

I need somewhere to store my questions as I would like to seperate each individual element of my quiz code to make it more managable if changes are needed.
My message box alerts, testing, the quiz engine that keeps track of the scoreing, something to keep track of the results and one more file to bring everything together.

quiz_questions.py

messages.py

test.quiz.py

quiz_engine.py

results.py

quiz_app.py

for nine files in total.

QUESTIONS = [
{
        "question": "Which language is used to build Tkinter GUIs?",
        "options": ["Java", "C#", "Python", "Go"],
        "answer_index": 2},
{





