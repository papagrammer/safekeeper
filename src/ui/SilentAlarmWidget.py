# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SilentAlarmWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SilentAlarmWidget(object):
    def setupUi(self, SilentAlarmWidget):
        SilentAlarmWidget.setObjectName("SilentAlarmWidget")
        SilentAlarmWidget.resize(209, 120)
        self.label = QtWidgets.QLabel(SilentAlarmWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(SilentAlarmWidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 10, 111, 70))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.OKButton = QtWidgets.QPushButton(SilentAlarmWidget)
        self.OKButton.setGeometry(QtCore.QRect(120, 90, 80, 23))
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(SilentAlarmWidget)
        self.CancelButton.setGeometry(QtCore.QRect(30, 90, 80, 23))
        self.CancelButton.setObjectName("CancelButton")

        self.retranslateUi(SilentAlarmWidget)
        QtCore.QMetaObject.connectSlotsByName(SilentAlarmWidget)

    def retranslateUi(self, SilentAlarmWidget):
        _translate = QtCore.QCoreApplication.translate
        SilentAlarmWidget.setWindowTitle(_translate("SilentAlarmWidget", "Silent Alarm"))
        self.label.setText(_translate("SilentAlarmWidget", "Description:"))
        self.OKButton.setText(_translate("SilentAlarmWidget", "Alarm"))
        self.CancelButton.setText(_translate("SilentAlarmWidget", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SilentAlarmWidget = QtWidgets.QWidget()
    ui = Ui_SilentAlarmWidget()
    ui.setupUi(SilentAlarmWidget)
    SilentAlarmWidget.show()
    sys.exit(app.exec_())
