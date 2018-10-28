# MIDI-Maker
サクッとMIDIデータを作るためのPythonスクリプト。

### 必要なもの
* Python 3.7.0以上の実行環境
  * MIDIUtil<br>https://github.com/MarkCWirt/MIDIUtil

### 概要
Pythonで手軽にMIDIデータを作れます。自分用なので超手抜きです。

* フォーマットに従ってテキストファイルを記述し入力することで、MIDIシーケンスを作れます。

### パラメータ
* 音高
  * 音高を音名\<note_name\>または数値\<number\>で指定できます。
  * \<note_name\> : { C-1, C#-1, D-1, ..., B2, C3, C#3, ..., F9, F#9, G9 }
  * \<number\> : { 0, 1, 2, ..., 47, 48, 49, ..., 125, 126, 127 }
```
# C3を指定
C3 # 音名表記
48 # 数値表記
```

* 発音時刻（*p*）
  * 発音時刻をMBT形式\<mbt\>またはティック\<tick\>で指定できます。
  * TPB(Ticks per beat) = 480
```
# 2小節目先頭を指定
p=2:1:0 # MBT形式表記
p=1920  # ティック表記
```

* 音価（*d*）
  * 音価を音符表記\<note_duration\>またはティック\<tick\>で指定できます。
  * TPB(Ticks per beat) = 480
```
# 4分音符長を指定
d=1/4 # 音符表記
d=480 # ティック表記
```

* ベロシティ（*v*）
  * ベロシティを強弱記号\<accent_symbol\>または数値\<number\>で指定できます。
  * \<accent_symbol\> : { ppp, pp, p, mp, mf, f, ff, fff } <--> { 16, 32, 48, 64, 80, 96, 112, 127 }
  * \<number\> : { 0, 1, 2, ..., 125, 126, 127 }
```
# ベロシティ値96を指定
v=f  # 強弱記号表記
v=96 # 数値表記
```

* BPM（*bpm*）
  * BPMを数値<number>で指定できます。
```
# BPMを114に指定
bpm=114
```

### パラメータの記述
パラメータは改行して1つずつ記述できます。
```
p=2:1:0
d=1/4
v=f
```
発音時刻、音価、ベロシティについては、カンマ区切りで1行にまとめて記述できます。
```
p=2:1:0,d=1/4,v=f
```

### 実行例
テキストファイル（sample.txt）
```
p=1:1:0,d=1/4,v=f
C3
D3
E3
F3
G3
A3
B3
C4

```
コマンド
```
$ python3 src/main.py -if input/sample.txt  -of output/sample.mid
BPM 120 at tick 0
NoteOn 48 at tick 0 duration 480 ch 0 vel 96
NoteOff 48 at tick 480 ch 0 vel 96
NoteOn 50 at tick 480 duration 480 ch 0 vel 96
NoteOff 50 at tick 960 ch 0 vel 96
NoteOn 52 at tick 960 duration 480 ch 0 vel 96
NoteOff 52 at tick 1440 ch 0 vel 96
NoteOn 53 at tick 1440 duration 480 ch 0 vel 96
NoteOff 53 at tick 1920 ch 0 vel 96
NoteOn 55 at tick 1920 duration 480 ch 0 vel 96
NoteOff 55 at tick 2400 ch 0 vel 96
NoteOn 57 at tick 2400 duration 480 ch 0 vel 96
NoteOff 57 at tick 2880 ch 0 vel 96
NoteOn 59 at tick 2880 duration 480 ch 0 vel 96
NoteOff 59 at tick 3360 ch 0 vel 96
NoteOn 60 at tick 3360 duration 480 ch 0 vel 96
NoteOff 60 at tick 3840 ch 0 vel 96
```
