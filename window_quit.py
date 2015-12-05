#!/usr/bin/python
__author__ = 'daniele'

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
              QtGui.QMainWindow.__init__(self)

              self.setWindowTitle('Pulsanti')

              button = QtGui.QPushButton('Quit');
              button.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold));
              self.connect(button, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'));

              self.setCentralWidget(button);

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())