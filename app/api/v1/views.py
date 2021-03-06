from flask import Blueprint, jsonify, abort, request, make_response
from .models import Questions, questions, Answers, answers, all_questions_answers


module = Blueprint('v1', __name__)

quest = Questions()
ans = Answers()

#endpoint for to fetch all questions
@module.route('/api/v1/questions', methods = ['GET'])
def get_questions():
    """
    Route to fetch all the questions.

    """
    if questions == []:
        return jsonify({"Message": "No questions yet"})
    return jsonify({"questions": quest.get_questions()}),200

#endpoint for fetching a specific question
@module.route('/api/v1/questions/<int:question_id>', methods =['GET'])
def get_specific_question(question_id):
    """
    Route to fetch a specific question.

    """

    # Return a 404 Not Found error message if question not found in the dictionary
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        return jsonify({"Message": "There is no question that matches the id you specified"}), 404

    return jsonify({'question': question[0]})

#endpoint for posting a questing
@module.route('/api/v1/questions', methods = ['POST'])
def post_question():
    """
    Route to post or ask a question.
    It populates the data qiestions dictionary if inputs are valid and
    Return 400. Bad Request error if input not in json format.
    
    """

    if not request.json:
        return jsonify({"Message": "Please make sure tour input is in dictionary format"}),400
    if not 'id' in request.json or not 'title' in request.json or not 'body' in request.json:
        return jsonify({"Message": "Please specify question id and body of the answer bofore you post"}), 400
    
    
    question = quest.post_question(request.json['id'], request.json['title'], request.json['body'])

    #return error message if post_question() method from the Questions class return an error
    if question != None:
        return question

    question = [question for question in questions if question['id'] == request.json['id']]
    return jsonify({'question': question[0]}), 201

@module.route('/api/v1/questions/<int:question_id>/answers', methods = ['POST'])
def post_answer(question_id):
    """Endpoint to post an answer for a specific question"""
    if not request.json:
        return jsonify({"Message": "Please make sure tour input is in dictionary format"}),400
    if not 'question_id' in request.json or not 'body' in request.json:
        return jsonify({"Message": "Please specify question id and body of the answer bofore you post"}), 400
    
    answer = ans.post_answer(request.json['question_id'], request.json['body'])

    #return error message if post_question() method from the Questions class return an error
    if answer != None:
        return answer

    answer = [answer for answer in answers if answer['question_id'] == request.json['question_id']]
    return jsonify({'Answer': answer[0]}), 201

@module.route('/api/v1/questions/<int:question_id>/answers', methods = ['GET'])
def get_answer(question_id):
    """endpoint to fetch all answers to a question"""
    if ans.get_answer(question_id) == False:
        return jsonify({"Message": "The question you are trying to access does not exist"})
    return jsonify({"Answers": ans.get_answer(question_id)}), 200

@module.errorhandler(404)
def not_found(error):
    """This errorhandler method return a user friendly message if resource is not found."""
    return make_response(jsonify({'error': 'The resource you are looking for does not exist in the database'}), 404)