from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os

class buttonsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        layout = QVBoxLayout()

        self.connectWatchButton = QAction(self)
        self.connectWatchButton.setText("Connect to Watch")
        self.connectWatchButton.setIcon(QIcon.fromTheme("project-open"))
        self.connectWatchButton.setCheckable(True)

        self.installApkButton = QAction(self)
        self.installApkButton.setText("Install APK")
        self.installApkButton.setIcon(QIcon.fromTheme("document-new"))
        self.installApkButton.setCheckable(True)

        self.viewInstalledButton = QAction(self)
        self.viewInstalledButton.setText("View/Uninstall Apks")
        self.viewInstalledButton.setIcon(QIcon.fromTheme("document-new"))
        self.viewInstalledButton.setCheckable(True)


        self.toolBar = QToolBar()
        self.toolBar.setIconSize(QSize(16, 16))
        self.toolBar.setToolButtonStyle(3)
        self.toolBar.setOrientation(0x2)
        self.toolBar.addAction(self.connectWatchButton)
        self.toolBar.addAction(self.installApkButton)
        self.toolBar.addAction(self.viewInstalledButton)

        bGroup = QActionGroup(self)
        bGroup.addAction(self.connectWatchButton)
        bGroup.addAction(self.installApkButton)
        bGroup.addAction(self.viewInstalledButton)
        
        layout.addWidget(self.toolBar)
        layout.setAlignment(Qt.AlignVCenter)
        self.setLayout(layout)

