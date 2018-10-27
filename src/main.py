from Midi import Midi

def example():
    """
    ♪ スピッツ / 空も飛べるはず
    """
    midi = Midi()

    midi.add_note('G3', '1:3:240', '1/8', 'f')
    midi.add_note('C4', '1:4:0', '1/8', 'f')
    midi.add_note('D4', '1:4:240', '1/8', 'f')

    midi.add_note('E4', '2:1:0', '1/4', 'f')
    midi.add_note('E4', '2:2:0', '1/4', 'f')
    midi.add_note('D4', '2:3:0', '1/8', 'f')
    midi.add_note('E4', '2:3:240', '1/8', 'f')
    midi.add_note('F4', '2:4:0', '1/4', 'f')

    midi.add_note('E4', '3:1:0', '1/4', 'f')
    midi.add_note('C4', '3:2:240', '1/8', 'f')
    midi.add_note('C4', '3:3:0', '1/2', 'f')

    midi.add_note('A4', '4:1:0', '1/4', 'f')
    midi.add_note('A4', '4:2:0', '1/4', 'f')
    midi.add_note('B3', '4:3:0', '1/8', 'f')
    midi.add_note('C4', '4:3:240', '1/8', 'f')
    midi.add_note('D4', '4:4:0', '1/8', 'f')
    midi.add_note('A4', '4:4:240', '1/8', 'f')

    midi.add_note('A4', '5:1:0', '1/8', 'f')
    midi.add_note('G4', '5:1:240', '1/8', 'f')
    midi.add_note('E4', '5:2:0', '1/8', 'f')
    midi.add_note('G4', '5:2:240', '1/4', 'f')
    midi.add_note('F4', '5:3:240', '1/4', 'f')
    midi.add_note('G4', '5:4:240', '1/8', 'f')

    midi.write_to_file('output/soramotoberuhazu.mid')

if __name__ == '__main__':
    midi = Midi()

    # 数値でノートのパラメータを指定
    midi.add_note(48, 240, 240, 96)
    midi.add_note(50, 960, 480, 96)
    midi.add_note(52, 1440, 480, 80)
    midi.add_note(50, 120, 240, 80)
    midi.add_note(52, 720, 240, 96)

    # 記号でノートのパラメータを指定
    midi.add_note('C3', '2:1:240', '1/8', 'f')
    midi.add_note('D3', '2:3:0', '1/4', 'f')
    midi.add_note('E3', '2:4:0', '1/4', 'mf')
    midi.add_note('D3', '2:1:120', '1/8', 'mf')
    midi.add_note('E3', '2:2:240', '1/8', 'f')

    midi.write_to_file('output/output.mid')
