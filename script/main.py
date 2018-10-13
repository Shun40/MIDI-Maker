from Midi import Midi

if __name__ == '__main__':
    midi = Midi()

    # 数値でノートのパラメータを指定
    midi.add_note(60, 240, 240, 100)
    midi.add_note(62, 960, 480, 100)
    midi.add_note(64, 1440, 480, 100)
    midi.add_note(62, 120, 240, 100)
    midi.add_note(64, 720, 240, 100)

    # 記号でノートのパラメータを指定
    midi.add_note('C3', '2:1:240', '1/8', 100)
    midi.add_note('D3', '2:3:0', '1/4', 100)
    midi.add_note('E3', '2:4:0', '1/4', 100)
    midi.add_note('D3', '2:1:120', '1/8', 100)
    midi.add_note('E3', '2:2:240', '1/8', 100)

    midi.write_to_file('output/output.mid')
