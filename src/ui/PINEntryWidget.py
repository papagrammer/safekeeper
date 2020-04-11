# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PINEntryWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PINEntryWidget(object):

    def __init__(self, ctx, callback):
        self.ctx = ctx
        self.callback = callback

    def _cancel_click(self):
        self.callback(False)
        self.__window.close()

    def _ok_click(self):
        self.callback(True)
        self.__window.close()

    def setupUi(self, PINEntryWidget):
        self.__window = PINEntryWidget

        PINEntryWidget.setObjectName("PINEntryWidget")
        PINEntryWidget.resize(245, 87)
        self.PINPromptText = QtWidgets.QLabel(PINEntryWidget)
        self.PINPromptText.setGeometry(QtCore.QRect(10, 10, 64, 21))
        self.PINPromptText.setObjectName("PINPromptText")
        self.OKButton = QtWidgets.QPushButton(PINEntryWidget)
        self.OKButton.setGeometry(QtCore.QRect(160, 60, 83, 25))
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(PINEntryWidget)
        self.CancelButton.setGeometry(QtCore.QRect(70, 60, 83, 25))
        self.CancelButton.setObjectName("CancelButton")
        self.PINEntryInput = QtWidgets.QLineEdit(PINEntryWidget)
        self.PINEntryInput.setGeometry(QtCore.QRect(80, 10, 113, 25))
        self.PINEntryInput.setText("")
        self.PINEntryInput.setObjectName("PINEntryInput")

        # click listeners
        self.OKButton.clicked.connect(self._ok_click)
        self.CancelButton.clicked.connect(self._cancel_click)

        self.retranslateUi(PINEntryWidget)
        QtCore.QMetaObject.connectSlotsByName(PINEntryWidget)

    def retranslateUi(self, PINEntryWidget):
        _translate = QtCore.QCoreApplication.translate
        PINEntryWidget.setWindowTitle(_translate("PINEntryWidget", "Enter PIN"))
        self.PINPromptText.setText(_translate("PINEntryWidget", "Enter PIN:"))
        self.OKButton.setText(_translate("PINEntryWidget", "OK"))
        self.CancelButton.setText(_translate("PINEntryWidget", "Cancel"))

