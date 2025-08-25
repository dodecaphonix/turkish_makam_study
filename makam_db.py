# TODO: This will be an actual relational DB eventually

MAKAMS = {
    "Rast": {
        "tonic": "Rast",
        "ajnas": [
            {"name": "Rast ₅", "starting_interval": "R"},
            {"name": "Rast ₄", "starting_interval": "P5"},
            {"name": "Bûselik ₄", "starting_interval": "P5"},
            {"name": "Rast ₄", "starting_interval": "low_P5"},
        ]
    },
    "Çârgâh": {
        "tonic": "Çârgâh",
        "ajnas": [
            {"name": "Çârgâh ₅", "starting_interval": "R"},
            {"name": "Çârgâh ₄", "starting_interval": "P5"},
        ]
    },
    "Uşşâk": {
        "tonic": "Dügâh",
        "ajnas": [
            {"name": "Uşşâk ₄", "starting_interval": "R"},
            {"name": "Bûselik ₅", "starting_interval": "P4"},
        ]
    },
    "Kürdî": {
        "tonic": "Dügâh",
        "ajnas": [
            {"name": "Kürdî ₄", "starting_interval": "R"},
            {"name": "Bûselik ₅", "starting_interval": "P4"},
        ]
    },
    # https://en.wikipedia.org/wiki/List_of_Turkish_makams
    "Nikriz": {
        "tonic": "Rast",
        "ajnas": [
            {"name": "Nikriz ₅", "starting_interval": "R"},
            {"name": "Rast ₄", "starting_interval": "P5"},
            {"name": "Bûselik ₄", "starting_interval": "P5"},
        ]
    },
    # https://en.wikipedia.org/wiki/List_of_Turkish_makams
    "Neveser": {
        "tonic": "Rast",
        "ajnas": [
            {"name": "Nikriz ₅", "starting_interval": "R"},
            {"name": "Hicaz ₄", "starting_interval": "P5"},
        ]
    },
    "Saba": {  # TODO WIP https://en.wikipedia.org/wiki/Saba_(music)
        "tonic": "Dügâh",
        "ajnas": [
            {"name": "Saba ₄", "starting_interval": "R"},
            {"name": "Hicaz ₅", "starting_interval": "m3"},
        ]
    },
}
