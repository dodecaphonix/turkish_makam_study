from constants import (
    AJINAS,
    COMMA_TO_INTERVAL,
    COMMAS_PER_OCTAVE,
    INTERVAL_TO_COMMA,
    NOTE_NAME_TO_COMMA,
)


def hydrate_intervals_for_makam(makam):
    makam["absolute_intervals"] = {}
    for i, jins in enumerate(makam["ajnas"]):
        jins["intervals"] = {}
        intervals = AJINAS[jins["name"]][:jins["pitch_count"]]
        for interval in intervals:
            commas = INTERVAL_TO_COMMA[interval] + NOTE_NAME_TO_COMMA[jins["starting_pitch"]]
            jins["intervals"][commas] = interval
            # TODO: This will be buggy for enharmonics E.G. a diminished 4th
            makam["absolute_intervals"][commas] = COMMA_TO_INTERVAL.get((commas - NOTE_NAME_TO_COMMA[makam["tonic"]]) % COMMAS_PER_OCTAVE, "")
    return makam
