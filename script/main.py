from Midi import Midi

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
