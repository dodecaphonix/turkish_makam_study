from constants import (
    COMMA_TO_NOTE_NAME,
    COMMA_TO_INTERVAL,
    DIVISIONS_OF_OCTAVE,
    INTERVAL_TO_COMMA,
    LARGEST_NOTE_COMMA,
    NOTE_NAME_TO_COMMA,
)

"""
For more info, see: https://en.wikipedia.org/wiki/Turkish_makam
"""


tetrachord_names = {
    "Çârgâh": ["R", "M2", "M3", "4"],  # Major
    "Bûselik": ["R", "M2", "m3", "4"],  # Minor
    "Kürdî": ["R", "m2", "m3", "4"],  # Phrygian
    "Uşşâk": ["R", "vM2", "m3", "4"],  # Minor with microtonal 2
    "Hicaz": ["R", "^m2", "vM3", "4"],  # Phrygian Dominant with microtonal 2, 3
    "Rast": ["R", "M2", "vM3", "4"],  # Major with microtonal 3
}


def intervals_to_commas(tetrachord_name, starting_pitch):
    interval_names = tetrachord_names[tetrachord_name]
    starting_comma = NOTE_NAME_TO_COMMA[starting_pitch]
    return [INTERVAL_TO_COMMA[interval_name] + starting_comma for interval_name in interval_names]


if __name__ == "__main__":
    tonic = "Dügâh"
    Uşşâk_makam = [
        {"tetrachord_name": "Uşşâk", "starting_pitch": "Dügâh"},
        {"tetrachord_name": "Bûselik", "starting_pitch": "Nevâ"},
    ]

    commas = []
    for tetrachord in Uşşâk_makam:
        commas += intervals_to_commas(**tetrachord)

    for i in range(LARGEST_NOTE_COMMA, -1, -1):
        name = COMMA_TO_NOTE_NAME.get(i, "")
        interval = COMMA_TO_INTERVAL.get((i - NOTE_NAME_TO_COMMA[tonic]) % DIVISIONS_OF_OCTAVE, "") if i in commas else ""
        print(f"{interval:>3} {i:>3} {name}")
