from interval import Interval


R = Interval(degree=1)
m2 = Interval(degree=2, accidental=-1)
up_m2 = Interval(degree=2, accidental=-1, comma_displacement=1)
down_M2 = Interval(degree=2, comma_displacement=-1)
M2 = Interval(degree=2)
m3 = Interval(degree=3, accidental=-1)
up_m3 = Interval(degree=3, accidental=-1, comma_displacement=1)
down_M3 = Interval(degree=3, comma_displacement=-1)
M3 = Interval(degree=3)
up_D4 = Interval(degree=4, accidental=-1, comma_displacement=1)
P4 = Interval(degree=4)
down_A4 = Interval(degree=4, accidental=1, comma_displacement=-1)
P5 = Interval(degree=5)
M6 = Interval(degree=6)
down_M7 = Interval(degree=7, comma_displacement=-1)

P5_below = Interval(degree=5, octave_displacement=-1)


JINS_STARTING_INTERVALS = {
    "R": R,
    "m3": m3,
    "P4": P4,
    "P5": P5,
    "low_P5": P5_below,
}

TETRACHORDS = {
    "Çârgâh ₄": [R, M2, M3, P4],  # Major - Pythagorean tuning
    "Bûselik ₄": [R, M2, m3, P4],  # Minor - Pythagorean tuning
    "Kürdî ₄": [R, m2, m3, P4],  # Phrygian - Pythagorean tuning
    "Uşşâk ₄": [R, down_M2, m3, P4],  # Minor - Pythagorean tuning with microtonal maj 2
    "Hicaz ₄": [R, up_m2, down_M3, P4],  # Phrygian Dominant - Just tuning with microtonal min 2
    "Rast ₄": [R, M2, down_M3, P4],  # Major - Just tuning
    # Less common
    "Saba ₄": [R, down_M2, m3, up_D4]  # Min b4 = with a vM2 ^D4
}

PENTACHORDS = {
    "Çârgâh ₅": [R, M2, M3, P4, P5],  # Major - Pythagorean tuning
    "Bûselik ₅": [R, M2, m3, P4, P5],  # Minor - Pythagorean tuning
    "Kürdî ₅": [R, m2, m3, P4, P5],  # Phrygian - Pythagorean tuning
    "Hüseyni ₅": [R, down_M2, m3, P4, P5],  # Minor - Pythagorean tuning with microtonal maj 2
    "Hicaz ₅": [R, up_m2, down_M3, P4, P5],  # Phrygian Dominant - Just tuning with microtonal min 2
    "Rast ₅": [R, M2, down_M3, P4, P5],  # Major - Just tuning
    # Less common
    "Pençgâh ₅": [R, M2, M3, down_A4, P5],  # Lydian - Pythagorean with vA4
    "Nikriz ₅": [R, M2, up_m3, down_A4, P5],  # Min #4 - with a ^m3  vA4
}

AJINAS = TETRACHORDS | PENTACHORDS

COMMA_TO_NOTE_NAME = {
    0: 'Kaba Çârgâh',
    4: 'Kaba Nim Hicâz',
    5: 'Kaba Hicâz',
    8: 'Kaba Dik Hicâz',
    9: 'Yegâh',
    13: 'Kaba Nim Hisâr',
    14: 'Kaba Hisâr',
    17: 'Kaba Dik Hisâr',
    18: 'Hüseynî Aşîrân',
    22: 'Acem Aşîrân',
    23: 'Dik Acem Aşîrân',
    26: 'Irak',
    27: 'Gevest',
    30: 'Dik Gevest',
    31: 'Rast',
    35: 'Nim Zirgüle',
    36: 'Zirgüle',
    39: 'Dik Zirgüle',
    40: 'Dügâh',
    44: 'Kürdi',
    45: 'Dik Kürdi',
    48: 'Segâh',
    49: 'Bûselik',
    52: 'Dik Bûselik',
    53: 'Çârgâh',
    57: 'Nim Hicâz',
    58: 'Hicâz',
    61: 'Dik Hicâz',
    62: 'Nevâ',
    66: 'Nim Hisâr',
    67: 'Hisâr',
    70: 'Dik Hisâr',
    71: 'Hüseynî',
    75: 'Acem',
    76: 'Dik Acem',
    79: 'Eviç',
    80: 'Mâhûr',
    83: 'Dik Mâhûr',
    84: 'Gerdâniye',
    88: 'Nim Şehnâz',
    89: 'Şehnâz',
    92: 'Dik Şehnâz',
    93: 'Muhayyer',
    97: 'Sünbüle',
    98: 'Dik Sünbüle',
    101: 'Tîz Segâh',
    102: 'Tîz Bûselik',
    105: 'Tîz Dik Bûselik',
    106: 'Tîz Çârgâh'
}

NOTE_NAME_TO_COMMA = {v: k for k, v in COMMA_TO_NOTE_NAME.items()}

TOTAL_COMMAS = max(COMMA_TO_NOTE_NAME.keys())

COMMAS_PER_OCTAVE = 53
# This is a just intonation major scale with the 3rd and 7th lowered by a comma
FUNDAMENTAL_INTERVALS = [R, M2, down_M3, P4, P5, M6, down_M7]
# These are the commas of the very accurate 53EDO approximation of the just major scale used in Turkish music
COMMAS_OF_FUNDAMENTAL_INTERVALS = [interval.commas for interval in FUNDAMENTAL_INTERVALS]
# It we start on Rast, we have the Cantemir pitch collection
# See https://www.turkishudlessons.com/pitch-perde for more info
COMMAS_OF_FUNDAMENTAL_PITCHES = [
    (comma + NOTE_NAME_TO_COMMA["Rast"]) % COMMAS_PER_OCTAVE
    for comma in COMMAS_OF_FUNDAMENTAL_INTERVALS
]

# TODO: Simplify this expression and define magic numbers as constants
OUD_NOTE_WIDTHS = [round(((1 / (2**(i/53))) - (1 / (2**((i+1)/53)))) * 3 * 100, 2) for i in range(31+1)]
OUD_TUNING = [
    NOTE_NAME_TO_COMMA["Gerdâniye"],
    NOTE_NAME_TO_COMMA["Nevâ"],
    NOTE_NAME_TO_COMMA["Dügâh"],
    NOTE_NAME_TO_COMMA["Hüseynî Aşîrân"],
    NOTE_NAME_TO_COMMA["Nevâ"] - COMMAS_PER_OCTAVE,
    NOTE_NAME_TO_COMMA["Dügâh"] - COMMAS_PER_OCTAVE,
]
