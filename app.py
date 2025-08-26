from flask import (
    Flask,
    g,
    render_template,
    request,
)

from constants import (
    COMMA_TO_NOTE_NAME,
    COMMAS_OF_FUNDAMENTAL_PITCHES,
    OUD_NOTE_WIDTHS,
    OUD_TUNING,
    TOTAL_COMMAS,
)
from interval_calculator import hydrate_intervals_for_makam
from makam_db import MAKAMS

app = Flask(__name__)


@app.route('/')
def index():
    makam_name = request.args.get('makam', default='Rast', type=str)
    g.show_oud_commas = request.args.get('show_oud_commas', default=False, type=bool)
    g.all_makams = MAKAMS.keys()
    g.note_names = COMMA_TO_NOTE_NAME
    g.fundamental_pitch_commas = COMMAS_OF_FUNDAMENTAL_PITCHES
    g.total_commas = TOTAL_COMMAS
    g.makam_name = makam_name
    g.makam_data = hydrate_intervals_for_makam(makam=MAKAMS[makam_name])
    g.oud_note_widths = OUD_NOTE_WIDTHS
    g.oud_tuning = OUD_TUNING
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
