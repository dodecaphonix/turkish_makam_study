COMMAS_PER_OCTAVE = 53

AJINAS = {
    "Çârgâh": ["R", "M2", "M3", "4", "5"],  # Major
    "Bûselik": ["R", "M2", "m3", "4", "5"],  # Minor
    "Kürdî": ["R", "m2", "m3", "4", "5"],  # Phrygian
    "Uşşâk": ["R", "vM2", "m3", "4", "5"],  # Minor with microtonal 2
    "Hicaz": ["R", "^m2", "vM3", "4", "5"],  # Phrygian Dominant with microtonal 2, 3
    "Rast": ["R", "M2", "vM3", "4", "5"],  # Major with microtonal 3
}

# See https://www.turkishudlessons.com/pitch-perde for more info
CANTEMIR_PITCH_COLLECTION = [
    "Yegâh",
    "Hüseynî Aşîrân",
    "Irak",
    "Rast",
    "Dügâh",
    "Segâh",
    "Çârgâh",
    "Nevâ",
    "Hüseynî",
    "Eviç",
    "Gerdâniye",
    "Muhayyer",
    "Tîz Segâh",
    "Tîz Çârgâh",
    "Tîz Nevâ",  # I don't have this in COMMA_TO_NOTE_NAME yet
    "Tîz Hüseynî",  # I don't have this in COMMA_TO_NOTE_NAME yet
]

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
COMMAS_OF_FUNDAMENTAL_PITCHES = [k for k, v in COMMA_TO_NOTE_NAME.items() if v in CANTEMIR_PITCH_COLLECTION]

TOTAL_COMMAS = max(COMMA_TO_NOTE_NAME.keys())
