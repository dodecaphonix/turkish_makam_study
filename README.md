# Explore and display Turkish makams

For more info, see the [Turkish makam](https://en.wikipedia.org/wiki/Turkish_makam) Wikipedia article

## Install virtual env
Prerequisite: Install [Poetry](https://python-poetry.org/docs/) for dependency management

Crate a virtual environment with:
```
poetry install
```

## Run project

To view the web UI, use Poetry to spin up the webserver from within a virtual environment:
```
poetry run python app.py
```

Then, navigate to http://127.0.0.1:5000 in a web browser.

## Notation used

Intervals:
```
R = Root or Tonic   (of a jins/makam)
2 = Second degree   (of a jins/makam)
3 = Third degree    (of a jins/makam)
4 = Fourth degree   (of a jins/makam)
5 = Fifth degree    (of a jins/makam)
6 = Sixth degree    (of a jins/makam)
7 = Seventh degree  (of a jins/makam)
```

Qualities:
```
M = Major
m = Minor
P = Perfect
A = Augmented
D = Diminished
^ = Up by a comma
v = Down by a comma
```

## Some interval theory

This section is for the theory nerds. Don't worry if you don't understand it.

53 equal divisions of the octave (53EDO) does a phenomenal job of approximating 5-limit Just Intonation intervals.

The Pythagorean subset of Just intervals are nicely spaced with:
- Whole tone = 9 commas
- Semitone = 4 commas

Here we expand this to the Major Scale:
```
PR       M2       M3  P4       P5       M6       M7  PR
 R--------2--------3---4--------5--------6--------7---R
```

Let's use the 9,4 rule to find a Minor 3rd, then compare to Major. We can see that semitones acting as chromatic alterations are 5 commas rather than the 4:
```
PR       M2  m3       P4
 R--------2---3--------4 ...
 R--------2--------3---4 ...
PR       M2       M3  P4

             m3   M3
              3----3 (Five commas)
```

Here are all the main Pythagorean intervals using the 9,4 rule:
```
PR  m2   M2  m3   M3  P4       P5  m6   M6  m7   M7  PR
 R---2----2---3----3---4--------5---6----6---7----7---R
```
But what about the Just intervals like the 5:4 major 3rd, or the 6:5 minor third? That's a good question. I'm glad you asked...

In 53EDO, one comma is very close to the syntonic comma. The remaining justly tuned intervals are one comma away from their Pythagorean counterparts. Simply raise minor intervals by a comma and lower major intervals by a comma:
```
 PR  m2   M2  m3   M3  P4       P5  m6   M6  m7   M7  PR
 R---2----2---3----3---4--------5---6----6---7----7---R
 R----2--2-----3--3----4--------5----6--6-----7--7----R
 PR ^m2 vM2  ^m3 vM3  P4       P5  ^m6 vM6  ^m7 vM7   PR
```
And all together:
```
 R---22--22---33--33---4--------5---66--66---77--77---R
```

Let's see how some common ajinas line up:
```
 R---22--22---33--33---4
 R   --  -2   --  -3   4   Çârgâh = Major in Pythagorean tuning
 R   --  -2   --  3-   4     Rast = Major with vM3
 R   --  -2   3-  --   4  Bûselik = Minor in Pythagorean tuning
 R   --  2-   3-  --   4    Uşşâk = Minor with vM2
 R   2-  --   3-  --   4    Kürdî = Phrygian in Pythagorean tuning
 R   -2  --   --  3-   4    Hicaz = Phrygian Dominant with ^m2 and vM3
```

If we add in the neutral intervals found in middle eastern music, it starts to look a lot like the frets of many middle eastern instruments:
```
 R---222222---333333---4--------5---666666---777777---R
```
