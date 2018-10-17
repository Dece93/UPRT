import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4.phonon import *
from PyQt4.uic import *


app = QtGui.QApplication(sys.argv)
widget = loadUi(r'C:\Users\Julius De Cesaris\PycharmProjects\UPRT\stammdaten.ui')


widget.show()
sys.exit(app.exec_())


