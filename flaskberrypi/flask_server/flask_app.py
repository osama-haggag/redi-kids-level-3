import random

from flask import Flask, request, render_template, session

app = Flask(__name__)
app.secret_key = 'thisIsSecret'

MAX_ATTEMPTS = 7


@app.route('/guess', methods=['POST'])
def guess():
    if session['num_attempts'] == 0:
        return "You failed!"
    user_guess_input = request.form.get('guess')
    if not user_guess_input.isnumeric():
        return "Wrong Input: give me a number"

    user_guess = int(user_guess_input)

    if user_guess == session['secret_number']:
        return render_template('index.html', answer='Correct')
    elif user_guess > session['secret_number']:
        session['num_attempts'] -= 1
        return render_template('index.html', answer='Too High. {} attempts left!'.format(session['num_attempts']))
    else:
        session['num_attempts'] -= 1
        return render_template('index.html', answer='Too Low. {} attempts left!'.format(session['num_attempts']))


@app.route('/')
def main():
    session['secret_number'] = random.randint(1, 100)
    print(session['secret_number'])
    session['num_attempts'] = MAX_ATTEMPTS
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
