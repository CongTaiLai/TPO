from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtWidgets import *



class Multi4(QWidget):
    def __init__(self, question, A, B, C, D, article, index, correct_answer:list):
        super().__init__()

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.question_text = question
        self.article_text = article

        self.index = index

        self.answers = []
        self.correct_answer = correct_answer

        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout(self)

        self.verticalLayout = QVBoxLayout(self)

        self.tickA = QCheckBox(self)
        self.tickA.setMinimumSize(QtCore.QSize(150, 30))
        # self.tickA.setMaximumSize(QtCore.QSize(200, 100))
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

        self.gridLayout.addItem(self.verticalLayout, 1, 0, 2, 2)

        self.question = QLabel(self)
        self.question.setText(self.question_text)
        self.gridLayout.addWidget(self.question, 0, 0, 1, 2)

        self.article = QTextBrowser(self)
        # self.article.setMinimumSize(QtCore.QSize(250, 150))
        self.article.setMinimumWidth(600)
        self.article.setMaximumWidth(800)
        self.article.setMinimumHeight(800)
        self.article.setText(self.article_text)
        self.gridLayout.addWidget(self.article, 0, 2, 3, 1)

    def get_answers(self):
        self.answers.sort()
        if self.answers == self.correct_answer:
            flag = True
        else:
            flag = False

        return {self.index: [self.correct_answer, self.answers, flag]}


if __name__ == '__main__':
    app = QApplication([])

    w = Multi4('Question', 'A', 'B', 'C', 'D', 'TEXT')
    w.show()

    exit(app.exec_())
