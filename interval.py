DEGREES = 7
INTERVALS_ORDERED_4THS = [0, 3, 6, 2, 5, 1, 4]  # 0 is 7 % 7
PERFECT_INTERVALS = INTERVALS_ORDERED_4THS[4:]  # 5, 1, 4 are perfect
TONIC_INDEX = INTERVALS_ORDERED_4THS.index(1)

W = 9  # Pythagorean whole tone
H = 4  # Pythagorean semitone
COMMA_IN_4TH = W + W + H  # 22 commas (53EDO Perfect 4th)
COMMA_IN_OCT = W + W + H + W + W + W + H  # 53 commas (53EDO Major scale)


class Interval:
    def __init__(self, degree, accidental=0, comma_displacement=0, octave_displacement=0):
        self._num_4th = INTERVALS_ORDERED_4THS.index(degree % DEGREES) - TONIC_INDEX - accidental * DEGREES
        self.accidental = (self._num_4th + TONIC_INDEX) // DEGREES
        self.degree = degree
        self._comma_displacement = comma_displacement
        self._octave_displacement = octave_displacement
        self._is_perfect = self.degree % DEGREES in PERFECT_INTERVALS
        self.commas = (
                (COMMA_IN_4TH * self._num_4th) % COMMA_IN_OCT
                + (degree // (DEGREES + 1) * COMMA_IN_OCT)
                + comma_displacement
                + (octave_displacement * COMMA_IN_OCT)
        )

    def __repr__(self):
        class_name = type(self).__name__
        return (
            f"{class_name}(degree={self.degree}, accidental={self.accidental}, "
            f"comma_displacement={self._comma_displacement}, octave_displacement={self._octave_displacement})"
        )

    def __str__(self):
        # TODO: Figure out best way to limit compound intervals (hard coded non_compound_degree for now)
        non_compound_degree = (self.degree - 1) % DEGREES + 1
        return f"{self._comma_displacement_to_string()}{self._accidental_to_str()}{non_compound_degree}"

    def __add__(self, other):
        new_degree = self.degree + other.degree - 1
        new_comma_displacement = self._comma_displacement + other._comma_displacement
        octave_displacement = self._octave_displacement + other._octave_displacement
        new_interval = Interval(
            degree=new_degree,
            comma_displacement=new_comma_displacement,
            octave_displacement=octave_displacement,
        )
        new_interval._num_4th = self._num_4th + other._num_4th
        new_interval.accidental = (new_interval._num_4th + TONIC_INDEX) // DEGREES

        return new_interval

    def _comma_displacement_to_string(self):
        """
        Returns commas up/down portion of an Interval: ^, v
        """
        return "^" * self._comma_displacement if self._comma_displacement > 0 else "v" * abs(self._comma_displacement)

    def _accidental_to_str(self) -> str:
        """
        Returns the quality portion of an Interval: P, M, m, A, D
        """
        if self._is_perfect:
            if self.accidental < 0:
                string = 'A' * abs(self.accidental)
            elif self.accidental > 0:
                string = 'D' * self.accidental
            else:
                string = 'P'
        else:
            if self.accidental < 0:
                string = 'A' * abs(self.accidental)
            elif self.accidental == 1:
                string = 'm'
            elif self.accidental > 1:
                string = 'D' * (self.accidental - 1)
            else:
                string = 'M'
        return string
