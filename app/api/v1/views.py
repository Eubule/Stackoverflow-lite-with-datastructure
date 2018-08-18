from flask import Blueprint, jsonify, abort, request, make_response
from ..models import Questions, questions, Answers, answers, all_questions_answers


module = Blueprint('v1', __name__)

quest = Questions()
ans = Answers()

#endpoint for to fetch all questions
@module.route('/api/v1/questions', methods = ['GET'])
def get_questions():
    """
    Route to fetch all the questions.

    """
    return jsonify({"questions":quest.get_questions()})
