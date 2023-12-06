from music21 import converter, analysis, interval, scale

# Path to your MIDI file
midi_path = 'melody_d_major.mid'

# Load the MIDI file
midi_data = converter.parse(midi_path)

# Analyzing the melody
key = midi_data.analyze('key')
melody = midi_data.recurse().notes
notes = [note.nameWithOctave for note in melody if note.isNote]
rhythms = [note.duration.quarterLength for note in melody if note.isNote]

# Interval Analysis
intervals = [interval.notesToChromatic(melody[i], melody[i+1]).semitones 
             for i in range(len(melody) - 1) if melody[i].isNote and melody[i+1].isNote]

# Scale Degree Analysis
scales = scale.Scale(key.tonic)
scale_degrees = [scales.getScaleDegreeFromPitch(note.pitch) for note in melody if note.isNote]

# Melody Contour Analysis
contours = []
for i in range(len(melody) - 1):
    if melody[i].isNote and melody[i+1].isNote:
        diff = melody[i+1].pitch.midi - melody[i].pitch.midi
        if diff > 0:
            contours.append('Rising')
        elif diff < 0:
            contours.append('Falling')
        else:
            contours.append('Static')

# Print analysis
print(f"Key: {key.name}")
print("First 10 Notes:", notes[:10])  # Displaying first 10 notes
print("Rhythms (first 10):", rhythms[:10])  # Displaying rhythms of first 10 notes
print("Intervals between Notes:", intervals[:10])  # Displaying intervals of first 10 notes
print("Scale Degrees:", scale_degrees[:10])  # Displaying scale degrees of first 10 notes
print("Melody Contours:", contours[:10])  # Displaying melody contours of first 10 notes