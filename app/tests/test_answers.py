from app import app
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
        self.assertTrue("question's title and body can't be empty" in response.get_data(as_text=True))
    
    def test_return_not_found_if_attempt_to_answer_question_that_doesnot_exist(self):
        """This method return error if user attempts to access a question that does not exist"""
        response = self.app.post('/api/v1/questions/1/answers', content_type='application/json',data = json.dumps({
            'question_id': 4,
            'body': 'this is the answer to the question right now on your mind...'
        }))
        self.assertEquals(response.status_code, 404)

    def test_if_get_answer_retrieved_all_questions_successfuly(self):
        """This method checks if the user successfully retrieved all the answers to the questions."""
        response = self.app.post('/api/v1/questions', content_type = 'application/json', data = json.dumps({
            'id':9,
            'title': 'Andela challenge 3',
            'body': 'What is challenge gonna be like?'
        }))
        response_ans = self.app.post('/api/v1/questions/8/answers', content_type = 'application/json', data = json.dumps({
            'question_id':9,
            'body': 'Oops...I do not remember the name of the founder of andela'
        }))
        self.assertEquals(response_ans.status_code, 201)
        response_get_ans = self.app.get('/api/v1/questions/9/answers')

        self.assertEquals(response_get_ans.status_code, 200)                                                                                                                       
    def test_if_error_is_thrown_attempting_to_answer_unexisting_question(self):
        """This method checks if user tries to answer an unexisting question"""
        response = self.app.post('/api/v1/questions', content_type = 'application/json', data = json.dumps({
            'id':10,
            'title': 'Andela challenge 4',
            'body': 'What is challenge gonna be like?'
        }))
        response = self.app.post('/api/v1/questions/11/answers', content_type = 'application/json', data = json.dumps({
            'question_id': 12,
            'body': 'Answer for unexisting question.'
        }))
        response = self.app.get('/api/v1/questions/12/answers')
        self.assertTrue("The question you are trying to access does not exist" in response.get_data(as_text = True))                       
        
        
