import os

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import writingGUI_generated
from PyQt5.QtCore import QUrl, Qt


class Writing_GUI(QWidget, writingGUI_generated.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadCb()

        self.refresh()

        self.length = 0
        self.cb.activated.connect(self.refresh)

        self.dynamic_player()
        self.Transcript.hide()

        self.Show.clicked.connect(self.transcriptVisability)

    def loadCb(self):
        tests = eval(open('../get_indexes/write_indexes.txt').read())
        for test in tests:
            self.cb.addItem(str('TPO' + test))

    def transcriptVisability(self):
        if self.Show.isChecked():
            self.Transcript.show()
        else:
            self.Transcript.hide()

    def refresh(self):
        listening_path = str(os.getcwd().replace('/UI',
                                                 '') + '/downloaded_resources/Writing/Listening/' + self.cb.currentText() + '.mp3')
        self.player = QMediaPlayer()
        # self.player.setMedia(QMediaContent(QUrl.fromLocalFile(listening_path)))
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile('/Users/Taylor/Desktop/TPO_Scrape/downloaded_resources/Writing/Listening/TPO69.mp3')))
        # self.player.setMedia(QMediaContent(QUrl.fromLocalFile(str(os.path.abspath(f'{os.getcwd().removesuffix("/UI")}//Users/Taylor/Desktop/TPO_Scrape/downloaded_resources/Writing/Listening/{self.cb.currentText()}.mp3')))))


        reading = open(str(os.getcwd().replace('/UI',
                                               '') + '/downloaded_resources/Writing/Reading/' + self.cb.currentText() + '.txt')).read()
        self.Article.setText(reading)

        transcripts = open(str(os.getcwd().replace('/UI',
                                                   '') + '/downloaded_resources/Writing/Transcripts/' + self.cb.currentText() + '.txt')).read()
        self.Transcript.setText(transcripts)

    def dynamic_player(self):
        self.Slider.sliderMoved.connect(self.set_pos)
        self.Slider.sliderPressed.connect(self.set_pos_smooth)
        self.player.durationChanged.connect(self.update_dur)
        self.player.positionChanged.connect(self.update_pos)
        self.Play.clicked.connect(self.check_play_state)

    def set_pos(self, pos):
        self.player.setPosition(pos)

    def set_pos_smooth(self):
        # self.player.pause()
        self.player.setPosition(self.Slider.value())
        # self.player.play()

    def update_pos(self, pos):
        self.Slider.setValue(pos)
        if self.Slider.value() == self.length:
            self.Play.setChecked(False)
        self.update_time_label()

    def update_dur(self, dur):
        self.Slider.setRange(0, dur)
        self.length = dur
        self.update_time_label()

    def check_play_state(self):
        if self.Play.isChecked() and self.Slider.value() < self.length:
            self.player.play()
        elif self.Play.isChecked() and self.Slider.value() >= self.length:
            self.player.setPosition(0)
            self.Slider.setValue(0)

        elif not self.Play.isChecked():
            self.player.pause()

    def update_time_label(self):
        pos = self.player.position()
        dur = self.player.duration()

        formatted_pos = "{:02}:{:02}".format(pos // 60000, (pos // 1000) % 60)
        formatted_dur = "{:02}:{:02}".format(dur // 60000, (dur // 1000) % 60)

        self.Timer.setText(f"{formatted_pos} / {formatted_dur}")


if __name__ == '__main__':
    app = QApplication([])

    w = Writing_GUI()
    w.show()

    exit(app.exec_())
