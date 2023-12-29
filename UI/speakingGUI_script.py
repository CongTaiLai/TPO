import os

from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *

from extract_text import Extract_text_speaking
import speakingGUI_generated


class Speaking_GUI(QStackedWidget, speakingGUI_generated.Ui_StackedWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.loadCb()
        self.getTest()

        self.index = 0

        # run signals
        self.navigate()
        self.comboBox.activated.connect(self.getTest)
        self.playerSignal()
        self.transcriptVisablity()

    # initialize combo box
    def loadCb(self):
        tests = eval(open('../SpeakingDatabase_formatted.txt').read())
        for t in tests:
            self.comboBox.addItem(str("TPO " + t))

    # switch between tasks
    def Refresh(self, i):
        self.setCurrentIndex(i)

    # transcript visability script
    def transcriptVisablity(self):
        # show or hide transcripts
        self.Transcript2.hide()
        self.Show2.clicked.connect(self.showTranscript2)

        self.Transcript3.hide()
        self.Show3.clicked.connect(self.showTranscript3)

        self.Transcript4.hide()
        self.Show4.clicked.connect(self.showTranscript4)

    # navigate script
    def navigate(self):
        def Next():
            self.index += 1
            self.Refresh(self.index)

        self.next0.clicked.connect(Next)
        self.next1.clicked.connect(Next)
        self.next2.clicked.connect(Next)
        self.next3.clicked.connect(Next)

        def Previous():
            self.index -= 1
            self.Refresh(self.index)

        self.previous1.clicked.connect(Previous)
        self.previous2.clicked.connect(Previous)
        self.previous3.clicked.connect(Previous)
        self.previous4.clicked.connect(Previous)

    # transcripts show and hide, scripts below
    def showTranscript2(self):
        if self.Show2.isChecked():
            self.Transcript2.show()
        else:
            self.Transcript2.hide()

    def showTranscript3(self):
        if self.Show3.isChecked():
            self.Transcript3.show()
        else:
            self.Transcript3.hide()

    def showTranscript4(self):
        if self.Show4.isChecked():
            self.Transcript4.show()
        else:
            self.Transcript4.hide()

    # extract text, update played audio
    def getTest(self):
        text = Extract_text_speaking.extract(int(self.comboBox.currentText().removeprefix("TPO ")))
        self.Article1.setText(text[0][0])
        self.Article2.setText(text[1][0])
        self.Article3.setText(text[2][0])
        self.Transcript2.setText(text[1][2])
        self.Transcript3.setText(text[2][2])
        self.Transcript4.setText(text[3][1])

        self.player2 = QMediaPlayer()
        self.player2.setMedia(
            QMediaContent(QtCore.QUrl.fromLocalFile(os.path.abspath(f'{os.getcwd().removesuffix("/UI")}{text[1][1]}'))))

        self.player3 = QMediaPlayer()
        self.player3.setMedia(
            QMediaContent(QtCore.QUrl.fromLocalFile(os.path.abspath(f'{os.getcwd().removesuffix("/UI")}{text[2][1]}'))))

        self.player4 = QMediaPlayer()
        self.player4.setMedia(
            QMediaContent(QtCore.QUrl.fromLocalFile(os.path.abspath(f'{os.getcwd().removesuffix("/UI")}{text[3][0]}'))))

        self.playerSignal()

    # player signals
    def playerSignal(self):
        self.Slider2.sliderMoved.connect(self.set_pos2)
        self.Slider2.sliderPressed.connect(self.set_pos_smooth2)
        self.player2.durationChanged.connect(self.update_dur2)
        self.player2.positionChanged.connect(self.update_pos2)

        self.Slider3.sliderMoved.connect(self.set_pos3)
        self.Slider3.sliderPressed.connect(self.set_pos_smooth3)
        self.player3.durationChanged.connect(self.update_dur3)
        self.player3.positionChanged.connect(self.update_pos3)

        self.Slider4.sliderMoved.connect(self.set_pos4)
        self.Slider4.sliderPressed.connect(self.set_pos_smooth4)
        self.player4.durationChanged.connect(self.update_dur4)
        self.player4.positionChanged.connect(self.update_pos4)

        self.Play2.clicked.connect(self.check_play_state2)
        self.Play3.clicked.connect(self.check_play_state3)
        self.Play4.clicked.connect(self.check_play_state4)

    # integrate sliders and players, scripts below
    def set_pos2(self, pos):
        self.player2.setPosition(pos)

    def set_pos3(self, pos):
        self.player3.setPosition(pos)

    def set_pos4(self, pos):
        self.player4.setPosition(pos)

    def set_pos_smooth2(self):
        self.player2.setPosition(self.Slider2.value())  # print(self.player2.media())

    def set_pos_smooth3(self):
        self.player3.setPosition(self.Slider3.value())

    def set_pos_smooth4(self):
        self.player4.setPosition(self.Slider4.value())

    def update_pos2(self, pos):
        self.Slider2.setValue(pos)
        if self.Slider2.value() == self.length2:
            self.Play2.setChecked(False)
        self.update_time_label2()

    def update_pos3(self, pos):
        self.Slider3.setValue(pos)
        if self.Slider3.value() == self.length3:
            self.Play3.setChecked(False)
        self.update_time_label3()

    def update_pos4(self, pos):
        self.Slider4.setValue(pos)
        if self.Slider4.value() == self.length4:
            self.Play4.setChecked(False)
        self.update_time_label4()

    def update_dur2(self, dur):
        self.Slider2.setRange(0, dur)
        self.length2 = dur
        self.update_time_label2()

    def update_dur3(self, dur):
        self.Slider3.setRange(0, dur)
        self.length3 = dur
        self.update_time_label3()

    def update_dur4(self, dur):
        self.Slider4.setRange(0, dur)
        self.length4 = dur
        self.update_time_label4()

    # play button script
    def check_play_state2(self):
        if self.Play2.isChecked() and self.Slider2.value() < self.length2:
            self.player2.play()
        elif self.Play2.isChecked() and self.Slider2.value() >= self.length2:
            self.player2.setPosition(0)
            self.Slider2.setValue(0)

        elif not self.Play2.isChecked():
            self.player2.pause()

    def check_play_state3(self):
        if self.Play3.isChecked() and self.Slider3.value() < self.length3:
            self.player3.play()
        elif self.Play3.isChecked() and self.Slider3.value() >= self.length3:
            self.player3.setPosition(0)
            self.Slider3.setValue(0)

        elif not self.Play3.isChecked():
            self.player3.pause()

    def check_play_state4(self):
        if self.Play4.isChecked() and self.Slider4.value() < self.length4:
            self.player4.play()
        elif self.Play4.isChecked() and self.Slider4.value() >= self.length4:
            self.player4.setPosition(0)
            self.Slider4.setValue(0)

        elif not self.Play4.isChecked():
            self.player4.pause()

    # update time labels
    def update_time_label2(self):
        pos = self.player2.position()
        dur = self.player2.duration()

        formatted_pos = "{:02}:{:02}".format(pos // 60000, (pos // 1000) % 60)
        formatted_dur = "{:02}:{:02}".format(dur // 60000, (dur // 1000) % 60)

        self.Timer2.setText(f"{formatted_pos} / {formatted_dur}")

    def update_time_label3(self):
        pos = self.player3.position()
        dur = self.player3.duration()

        formatted_pos = "{:02}:{:02}".format(pos // 60000, (pos // 1000) % 60)
        formatted_dur = "{:02}:{:02}".format(dur // 60000, (dur // 1000) % 60)

        self.Timer3.setText(f"{formatted_pos} / {formatted_dur}")

    def update_time_label4(self):
        pos = self.player4.position()
        dur = self.player4.duration()

        formatted_pos = "{:02}:{:02}".format(pos // 60000, (pos // 1000) % 60)
        formatted_dur = "{:02}:{:02}".format(dur // 60000, (dur // 1000) % 60)

        self.Timer4.setText(f"{formatted_pos} / {formatted_dur}")


if __name__ == '__main__':
    app = QApplication([])

    w = Speaking_GUI()
    w.show()

    exit(app.exec_())
