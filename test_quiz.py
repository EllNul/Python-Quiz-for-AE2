import unittest # Importing the unittest module which I will use for testing
from unittest.mock import patch # For mock testing, used to simulate the pop up windows etc

from quiz_engine import QuizEngine # Importing from quiz_engine for testing
from quiz_questions import QUESTIONS # Importing from quiz_questions testing


class TestSmoke(unittest.TestCase): # Smoke test to make sure that unittest is working (testing the tes)

    def test_unittest_runs(self):
        self.assertTrue(True) # True is always true so should always pass

    def test_questions_load(self):
        self.assertGreater(len(QUESTIONS), 0) # Make sure that questions is imported correctly, file its empty or broken

class TestQuizEngine(unittest.TestCase): # Testing the quiz engine

    def setUp(self):
        self.engine = QuizEngine() # Creates fresh engine, dosen't interfere with other tests

    def test_initial_state(self):
        self.assertEqual(self.engine.index, 0)
        self.assertEqual(self.engine.score, 0)
        self.assertEqual(self.engine.results, []) 

    # Check that when an engine is created, the question index is 0, score is 0, and no results have been stores.
    # verifies that the __init__ function is workign correctly

    def test_correct_answer_increments_score(self): # Test correct answers
        q = self.engine.current_question()
        correct = q["answer_index"]

        result = self.engine.check_answer(correct)

        self.assertTrue(result)
        self.assertEqual(self.engine.score, 1)
        self.assertEqual(len(self.engine.results), 1)

    # Testing that the correct answers work as they should do by confirming:
    # The method returned true
    # The score increased to 1
    # One result was stored

    def test_incorrect_answer_does_not_increment_score(self): # Test incorrect answers
        q = self.engine.current_question()
        wrong = (q["answer_index"] + 1) % len(q["options"])

    # Gets the answer index and adds one to make sure the answer is incorrect as that is what we are testing for

        result = self.engine.check_answer(wrong)

        self.assertFalse(result)
        self.assertEqual(self.engine.score, 0)
        self.assertEqual(len(self.engine.results), 1)

    # Testing incorrect answers work as they should do by confirming:
    # Returned false
    # Score did not go up
    # The results was still stored

    def test_next_question_works(self): # Tests that it continuously call the ext question until it returns false
        moves = 0
        while self.engine.next_question():
            moves += 1

        self.assertEqual(moves, len(self.engine.questions) - 1)
        self.assertFalse(self.engine.next_question()) # Calls next_question() one more time at the end to ensure it returns false

    # Checks that we can move through all questions and stops at the end

    def test_restart_resets(self): # Tests the restart button has reset the quiz
        self.engine.check_answer(self.engine.current_question()["answer_index"])
        self.engine.next_question()
        self.engine.restart()

        self.assertEqual(self.engine.index, 0)
        self.assertEqual(self.engine.score, 0)
        self.assertEqual(self.engine.results, [])

    # Answers a question
    # Moves to the next question
    # Calls restart and verify's everything has been reset properly, Question index, Score and user results.

if __name__ == "__main__":
    unittest.main()