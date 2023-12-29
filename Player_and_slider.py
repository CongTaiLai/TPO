from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt


class Main_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
        self.length = 0

    def UI(self):
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(
            QUrl.fromLocalFile("/Users/Taylor/Library/Application Support/JetBrains/PyCharm2023.2/scratches/test.mp3")))

        self.layout_ = QVBoxLayout()

        self.btn = QPushButton(self)
        self.btn.setCheckable(True)

        self.btn.clicked.connect(self.check_play_state)

        self.slider = QSlider(self)
        self.slider.setOrientation(Qt.Horizontal)

        self.slider.sliderMoved.connect(self.set_pos)
        self.slider.sliderPressed.connect(self.set_pos_smooth)
        self.player.durationChanged.connect(self.update_dur)
        self.player.positionChanged.connect(self.update_pos)

        self.label = QLabel("00:00 / 00:00")

        self.layout_.addWidget(self.btn)
        self.layout_.addWidget(self.slider)
        self.layout_.addWidget(self.label)
        self.setLayout(self.layout_)

    def set_pos(self, pos):
        self.player.setPosition(pos)

    def set_pos_smooth(self):
        # self.player.pause()
        self.player.setPosition(self.slider.value())
        # self.player.play()

    def update_pos(self, pos):
        self.slider.setValue(pos)
        if self.slider.value() == self.length:
            self.btn.setChecked(False)
        self.update_time_label()

    def update_dur(self, dur):
        self.slider.setRange(0, dur)
        self.length = dur
        self.update_time_label()

    def check_play_state(self):
        if self.btn.isChecked() and self.slider.value() < self.length:
            self.player.play()
        elif self.btn.isChecked() and self.slider.value() >= self.length:
            self.player.setPosition(0)
            self.slider.setValue(0)

        elif not self.btn.isChecked():
            self.player.pause()

    def update_time_label(self):
        pos = self.player.position()
        dur = self.player.duration()

        formatted_pos = "{:02}:{:02}".format(pos // 60000, (pos // 1000) % 60)
        formatted_dur = "{:02}:{:02}".format(dur // 60000, (dur // 1000) % 60)

        self.label.setText(f"{formatted_pos} / {formatted_dur}")


if __name__ == '__main__':
    App = QApplication([])
    w = Main_widget()
    w.show()
    exit(App.exec_())
