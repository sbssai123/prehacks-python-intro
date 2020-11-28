import copy
import math
from flask import (
    Flask, flash, render_template, request
)
import random

app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY='dev',
)

# a simple page that says hello :)
@app.route('/')
def hello():
    return "Hello World!! 😁"

questions = [
    {"question": "What is your favorite stone?", "answers": ["Opal", "Sapphire", "Ruby", "Emerald"]},
    {"question": "What is your favorite type of animal?", "answers": ["Dog", "Elephant", "Cat", "Snake"]},
    {"question": "What is your favorite food?", "answers": ["Pizza", "Oatmeal","Chicken", "Avocado"]}
]

@app.route('/quiz', methods=['GET'])
def show_quiz():
    shuffled_questions = shuffle_questions()
    return render_template('quiz.html', questions=shuffled_questions)

@app.route('/result', methods=['POST'])
def submit_quiz():
    results = request.form
    if len(results) != len(questions):
        error = 'Please fill out all questions'
        flash(error)
        shuffled_questions = shuffle_questions()
        return render_template('quiz.html', questions=shuffled_questions)
    else:
        score = 0
        for q in questions:
            answer_selected = results[q['question']]
            if answer_selected == q['answers'][0]:
                score = score + 1
        percent_correct = math.ceil((score / len(questions)) * 100)
        return render_template('result.html', percent_correct=percent_correct)

def shuffle_questions():
    shuffled_questions = copy.deepcopy(questions)
    for item in shuffled_questions:
        random.shuffle(item["answers"])
    return shuffled_questions