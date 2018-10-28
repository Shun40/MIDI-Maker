from midiutil.MidiFile import MIDIFile

class Sequence:
    """
    MIDIシーケンスのクラス
    """
    TPB = 480 # 4分音符分解能(Ticks Per Beat)
    DEFAULT_BPM = 120 # デフォルトBPM

    def __init__(self):
        """
        コンストラクタ
        """
        self.sequence = MIDIFile(file_format = 0, ticks_per_quarternote = Sequence.TPB, eventtime_is_ticks = True)
        self.set_tempo(Sequence.DEFAULT_BPM)


    def set_tempo(self, bpm = DEFAULT_BPM):
        """
        MIDIシーケンスのテンポをセットする

        Parameters
        ----------
        bpm : int
            BPM
        """
        # すでにテンポイベントが登録されていたらそのイベントを削除する
        for event in self.sequence.tracks[0].eventList:
            if event.evtname == 'Tempo':
                self.sequence.tracks[0].eventList.remove(event)
        # 新しいBPM値でテンポイベントをセット
        self.sequence.addTempo(0, 0, bpm)


    def add_note(self, pitch, position, duration, velocity):
        """
        MIDIシーケンスへノートイベントを追加する

        Parameters
        ----------
        pitch : int
            ノートナンバー
        position : int
            発音時刻
        duration : int
            音価(発音時間長)
        velocity : int
            ベロシティ
        """
        self.sequence.addNote(0, 0, pitch, position, duration, velocity)


    def show(self):
        """
        MIDIシーケンスが持つ全MIDIイベントを表示する
        """
        for track in self.sequence.tracks:
            for event in track.eventList:
                if event.evtname == 'Tempo':
                    bpm = int(60000000 / event.tempo)
                    tick = event.tick
                    print('BPM {} at tick {}'.format(bpm, tick))
                else:
                    print(event)


    def write_to_file(self, path):
        """
        MIDIシーケンスの内容をファイルに書き込む

        Parameters
        ----------
        path : str
            MIDIファイルのファイルパス
        """
        with open(path, 'wb') as file:
            self.sequence.writeFile(file)
