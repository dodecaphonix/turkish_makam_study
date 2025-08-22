from flask import Flask

from makam import generate_test_makam


app = Flask(__name__)


@app.route('/')
def hello_world():
    response = ""
    for interval, comma, name in generate_test_makam():
        response += f"{interval:>3} {comma:>3} {name}<br>"
    return f"<pre>{response}</pre>"


if __name__ == '__main__':
    app.run(debug=True)
