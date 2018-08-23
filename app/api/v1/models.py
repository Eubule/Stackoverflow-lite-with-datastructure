from flask import jsonify, abort, make_response


questions = []
answers = []
all_questions_answers = []

class Questions():
    """
    This class deals with all qestion related tasked, for users who attempt to fetch:
    - fetch all questions
    - fetch a specific questions or
    - post all question
    """
    def __init__(self):
        self.quest_id = 0
        self.title = ""
        self.body = ""
    
    def get_questions(self):
        """
        This method returns the list of all questions in the database.

        """
                
        if self.quest_id == 0 and self.title.strip() == "" and self.body.strip() == "":
            abort(404)
        return questions

    def post_question(self, id:int, title:str,body:str):
        """
        This method is meant to post a question with a question id, title and body.
        It returns a failed message if an of the fields is empty or if user attempts to enter an already asked question.

        """

        if id <= 0 or title.strip() == '' or body.strip() == '':
            return jsonify({
                "Message": "question's title and body can't be empty"
            }),400
        question = [question for question in questions if question['id'] == id or question['title'] == title.strip()]
        
        # Returns a failed message if user attempts to post an already asked questions.
        if len(question) != 0:
            return jsonify({
                "Message": "Question's id or title already exists"
            })
        self.quest_id = id
        self.title = title.strip()
        self.body = body
        question = {
            'id': id,
            'title': title,
            'body': body
        }
        questions.append(question)

class Answers():
    """
    This class models the user's activities with theanswers data. It allows the user:
    - To post an answer
    - View answers to particular question and
    - view a particular answer to a particular question

    """

    def post_answer(self, question_id, body):
        """
        This method allows the user to post an answer tied to a question.
        Return a fail message in case the message body was empty or if question does not exist

        """
        question = [question for question in questions if question['id'] == question_id]
        if len(question) == 0:
            return jsonify({
                "Message": "You can't answer a question that does not exist"
            }), 404
        if body.strip() == '':
            return jsonify({
                "Message": "Your answer's body is empty please enter a valid answer."
            }),400

        #Automaticaly generate answer id by adding 1 to the length of the dictionary.
        id = len(answers) + 1
        quest = [quest for quest in questions if quest['id'] == question_id]
        title = quest[0]['title']
        answer = {
            'question_id': question_id,
            'title': title,
            'id': id,
            'body': body
        }
        answers.append(answer)

    def get_answer(self, question_id):
        """
        This method fetches all the answers posted for a specific question

        """
        question = [question for question in questions if question['id'] == question_id]
        if len(question) != 0:
            return answers
        abort(404)
        