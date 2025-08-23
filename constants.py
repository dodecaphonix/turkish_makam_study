COMMAS_PER_OCTAVE = 53

AJINAS = {
    "Çârgâh": ["R", "M2", "M3", "4", "5"],  # Major - Pythagorean tuning
    "Bûselik": ["R", "M2", "m3", "4", "5"],  # Minor - Pythagorean tuning
    "Kürdî": ["R", "m2", "m3", "4", "5"],  # Phrygian - Pythagorean tuning
    "Uşşâk": ["R", "vM2", "m3", "4", "5"],  # Minor - Pythagorean tuning with microtonal maj 2
    "Hicaz": ["R", "^m2", "vM3", "4", "5"],  # Phrygian Dominant - Just tuning with microtonal min 2
    "Rast": ["R", "M2", "vM3", "4", "5"],  # Major - Just tuning
}

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

COMMA_TO_INTERVAL = {
    0: "R",
    4: "m2",
    5: "^m2",
    8: "vM2",
    9: "M2",
    13: "m3",
    14: "^m3",
    17: "vM3",
    18: "M3",
    22: "4",
    23: "^4",
    26: "D5",
    27: "A4",
    30: "v5",
    31: "5",
    35: "m6",
    36: "^m6",
    39: "vM6",
    40: "M6",
    44: "m7",
    45: "^m7",
    48: "vM7",
    49: "M7",
}


NOTE_NAME_TO_COMMA = {v: k for k, v in COMMA_TO_NOTE_NAME.items()}
INTERVAL_TO_COMMA = {v: k for k, v in COMMA_TO_INTERVAL.items()}

TOTAL_COMMAS = max(COMMA_TO_NOTE_NAME.keys())

# This is a just intonation major scale with the 3rd and 7th lowered by a comma
FUNDAMENTAL_INTERVALS = ["R", "M2", "vM3", "4", "5", "M6", "vM7"]
# These are the commas of the very accurate 53EDO approximation of the just major scale used in Turkish music
COMMAS_OF_FUNDAMENTAL_INTERVALS = [k for k, v in COMMA_TO_INTERVAL.items() if v in FUNDAMENTAL_INTERVALS]
# It we start on Rast, we have one octave of the Cantemir pitch collection
# See https://www.turkishudlessons.com/pitch-perde for more info
COMMAS_OF_FUNDAMENTAL_PITCHES = [
    (comma + NOTE_NAME_TO_COMMA["Rast"]) % COMMAS_PER_OCTAVE
    for comma in COMMAS_OF_FUNDAMENTAL_INTERVALS
]
