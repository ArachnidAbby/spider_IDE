import sys,json, os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat, QColor, QFontMetricsF
from PyQt5.QtWidgets import *
import Settings
import MainLayout
import Highlighting


# Creating the main window
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Spider IDE'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.showMaximized()
        self.activeDirectory = os.getcwd()

        with open(f'{Settings.EDITOR["Theme"]}/index.css') as f:
            self.setStyleSheet(f.read())

  
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        left_widget= MainLayout.LeftBar_Main(self)

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.tab_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        menu = MainLayout.MenuBar(self)
        #menu.create_toolbar()
  
        self.show()
    

  
# Creating tab widgets
class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
  
        # Initialize tab screen
        self.tabs = QTabWidget()
        # self.tab1 = QTextEdit()
        # self.tab2 = QWidget()
        # self.tab3 = QWidget()
        self.tabs.resize(300, 200)
        self.tabs.tabCloseRequested.connect(lambda index: self.tabs.removeTab(index))
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
  
        # Add tabs
        # self.tabs.addTab(self.tab1, "File1")
        # self.tabs.addTab(self.tab2, "File2")
        # self.tabs.addTab(self.tab3, "File3")
  
        # Create first tab
        #self.tab1.layout = QVBoxLayout(self)
        #self.tab1.setPlainText("Pog Champers My dude")
        # self.l = QLabel()
        # self.l.setText("This is the first tab")
        # self.tab1.layout.addWidget(self.l)
        #self.tab1.setLayout(self.tab1.layout)
  
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    
    def setup_editor(self):
        self.highlight.setDocument(self.tab1.document())


  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())