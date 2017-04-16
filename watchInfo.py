from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class watchInfoWidget(QWidget):
    def __init__(self, parent=None):
        super(watchInfoWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.instructions = QLabel("Connect your watch and click \'connect\'")
        self.connectButton = QAction(self)
        self.connectButton.setText("Connect")

        self.toolBar = QToolBar()
        self.addAction(self.connectButton)

        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.instructions)
        layout.addWidget(self.toolBar)
        self.setLayout(layout)

