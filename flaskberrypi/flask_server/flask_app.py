from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/move', methods=['POST'])
def move():
    return render_template('index.html')


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
