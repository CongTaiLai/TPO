from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class Multi6(QWidget):
    def __init__(self, A, B, C, D, E, F, article, index, correct_answer: list):
        super().__init__()

        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F

        self.article_text = article

        self.index = index

        self.answers = []
        self.correct_answer = correct_answer

        self.UI()

    def UI(self):
        self.horizontalLayout = QHBoxLayout(self)

        self.verticalLayout = QVBoxLayout(self)

        self.tickA = QCheckBox(self)
        self.tickA.setMinimumSize(QtCore.QSize(150, 50))
        # self.tickA.setMaximumSize(QtCore.QSize(200,100))
        self.tickA.setText(self.A)
        self.verticalLayout.addWidget(self.tickA)

        def checkA():
            if self.tickA.isChecked():
                self.answers.append('A')
            else:
                self.answers.remove('A')

        self.tickA.clicked.connect(checkA)

        self.tickB = QCheckBox(self)
        # self.tickB.setMinimumSize(QtCore.QSize(150, 30))
        self.tickB.setText(self.B)
        self.verticalLayout.addWidget(self.tickB)

        def checkB():
            if self.tickB.isChecked():
                self.answers.append('B')
            else:
                self.answers.remove('B')

        self.tickB.clicked.connect(checkB)

        self.tickC = QCheckBox(self)
        # self.tickC.setMinimumSize(QtCore.QSize(150, 30))
        self.tickC.setText(self.C)
        self.verticalLayout.addWidget(self.tickC)

        def checkC():
            if self.tickC.isChecked():
                self.answers.append('C')
            else:
                self.answers.remove('C')

        self.tickC.clicked.connect(checkC)

        self.tickD = QCheckBox(self)
        # self.tickD.setMinimumSize(QtCore.QSize(150, 30))
        self.tickD.setText(self.D)
        self.verticalLayout.addWidget(self.tickD)

        def checkD():
            if self.tickD.isChecked():
                self.answers.append('D')
            else:
                self.answers.remove('D')

        self.tickD.clicked.connect(checkD)

        self.tickE = QCheckBox(self)
        # self.tickE.setMinimumSize(QtCore.QSize(150, 30))
        self.tickE.setText(self.E)
        self.verticalLayout.addWidget(self.tickE)

        def checkE():
            if self.tickE.isChecked():
                self.answers.append('E')
            else:
                self.answers.remove('E')

        self.tickE.clicked.connect(checkE)

        self.tickF = QCheckBox(self)
        # self.tickF.setMinimumSize(QtCore.QSize(150, 30))
        self.tickF.setText(self.F)
        self.verticalLayout.addWidget(self.tickF)

        def checkF():
            if self.tickF.isChecked():
                self.answers.append('F')
            else:
                self.answers.remove('F')

        self.tickF.clicked.connect(checkF)

        self.horizontalLayout.addItem(self.verticalLayout)

        self.article = QTextBrowser(self)
        self.article.setText(self.article_text)
        self.article.setMinimumWidth(600)
        self.article.setMaximumWidth(800)
        self.article.setMinimumHeight(800)
        self.horizontalLayout.addWidget(self.article)

    def get_answers(self):
        self.answers.sort()
        if self.answers == self.correct_answer:
            flag = True
        else:
            flag = False

        return {self.index: [self.correct_answer, self.answers, flag]}


if __name__ == '__main__':
    app = QApplication([])

    w = Multi6('A', 'B', 'C', 'D', 'E', 'F', 'TEXT')
    w.show()

    exit(app.exec_())
