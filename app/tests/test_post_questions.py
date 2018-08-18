from run import app
import unittest
from app.api.v1 import views
from flask import jsonify, json


class TestPostQuestions(unittest.TestCase):

    def setUp(self):
        """This instanciates the flask app for a background no-live-server operations for testing purposes"""
        self.app = app.test_client()

    def test_if_post_question_adds_valid_data(self):
        """This checks if valid data has been added"""

        response = self.app.post("/api/v1/questions", content_type='application/json',data = json.dumps(dict({
            'id': 6,
            'title': 'Andela bootcamp',
            'body': 'What are we gonna do for at bootcamp?'
        })))
        self.assertEquals(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEquals(data['question'],{
            'id': 6,
            'title': 'Andela bootcamp',
            'body': 'What are we gonna do for at bootcamp?'
        })

    def test_return_bad_format_if_request_has_missing_fields(self):
        """This checks if input fields are in bad format and returns an error"""

        response = self.app.post("/api/v1/questions", data = json.dumps({
            'title': 'testing',
            'body': 'answer test'
        }))
        self.assertEquals(response.status_code, 400)
    
  
        