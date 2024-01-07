from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class Single4(QWidget):
    def __init__(self, question, A, B, C, D, article, index, correct_answer:str):
        super().__init__()

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.question_text = question
        self.article_text = article

        self.index = index

        self.answer = ''
        self.correct_answer = correct_answer

        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout(self)

        self.verticalLayout = QVBoxLayout(self)

        self.choiceA = QRadioButton(self)
        self.choiceA.setMinimumSize(QtCore.QSize(150, 50))
        # self.choiceA.setMaximumSize(QtCore.QSize(200, 100))
        self.choiceA.setText(self.A)
        self.verticalLayout.addWidget(self.choiceA)

        def selectA():
            if self.choiceA.isChecked():
                self.answer = 'A'

        self.choiceA.clicked.connect(selectA)

        self.choiceB = QRadioButton(self)
        # self.choiceB.setMinimumSize(QtCore.QSize(150, 30))
        self.choiceB.setText(self.B)
        self.verticalLayout.addWidget(self.choiceB)

        def selectB():
            if self.choiceB.isChecked():
                self.answer = 'B'

        self.choiceB.clicked.connect(selectB)

        self.choiceC = QRadioButton(self)
        # self.choiceC.setMinimumSize(QtCore.QSize(150, 30))
        self.choiceC.setText(self.C)
        self.verticalLayout.addWidget(self.choiceC)

        def selectC():
            if self.choiceC.isChecked():
                self.answer = 'C'

        self.choiceC.clicked.connect(selectC)

        self.choiceD = QRadioButton(self)
        # self.choiceD.setMinimumSize(QtCore.QSize(150, 30))
        self.choiceD.setText(self.D)
        self.verticalLayout.addWidget(self.choiceD)

        def selectD():
            if self.choiceD.isChecked():
                self.answer = 'D'

        self.choiceD.clicked.connect(selectD)

        self.gridLayout.addItem(self.verticalLayout, 1, 0, 2, 2)

        self.question = QLabel(self)
        self.question.setText(self.question_text)
        self.gridLayout.addWidget(self.question, 0, 0, 1, 2)

        self.article = QTextBrowser(self)
        self.article.setMinimumWidth(600)
        self.article.setMaximumWidth(800)
        self.article.setMinimumHeight(800)
        self.article.setText(self.article_text)
        self.gridLayout.addWidget(self.article, 0, 2, 3, 1)

    def get_answers(self):
        if self.answer == self.correct_answer:
            flag = True
        else:
            flag = False

        return {self.index: [self.correct_answer, self.answer, flag]}


if __name__ == '__main__':
    app = QApplication([])

    w = Single4('Question', 'A', 'B', 'C', 'D', 'TEXT')
    w.show()

    exit(app.exec_())
