from sys import exit
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from darktheme.widget_template import DarkPalette
import db
import insert 
import search
import cmpdevice

labelFont = QFont("Times",18,italic=True)
buttonFont = QFont("Arial",14)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MusicApp")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setFixedSize(300, 370)
        self.db = db.DB()
        screen = QDesktopWidget().screenGeometry()
        x = int(screen.width()/2 - 300/2)
        y = int(screen.height()/2 - 370/2)
        self.move(x,y)

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        layout.setSpacing(20)

        label = QLabel("Welcome to MusicApp!")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(labelFont)
        layout.addWidget(label)

        btn1 = QPushButton("Insert Music")
        btn1.setFont(buttonFont)
        btn1.clicked.connect(self.switch_i)
        layout.addWidget(btn1)

        btn2 = QPushButton("Search and Edit")
        btn2.setFont(buttonFont)
        btn2.clicked.connect(self.switch_s)
        layout.addWidget(btn2)

        btn3 = QPushButton("Compare with a Device")
        btn3.setFont(buttonFont)
        btn3.clicked.connect(self.switch_c)
        layout.addWidget(btn3)

        self.topFrame = QFrame()
        self.topFrame.setFrameStyle(QFrame.Box)
        self.topFrame.setLineWidth(3)
        self.topFrame.setLayout(layout)
        self.topLayout = QVBoxLayout()
        self.topLayout.addWidget(self.topFrame)

        # Set the layout on the application's window
        self.setLayout(self.topLayout)

    def switch_i(self):
        insert.init(self.db)
        self.close()
        
    def switch_s(self):
        self.cams = search.SearchWindow()
        self.cams.show()
        self.close()

    def switch_c(self):
        self.cams = cmpdevice.CmpDeviceWindow()
        self.cams.show()
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    app.setPalette(DarkPalette())
    window = MainWindow()
    window.show()
    exit(app.exec_())
