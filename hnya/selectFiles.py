# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os, sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(402, 144)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 90, 110, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 361, 20))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setObjectName(_fromUtf8("label"))
        #MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.openFile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", u"Выбрать файл", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
class Win(QtGui.QDialog,Ui_MainWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'),"")
        self.label.setText(_translate("MainWindow", filename, None))
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MWindow = Win()
    MWindow.show()
    sys.exit(app.exec_())


