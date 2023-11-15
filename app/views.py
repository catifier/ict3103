from app import app
from app.validate import validate, validate_addition
from flask import render_template, request


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("text_box")
        result = validate(text)
        if result[1]:
            return render_template("result.html", validated_result=text)
    return render_template('home.html')


@app.route('/calculator', methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        result = validate_addition(number1, number2)
        if result[1]:
            return render_template("result.html", validated_result=str(result[0]))
    return render_template('calculator.html')