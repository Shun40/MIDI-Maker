# MIDI-Maker
サクッとMIDIデータを作るためのPythonスクリプト。

### 必要なもの
* Python 3.7.0以上の実行環境
  * MIDIUtil<br>https://github.com/MarkCWirt/MIDIUtil

### 概要
Pythonで手軽にMIDIデータを作れます。自分用なので超手抜きです。

* MIDIノートを追加するとき、数値による指定と記号による指定ができます。

（例）音高C3の4分音符を、1小節目の1拍目に、ベロシティ100で追加
```
# 数値で指定
add_note(60, 0, 480, 100)
```
```
# 記号で指定
add_note('C3', '1:1:0', '1/4', 100)
```

### 実行例
```
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
```
