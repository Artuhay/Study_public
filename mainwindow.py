# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 584)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 901, 561))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Suicide_family")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.treshhold_input = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Suicide_family")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.treshhold_input.setFont(font)
        self.treshhold_input.setObjectName("treshhold_input")
        self.verticalLayout_2.addWidget(self.treshhold_input)
        self.thresh_text = QtWidgets.QPlainTextEdit(self.widget)
        self.thresh_text.setObjectName("treshhold_input")
        self.verticalLayout_2.addWidget(self.thresh_text)


        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")


        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Suicide_family")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listView = QtWidgets.QListView(self.widget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)


        self.label_3= QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Suicide_family")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.listView1 = QtWidgets.QListView(self.widget)
        self.listView1.setObjectName("listView1")
        self.verticalLayout.addWidget(self.listView1)



        #self.label_3 = QtWidgets.QLabel(self.widget)
        # font = QtGui.QFont()
        # font.setFamily("Microsoft New Tai Lue")
        # font.setPointSize(11)
        # font.setBold(True)
        # font.setWeight(75)
        #self.label_3.setFont(font)
        #self.label_3.setObjectName("label_3")
        #self.verticalLayout.addWidget(self.label_3)
        #self.listView_2 = QtWidgets.QListView(self.widget)
        #self.listView_2.setObjectName("listView_2")
        #self.verticalLayout.addWidget(self.listView_2)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Suicide_family")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Message for analizing:"))
        self.treshhold_input.setText(_translate("MainWindow", "Threshold:"))
        self.label_2.setText(_translate("MainWindow", "Watson output:"))
        self.label_3.setText(_translate("MainWindow", "Chance of suicide:"))

        self.pushButton.setText(_translate("MainWindow", "Check suicide"))


