from flask import (
    Flask,
    g,
    render_template,
)

from constants import (
    COMMA_TO_NOTE_NAME,
    TOTAL_COMMAS,
)
from interval_calculator import hydrate_intervals_for_makam
from makam_db import MAKAMS

app = Flask(__name__)


@app.route('/')
def index():
    g.note_names = COMMA_TO_NOTE_NAME
    g.total_commas = TOTAL_COMMAS
    # Only one makam hardcoded for now
    g.makam = hydrate_intervals_for_makam(makam=MAKAMS["makam_Uşşâk"])
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
