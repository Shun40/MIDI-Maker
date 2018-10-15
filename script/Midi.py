from midiutil.MidiFile import MIDIFile
from mido import MidiFile
from enum import Enum
import re

# MIDIノートのパラメータ種類
class ParameterType(Enum):
    PITCH = 1
    POSITION = 2
    DURATION = 3
    VELOCITY = 4

# 4分音符分解能(Ticks Per Beat)
TPB = 480

# 正規表現による音高の記号表記フォーマット
PITCH_NOTATION = r'^(?P<pitch>[a-gA-G])(?P<accidental>[b#]?)(?P<octave>[+-]?[0-9])$'

# 正規表現による発音時刻の記号表記フォーマット
POSITION_NOTATION = r'^(?P<measure>\d+):(?P<beat>[1-4]):(?P<tick>\d+)$'

# 正規表現による音価(長さ)の記号表記フォーマット
DURATION_NOTATION = r'^(?P<duration>1/32|1/16|1/8|1/4|1/2|1)$'

# 正規表現によるベロシティの記号表記フォーマット
VELOCITY_NOTATION = r'^(?P<velocity>ppp|pp|p|mp|mf|f|ff|fff)$'

pitch_map = { 'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11 }
accidental_map = { 'b': -1, '': 0, '#': 1 }
duration_map = { '1/32': TPB // 8, '1/16': TPB // 4, '1/8': TPB // 2, '1/4': TPB, '1/2': TPB * 2, '1': TPB * 4 }
velocity_map = { 'ppp': 16, 'pp': 32, 'p': 48, 'mp': 64, 'mf': 80, 'f': 96, 'ff': 112, 'fff': 127 }
notation_map = {
    ParameterType.PITCH: PITCH_NOTATION,
    ParameterType.POSITION: POSITION_NOTATION,
    ParameterType.DURATION: DURATION_NOTATION,
    ParameterType.VELOCITY: VELOCITY_NOTATION
}

class Midi:
    def __init__(self):
        self.sequence = MIDIFile(file_format = 0, ticks_per_quarternote = TPB, eventtime_is_ticks = True)
        self.sequence.addTrackName(0, 0, "")

    def add_note(self, pitch, position, duration, velocity):
        if self.check_notation(pitch, ParameterType.PITCH):
            pitch = self.pitch_symbol_to_number(pitch)
        if self.check_notation(position, ParameterType.POSITION):
            position = self.position_symbol_to_number(position)
        if self.check_notation(duration, ParameterType.DURATION):
            duration = self.duration_symbol_to_number(duration)
        if self.check_notation(velocity, ParameterType.VELOCITY):
            velocity = self.velocity_symbol_to_number(velocity)
        self.sequence.addNote(0, 0, pitch, position, duration, velocity)

    @staticmethod
    def check_notation(parameter, parameter_type):
        _parameter = str(parameter)
        return re.match(notation_map[parameter_type], _parameter)

    @staticmethod
    def pitch_symbol_to_number(pitch):
        _pitch = str(pitch)
        match = re.match(PITCH_NOTATION, _pitch)
        pitch = pitch_map[match.group('pitch').upper()]
        offset = accidental_map[match.group('accidental')]
        octave = int(match.group('octave'))
        return 12 * (octave + 1) + pitch + offset

    @staticmethod
    def position_symbol_to_number(position):
        _position = str(position)
        match = re.match(POSITION_NOTATION, _position)
        measure = int(match.group('measure'))
        beat = int(match.group('beat'))
        tick = int(match.group('tick'))
        return ((measure - 1) * (TPB * 4)) + ((beat - 1) * TPB) + tick

    @staticmethod
    def duration_symbol_to_number(duration):
        _duration = str(duration)
        match = re.match(DURATION_NOTATION, _duration)
        return duration_map[match.group('duration')]

    @staticmethod
    def velocity_symbol_to_number(velocity):
        _velocity = str(velocity)
        match = re.match(VELOCITY_NOTATION, _velocity)
        return velocity_map[match.group('velocity')]

    def write_to_file(self, path):
        with open(path, 'wb') as file:
            self.sequence.writeFile(file)

    @staticmethod
    def show_midi_file(path):
        midi = MidiFile(path)
        for track in midi.tracks:
            print(track)
            for event in track:
                print(event)
