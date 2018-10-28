from enum import Enum
import re
from Sequence import Sequence

class ParameterType(Enum):
    """
    イベントのパラメータ
    """
    PITCH = 1
    POSITION = 2
    DURATION = 3
    VELOCITY = 4
    BPM = 5

# 音高の記号表記フォーマット
PITCH_NOTATION = r'^(?P<pitch>[a-gA-G])(?P<accidental>[b#]?)(?P<octave>[+-]?[0-9])$'

# 発音時刻の記号表記フォーマット
POSITION_NOTATION = r'^(?P<measure>\d+):(?P<beat>[1-4]):(?P<tick>\d+)$'

# 音価(発音時間長)の記号表記フォーマット
DURATION_NOTATION = r'^(?P<duration>1/32|1/32.|1/16|1/16.|1/8|1/8.|1/4|1/4.|1/2|1/2.|1)$'

# ベロシティの記号表記フォーマット
VELOCITY_NOTATION = r'^(?P<velocity>ppp|pp|p|mp|mf|f|ff|fff)$'

pitch_map = {
    'C': 0,
    'D': 2,
    'E': 4,
    'F': 5,
    'G': 7,
    'A': 9,
    'B': 11
}

accidental_map = {
    'b': -1,
    '': 0,
    '#': 1
}

duration_map = {
    '1/32': Sequence.TPB // 8,
    '1/32.': Sequence.TPB // 8 + Sequence.TPB // 16,
    '1/16': Sequence.TPB // 4,
    '1/16.': Sequence.TPB // 4 + Sequence.TPB // 8,
    '1/8': Sequence.TPB // 2,
    '1/8.': Sequence.TPB // 2 + Sequence.TPB // 4,
    '1/4': Sequence.TPB,
    '1/4.': Sequence.TPB + Sequence.TPB // 2,
    '1/2': Sequence.TPB * 2,
    '1/2.': Sequence.TPB * 2 + Sequence.TPB,
    '1': Sequence.TPB * 4
}

velocity_map = {
    'ppp': 16,
    'pp': 32,
    'p': 48,
    'mp': 64,
    'mf': 80,
    'f': 96,
    'ff': 112,
    'fff': 127
}

def make_sequence(path):
    sequence = Sequence()

    pitch = 48
    position = 0
    duration = Sequence.TPB
    velocity = 100

    commands = read_commands_from_file(path)
    for command in commands:
        type, value = get_type_and_value(command)
        if type == ParameterType.PITCH:
            pitch = value
            sequence.add_note(pitch, position, duration, velocity)
            position += duration
        elif type == ParameterType.POSITION:
            position = value
        elif type == ParameterType.DURATION:
            duration = value
        elif type == ParameterType.VELOCITY:
            velocity = value
        elif type == ParameterType.BPM:
            bpm = value
            sequence.set_tempo(bpm)

    return sequence


def get_type_and_value(command):
    type = None
    value = None
    if '=' in command:
        type_and_value = command.split('=')
        type = get_type_from_label(type_and_value[0])
        value = get_numeric_value(type, type_and_value[1])
    else:
        type = ParameterType.PITCH
        value = get_numeric_value(type, command)
    return type, value


def get_type_from_label(type_label):
    if type_label in ['p', 'P']:
        return ParameterType.POSITION
    elif type_label in ['d', 'D']:
        return ParameterType.DURATION
    elif type_label in ['v', 'V']:
        return ParameterType.VELOCITY
    elif type_label in ['bpm', 'BPM']:
        return ParameterType.BPM


def get_numeric_value(type, value):
    # そもそも数字だったらint型に変換して返す
    if value.isdecimal():
        return int(value)

    if type == ParameterType.PITCH:
        return get_numeric_pitch_value(value)
    elif type == ParameterType.POSITION:
        return get_numeric_position_value(value)
    elif type == ParameterType.DURATION:
        return get_numeric_duration_value(value)
    elif type == ParameterType.VELOCITY:
        return get_numeric_velocity_value(value)


def get_numeric_pitch_value(value):
    match = re.match(PITCH_NOTATION, value)
    pitch = pitch_map[match.group('pitch').upper()]
    offset = accidental_map[match.group('accidental')]
    octave = int(match.group('octave'))
    return 12 * (octave + 1) + pitch + offset


def get_numeric_position_value(value):
    match = re.match(POSITION_NOTATION, value)
    measure = int(match.group('measure'))
    beat = int(match.group('beat'))
    tick = int(match.group('tick'))
    return ((measure - 1) * (Sequence.TPB * 4)) + ((beat - 1) * Sequence.TPB) + tick


def get_numeric_duration_value(value):
    match = re.match(DURATION_NOTATION, value)
    return duration_map[match.group('duration')]


def get_numeric_velocity_value(value):
    match = re.match(VELOCITY_NOTATION, value)
    return velocity_map[match.group('velocity')]


def read_commands_from_file(path):
    """
    MIDIシーケンス作成コマンドをファイルから読み込む

    Parameters
    ----------
    path : str
        テキストファイルのファイルパス

    Returns
    -------
    commands : list
        コマンド群
    """
    commands = []
    with open(path, 'r') as file:
        commands = [line.strip() for line in file.readlines()] # 改行削除
    _commands = []
    for command in commands:
        for _command in command.split(','):
            _commands.append(_command)
    return _commands
