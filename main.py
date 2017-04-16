import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from buttons import buttonsWidget
from watchInfo import watchInfoWidget
class mainInterface(QWidget):
    def __init__(self):
        super().__init__()
        centralLayout = QVBoxLayout()
        mainLayout = QHBoxLayout()
        self.centralWidget = QStackedWidget()
        self.buttons = buttonsWidget(self)

        self.buttons.connectWatchButton.triggered.connect(self.watchConnect)

        vertLine = QFrame()
        vertLine.setFrameShape(QFrame.VLine)
        vertLine.setFrameShadow(QFrame.Sunken)

        centralLayout.addWidget(self.centralWidget)
        mainLayout.addWidget(self.buttons)
        mainLayout.addWidget(vertLine)
        mainLayout.addLayout(centralLayout)
        self.setLayout(mainLayout)

        self.resize(800, 600)
        self.setWindowTitle("Android Wear Tool")
        self.setWindowIcon(QIcon.fromTheme("application-rtf"))
        
    def watchConnect(self):
        self.buttons.connectWatchButton.setChecked(True)
        connectWidget = watchInfoWidget()
        self.centralWidget.addWidget(connectWidget)
        self.centralWidget.setCurrentWidget(connectWidget)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainInterface()

    ex.show()
    sys.exit(app.exec_())
