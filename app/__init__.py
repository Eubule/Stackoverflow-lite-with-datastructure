from flask import Flask

app = Flask(__name__)

from app.api.v1.views import module

app.register_blueprint(module)