from run import app
import unittest
from flask import json
from app.api.v1 import views


class TestAnswers(unittest.TestCase):

    def setUp(self):
        """This instanciates the flask app for a background no-live-server operations for testing purposes"""    
        self.app = app.test_client()

    def test_return_bad_request_error_if_request_is_missing_some_fields(self):
        """This checks if input fields are in bad format and returns an error"""

        response = self.app.post("/api/v1/questions", content_type='application/json',data = json.dumps({
            'id': 1,
            'title': 'testing',
            'body': 'answer test'
        }))
        response = self.app.post("/api/v1/questions/1/answers",content_type='application/json', data = json.dumps(dict({
            'body': 'answer test'
        })))
        self.assertEquals(response.status_code, 400)

    def test_return_created_code_if_answer_is_valid(self):
        """This method checks if a valid answer has been posted and returns an apropriate status code 201"""

        response = self.app.post('/api/v1/questions', content_type = 'application/json', data = json.dumps({
            'id':2,
            'title': 'Psychic',
            'body': 'What am I thinking about right now?'
        }))
        response = self.app.post('/api/v1/questions/1/answers', content_type='application/json',data = json.dumps({
            'question_id': 2,
            'body': 'this is the answer to the question right now on your mind...'
        }))
        self.assertEquals(response.status_code, 201)

    def test_return_error_msg_if_body_of_answer_is_empty(self):
        """This method tests if the body of posted answer is empty, if so it returns an error message"""
        response = self.app.post('/api/v1/questions', content_type = 'application/json', data = json.dumps({
            'id':3,
            'title': 'What is an andela developer supposed to know?',
            'body': ''
        }))
        self.assertEquals(response.status_code, 400)
        self.assertTrue("Failed" in response.get_data(as_text=True))
    
    def test_return_not_found_if_attempt_to_answer_question_that_doesnot_exist(self):
        """This method return error if user attempts to access a question that does not exist"""
        response = self.app.post('/api/v1/questions/1/answers', content_type='application/json',data = json.dumps({
            'question_id': 4,
            'body': 'this is the answer to the question right now on your mind...'
        }))
        self.assertEquals(response.status_code, 404)