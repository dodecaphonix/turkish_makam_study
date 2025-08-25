from constants import (
    AJINAS,
    NOTE_NAME_TO_COMMA,
    COMMA_TO_NOTE_NAME,
    JINS_STARTING_INTERVALS,
)


def hydrate_intervals_for_makam(makam):
    tonic_commas = NOTE_NAME_TO_COMMA[makam["tonic"]]
    makam["absolute_intervals"] = {}
    for i, jins in enumerate(makam["ajnas"]):
        jins_starting_interval = JINS_STARTING_INTERVALS[jins["starting_interval"]]
        jins["intervals"] = {}
        intervals = AJINAS[jins["name"]][:jins["pitch_count"]]
        jins_starting_commas = tonic_commas + jins_starting_interval.commas
        jins["starting_pitch"] = COMMA_TO_NOTE_NAME.get(jins_starting_commas, "")
        for interval in intervals:
            commas = interval.commas + jins_starting_commas
            jins["intervals"][commas] = str(interval)
            makam["absolute_intervals"][commas] = str(interval + jins_starting_interval)
    return makam
