# TODO: This will be an actual relational DB eventually

# TODO: Should starting_pitch be modeled as starting commas/interval up from tonic for ease of transposition?
#  Also, it is slightly complicated by being able to start on Yegâh/Nevâ which are both the 5th
#  Hmmm... starting_pitch is used by the UI. Will we ever actually transpose?
MAKAMS = {
    "Rast": {
        "tonic": "Rast",
        "ajnas": [
            {"name": "Rast", "starting_pitch": "Rast", "pitch_count": 5},
            {"name": "Rast", "starting_pitch": "Nevâ", "pitch_count": 4},
            {"name": "Bûselik", "starting_pitch": "Nevâ", "pitch_count": 4},
            {"name": "Rast", "starting_pitch": "Yegâh", "pitch_count": 4},
        ]
    },
    "Çârgâh": {
        "tonic": "Çârgâh",
        "ajnas": [
            {"name": "Çârgâh", "starting_pitch": "Çârgâh", "pitch_count": 5},
            {"name": "Çârgâh", "starting_pitch": "Gerdâniye", "pitch_count": 4},
        ]
    },
    "Uşşâk": {
        "tonic": "Dügâh",
        "ajnas": [
            {"name": "Uşşâk", "starting_pitch": "Dügâh", "pitch_count": 4},
            {"name": "Bûselik", "starting_pitch": "Nevâ", "pitch_count": 5},
        ]
    },
    "Kürdî": {
        "tonic": "Dügâh",
        "ajnas": [
            {"name": "Kürdî", "starting_pitch": "Dügâh", "pitch_count": 4},
            {"name": "Bûselik", "starting_pitch": "Nevâ", "pitch_count": 5},
        ]
    }
}
