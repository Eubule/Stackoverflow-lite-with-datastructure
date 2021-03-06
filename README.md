# Stackoverflow-lite-with-datastructure
[![Build Status](https://travis-ci.com/Eubule/Stackoverflow-lite-with-datastructure.svg?branch=master)](https://travis-ci.com/Eubule/Stackoverflow-lite-with-datastructure)
[![Coverage Status](https://coveralls.io/repos/github/Eubule/Stackoverflow-lite-with-datastructure/badge.svg?branch=ch-test-resources-endpoint-159869003)](https://coveralls.io/github/Eubule/Stackoverflow-lite-with-datastructure?branch=ch-test-resources-endpoint-159869003)
[![Maintainability](https://api.codeclimate.com/v1/badges/602cd3fa79e194352588/maintainability)](https://codeclimate.com/github/Eubule/Stackoverflow-lite-with-datastructure/maintainability)

## DESCRIPTION

Stackoverflow-lite is a platform where people can ask questions and provide answers

## Link to Stackoverflow-lite on Github Pages

[Stackoverflow-lite](https://eubule.github.io/Stack-Overflow-lite/)

## Link to Stackoverflow-lite using data stuctures on Heroku

[Stackoverflow-lite-using-data-structure](https://fierce-journey-23996.herokuapp.com/api/v1/questions)

## Routes captured by Stackoverflow-lite

 REQUEST | ROUTE | FUNCTIONALITY
 ------- | ----- | -------------
 **GET** | /api/v1/questions | Fetches all questions
 **POST** | /api/v1/questions | Posts a question
 **GET** | /api/v1/question/< questionId> | Fetches a specific question
 **POST** | /api/v1/questions/< questionId>/answers | Post an answer to a question
 **GET** | /api/v1/questions/< questionId>/answers | Fetches all answers

## BUIT WITH

 * Flask-Python

## HOW TO RUN THE APPLICATION

 ### SETING UP THE ENVIRONMENT
 
 1. Clone this repository to your local PC

    **` git clone https://github.com/Eubule/Stackoverflow-lite-with-datastructure.git `** [here](https://github.com/Eubule/Stackoverflow-lite-with-datastructure)


 2. Create a virtual environment to run application specific dependencies

    **`$ virtualenv venv`**  To create a virtual environment separate from your system

    **`$ source venv/bin/activate`**   To activate you virtual environment

    **`$ pip install flask`**   To install the flask framework that will be used throughout

    **`$ pip freeze > requirements.txt`**   To install requirements useful when hosting the app on a remote server


 ### RUN THE APP

 1. To run the app

    **` python run.py `**

 2. To run tests

    **`  python -m pytest --cov app/ `**


## Author

**Malaba**

