from midiutil.MidiFile import MIDIFile
import re

TPB = 480 # Ticks per beat

pitch_map = { 'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11 }
time_map = { '1/16': TPB // 4, '1/8': TPB // 2, '1/4': TPB // 1, '1/2': TPB * 2, '1': TPB * 4 }

class Midi:
    def __init__(self):
        self.sequence = MIDIFile(file_format = 0, ticks_per_quarternote = TPB, eventtime_is_ticks = True)
        self.sequence.addTrackName(0, 0, "")

    def add_note(self, pitch, position, duration, velocity):
        if isinstance(pitch, str):
            pitch = self.__note_name_to_number(pitch)
        if isinstance(position, str):
            position = self.__mbt_to_ticks(position)
        if isinstance(duration, str):
            duration = self.__time_to_ticks(duration)
        self.sequence.addNote(0, 0, pitch, position, duration, velocity)

    def __note_name_to_number(self, note_name):
        match = re.match(r'(?P<pitch>[a-gA-G])(?P<octave>\d)', note_name)
        pitch = int(pitch_map[match.group('pitch').upper()])
        octave = int(match.group('octave'))
        return 12 * (octave + 2) + pitch

    def __mbt_to_ticks(self, mbt):
        _mbt = mbt.split(':')
        m = int(_mbt[0])
        b = int(_mbt[1])
        t = int(_mbt[2])
        return ((m - 1) * (TPB * 4)) + ((b - 1) * TPB) + t

    def __time_to_ticks(self, time):
        return time_map[time]

    def write_to_file(self, path):
        with open(path, 'wb') as file:
            self.sequence.writeFile(file)
