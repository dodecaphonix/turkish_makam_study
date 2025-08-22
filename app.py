from flask import (
    Flask,
    g,
    render_template,
)

from makam import generate_test_makam


app = Flask(__name__)


@app.route('/')
def index():
    g.table_data = generate_test_makam()
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
