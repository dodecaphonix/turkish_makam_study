from flask import (
    Flask,
    g,
    render_template,
    request,
)

from constants import (
    COMMA_TO_NOTE_NAME,
    TOTAL_COMMAS,
    COMMAS_OF_FUNDAMENTAL_PITCHES,
)
from interval_calculator import hydrate_intervals_for_makam
from makam_db import MAKAMS

app = Flask(__name__)


@app.route('/')
def index():
    makam_name = request.args.get('makam', default='Rast', type=str)
    g.all_makams = MAKAMS.keys()
    g.note_names = COMMA_TO_NOTE_NAME
    g.fundamental_pitch_commas = COMMAS_OF_FUNDAMENTAL_PITCHES
    g.total_commas = TOTAL_COMMAS
    g.makam_name = makam_name
    g.makam_data = hydrate_intervals_for_makam(makam=MAKAMS[makam_name])
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
