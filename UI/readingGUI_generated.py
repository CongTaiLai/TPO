# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Taylor/Desktop/TPO_Scrape/UI/readingGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 300)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous = QtWidgets.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/Taylor/Desktop/TPO_Scrape/UI/res/previous.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous.setIcon(icon)
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.previous)
        self.questionNumber = QtWidgets.QLabel(Form)
        self.questionNumber.setObjectName("questionNumber")
        self.horizontalLayout.addWidget(self.questionNumber)
        self.next = QtWidgets.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/Taylor/Desktop/TPO_Scrape/UI/res/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon1)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.start = QtWidgets.QWidget()
        self.start.setObjectName("start")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.start)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.cb1 = QtWidgets.QComboBox(self.start)
        self.cb1.setObjectName("cb1")
        self.gridLayout_5.addWidget(self.cb1, 0, 1, 1, 1)
        self.cb2 = QtWidgets.QComboBox(self.start)
        self.cb2.setObjectName("cb2")
        self.gridLayout_5.addWidget(self.cb2, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.start)
        self.end = QtWidgets.QWidget()
        self.end.setObjectName("end")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.end)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.end)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.evaluation = QtWidgets.QLabel(self.end)
        self.evaluation.setObjectName("evaluation")
        self.horizontalLayout_2.addWidget(self.evaluation)
        self.stackedWidget.addWidget(self.end)
        self.gridLayout_4.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Correct answer"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "My answer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Stats"))
