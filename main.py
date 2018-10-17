import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4.phonon import *
from PyQt4.uic import *


app = QtGui.QApplication(sys.argv)
widget = loadUi(r'C:\Users\Julius De Cesaris\PycharmProjects\UPRT\monitor.ui')

#Gopro Video
media1 = Phonon.MediaSource(r'C:\Users\Julius De Cesaris\Desktop\GoPro\GP011658.MP4')
widget.GoPro.load(media1)
widget.GoPro.play()

#Eye Tracker Video
media2 = Phonon.MediaSource(r'C:\Users\Julius De Cesaris\Desktop\GoPro\Screen_Video_EyeTracking.mp4')
widget.EyeTracker.load(media2)
widget.EyeTracker.play()

#Heart Frequency
media3 = Phonon.MediaSource(r'C:\Users\Julius De Cesaris\Desktop\GoPro\heartrate.mp4')
widget.HeartFrequency.load(media3)
widget.HeartFrequency.play()



"""
class Debriefingtool(QDialog):
    def __init__(self):
        super(Debriefingtool, self).__init__()
        loadUi("pyqt4.ui", self)
        self.setWindowTitle("Debriefingtool for ZAV")

"""


widget.show()
sys.exit(app.exec_())


