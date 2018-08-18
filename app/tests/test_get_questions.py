from run import app
import unittest
from app.api.v1 import views
from flask import json


class TestGetQuestions(unittest.TestCase):
    """
    This Test class is meant to test all the routes with a GET method

    """

    def setUp(self):
        """This instanciates the flask app for a background no-live-server operations for testing purposes"""    
        self.app = app.test_client()
    
    def test_if_all_successfuly_returned_all_questions(self):
        """This method checks if a successful code is returned in case all questions were fetched"""
        response = self.app.post('/api/v1/questions', content_type='application/json', data={
            'id': 1,
            'title': 'testing',
            'body': 'answer test'
        })
        response = self.app.get('/api/v1/questions', follow_redirects = True)
        self.assertEquals(response.status_code, 200)

    def test_returns_not_found_if_question_doesnot_exist(self):
        """This method returns a 404 Not found error message if a specific question is not found"""
        response = self.app.get('/api/v1/questions/7')
        self.assertEquals(response.status_code, 404)
        self.assertTrue('Not found' in response.get_data(as_text = True))

    def test_pass_if_question_is_found_in_the_database(self):
        """This method returns a 200 status code if question id is found in the database"""

        response = self.app.post('/api/v1/questions', content_type='application/json', data=json.dumps({
            'id': 1,
            'title': 'testing',
            'body': 'answer test'
        }))
        response = self.app.get('/api/v1/questions/1')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEquals(data['question'], {
            'id': 1,
            'title': 'testing',
            'body': 'answer test'
        })