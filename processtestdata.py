from PyQt4 import QtGui, QtCore
import sys
from os.path import isdir, join
from makefile import makefile
from datetime import datetime

class ProcessTestData(QtGui.QWidget):
    """docstring for ProcessTestData"""
    def __init__(self, parent=None):
        super (ProcessTestData, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setFixedSize(500,260)
        self.audio_line = QtGui.QLineEdit()
        self.audio_line.setFixedWidth(350)
        self.gonogo_line = QtGui.QLineEdit()
        self.gonogo_line.setFixedWidth(350)
        self.save_line = QtGui.QLineEdit()
        self.save_line.setFixedWidth(350)
        self.audio_button = QtGui.QPushButton("Browse")
        self.audio_button.setFixedWidth(120)
        self.gonogo_button = QtGui.QPushButton("Browse")
        self.gonogo_button.setFixedWidth(120)
        self.save_button = QtGui.QPushButton("Browse")
        self.save_button.setFixedWidth(120)
        self.submit = QtGui.QPushButton("Submit")
        
        self.status = QtGui.QStatusBar()
        self.status.setSizeGripEnabled(False)
        
        self.audio_layout = QtGui.QHBoxLayout()
        self.audio_layout.addWidget(self.audio_line)
        self.audio_layout.addWidget(self.audio_button)
        self.gonogo_layout = QtGui.QHBoxLayout()
        self.gonogo_layout.addWidget(self.gonogo_line)
        self.gonogo_layout.addWidget(self.gonogo_button)
        self.save_layout = QtGui.QHBoxLayout()
        self.save_layout.addWidget(self.save_line)
        self.save_layout.addWidget(self.save_button)
        
        self.audio_text = QtGui.QStatusBar()
        self.audio_text.showMessage('Audio Results Directory:')
        self.audio_text.setSizeGripEnabled(False)
        self.gonogo_text = QtGui.QStatusBar()
        self.gonogo_text.showMessage('GoNoGo Results Directory:')
        self.gonogo_text.setSizeGripEnabled(False)
        self.save_dir = QtGui.QStatusBar()
        self.save_dir.showMessage('Save Path:')
        self.save_dir.setSizeGripEnabled(False)
        
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.audio_text)
        self.layout.addLayout(self.audio_layout)
        self.layout.addWidget(self.gonogo_text)
        self.layout.addLayout(self.gonogo_layout)
        self.layout.addWidget(self.save_dir)
        self.layout.addLayout(self.save_layout)
        self.layout.addWidget(self.submit)
        self.layout.addWidget(self.status)
        
        self.setLayout(self.layout)
        
        self.submit.pressed.connect(self.check_valid)
        self.audio_button.pressed.connect(self.audio_pressed)
        self.gonogo_button.pressed.connect(self.gonogo_pressed)
        self.save_button.pressed.connect(self.save_pressed)
        
        
        
    def check_valid(self):
        valid = True
        if not isdir(self.save_line.text()):
            self.status.showMessage('Please enter a save path for the output files.', 5000)
            return
        if not isdir(self.audio_line.text()) and not self.audio_line.text() == '':
            self.status.showMessage('Invalid Audio Directory.', 5000)
            valid = False
        if not isdir(self.gonogo_line.text()) and not self.gonogo_line.text() == '':
            self.status.showMessage('Invalid GoNoGo Directory.', 5000)
            valid = False
        if not isdir(self.audio_line.text()) and not self.audio_line.text() == '' and not isdir(self.gonogo_line.text()) and not self.gonogo_line.text() == '':
            self.status.showMessage('Invalid Audio & GoNoGo Directories.', 5000)
            valid = False
        if valid:
            self.status.showMessage('')
            self.submit_process()

    def get_dir(self, param):
        dirname = str(QtGui.QFileDialog.getExistingDirectory(self, 'Select ' + param + ' Directory'))
        
        if isdir(dirname):
            if param == 'Audio':
                self.audio_line.setText(dirname)
            elif param == 'GoNoGo':
                self.gonogo_line.setText(dirname)
            elif param == 'Save':
                self.save_line.setText(dirname)
                
    def audio_pressed(self):
        self.get_dir('Audio')
        
    def gonogo_pressed(self):
        self.get_dir('GoNoGo')
        
    def save_pressed(self):
        self.get_dir('Save')
        
    def submit_process(self):
        now = datetime.now()
        
        timestr = str(now.day) + '-' + str(now.month) + '-' + str(now.year) \
                  + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second)
                  
        if not self.audio_line.text() == '':
            makefile('audio', str(self.save_line.text() + '/Audio-' + timestr), \
                     str(self.audio_line.text()))
        if not self.gonogo_line.text() == '':
            makefile('gonogo', str(self.save_line.text() + '/GoNoGo-' + timestr), \
                     str(self.gonogo_line.text()))
        self.close()
        


def main():
    """ PURPOSE: Creates app and runs widget """
    # Create the Qt Application
    app = QtGui.QApplication(sys.argv)
    # Create and show the form
    session = ProcessTestData()
    session.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
            
if __name__ == '__main__':
    main()   