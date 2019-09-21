import random

from flask import Flask, request, render_template, session

from pins import displayLife, win

app = Flask(__name__)
app.secret_key = 'thisIsSecret'

MAX_ATTEMPTS = 9


@app.route('/guess', methods=['POST'])
def guess():
    user_guess_input = request.form.get('guess')
    if not user_guess_input.isnumeric():
        return "Wrong Input: give me a number"

    user_guess = int(user_guess_input)

    if user_guess == session['secret_number']:
        win()
        return render_template('success.html')

    if user_guess > session['secret_number']:
        session['num_attempts'] -= 1
        answer = "Too high"
    else:
        session['num_attempts'] -= 1
        answer = "Too low"

    if session['num_attempts'] == 0:
        return render_template('failure.html')

    displayLife(session['num_attempts'])
    return render_template('index.html', answer=answer, max_attempts=MAX_ATTEMPTS, attempts_left=session['num_attempts'])


@app.route('/')
def main():
    session['secret_number'] = random.randint(1, 100)
    print(session['secret_number'])
    session['num_attempts'] = MAX_ATTEMPTS
    displayLife(MAX_ATTEMPTS)
    return render_template('index.html', max_attempts=MAX_ATTEMPTS, attempts_left=session['num_attempts'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
