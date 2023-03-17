from pysynth_b import *

song = [("E5", 2), ("D#5", 2), ("E5", 2), ("D#5", 2),
        ("E5", 2), ("B4", 2), ("D5", 2), ("C#5", 2),
        ("A4", 4), ("A4", 4), ("B4", 4), ("C#5", 4),
        ("D5", 2), ("E5", 2), ("G#4", 2), ("G4", 2),
        ("F#4", 2), ("E4", 2), ("D#4", 2), ("E4", 2)]

make_wav(song, bpm=120, fn="golden_dreams_piano.wav", soundfont='FluidR3_GM.sf2')
