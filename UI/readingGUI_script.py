from PyQt5.QtWidgets import *

import readingGUI_generated
from reading_components import multi4, multi6, single4


class Reading_GUI(QWidget, readingGUI_generated.Ui_Form):
    def __init__(self):
        super().__init__()
        self.index = 0
        # self.test = 69
        self.stats = []

        self.setupUi(self)
        self.previous.setEnabled(False)
        self.loadCb()
        self.dynamic_script()
        self.refreshTest()
        self.refresh()

    def loadCb(self):
        tests = eval(open('../get_indexes/read_indexes.txt').read())
        for t in tests:
            self.cb1.addItem(str("TPO " + t))
        for i in range(1, 4):
            self.cb2.addItem(str("test " + str(i)))

    def refreshTest(self):
        self.cb1.activated.connect(self.refresh)
        self.cb2.activated.connect(self.refresh)

    def refresh(self):
        count = len(self.stackedWidget) - 2

        for i in range(count):
            self.stackedWidget.removeWidget(self.stackedWidget.widget(1))

        self.db = eval(open(
            f'../downloaded_resources/Reading/TPO{self.cb1.currentText().removeprefix("TPO ")}_{self.cb2.currentText().removeprefix("test ")}.txt').read())
        for q in self.db:
            i = self.db.index(q)
            if i == len(self.db) - 1:
                page = multi6.Multi6(q[1], q[2], q[3], q[4],
                                     q[5], q[6], q[0], i + 1, [i for i in q[-1]])
                self.stackedWidget.insertWidget(i + 1, page)
            elif i == len(self.db) - 2:
                page = single4.Single4(q[1], 'A', 'B', 'C', 'D', q[0], i + 1, q[-1])
                self.stackedWidget.insertWidget(i + 1, page)

            else:
                if len(q[-1]) > 1:
                    page = multi4.Multi4(q[1], q[2], q[3], q[4], q[5], q[0], i + 1, [i for i in q[-1]])
                    self.stackedWidget.insertWidget(i + 1, page)
                else:
                    page = single4.Single4(q[1], q[2], q[3], q[4], q[5], q[0], i + 1, q[-1])
                    self.stackedWidget.insertWidget(i + 1, page)

    def dynamic_script(self):
        self.next.clicked.connect(self.next_action)
        self.previous.clicked.connect(self.previous_action)
        self.stackedWidget.currentChanged.connect(self.checkEnable)

    def previous_action(self):
        if self.index > 0:
            self.index -= 1
            self.stackedWidget.setCurrentIndex(self.index)

    def next_action(self):
        if self.index < len(self.stackedWidget) - 1:
            self.index += 1
            self.stackedWidget.setCurrentIndex(self.index)
            # if self.index == len(self.stackedWidget) - 1:
            #     self.next.setEnabled(False)

        if self.stackedWidget.currentIndex() == len(self.stackedWidget) - 1:
            for i in range(len(self.db)):
                self.stats.append(self.stackedWidget.widget(i + 1).get_answers())

            for x in self.stats:
                d = x.popitem()
                self.tableWidget.setItem(d[0] - 1, 0, QTableWidgetItem(str(d[1][0])))
                self.tableWidget.setItem(d[0] - 1, 1, QTableWidgetItem(str(d[1][1])))
                self.tableWidget.setItem(d[0] - 1, 2, QTableWidgetItem(str(d[1][2])))
                print(str(d[1][0]))

    def checkEnable(self):
        if self.index==0:
            self.previous.setEnabled(False)
        else:
            self.previous.setEnabled(True)
        if self.index==len(self.stackedWidget)-1:
            self.next.setEnabled(False)

if __name__ == '__main__':
    app = QApplication([])

    w = Reading_GUI()
    w.show()

    exit(app.exec_())
