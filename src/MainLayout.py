from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Highlighting, Main, Settings

class LeftBar_Main(QWidget):
    def __init__(self,main_window):
        super().__init__()

        self.btn_1 = QPushButton('Files', main_window)
        self.btn_2 = QPushButton('Git', main_window)
        self.btn_3 = QPushButton('Project Settings', main_window)
        self.btn_4 = QPushButton('Addons', main_window)

        self.btn_1.setObjectName('left_button')
        self.btn_2.setObjectName('left_button')
        self.btn_3.setObjectName('left_button')
        self.btn_4.setObjectName('left_button')

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        self.setLayout(left_layout)

class MenuBar(QMenuBar):
    def __init__(self,main_window):
        super().__init__()
        self.create_toolbar(main_window)
        self.main_window = main_window
    
    def create_toolbar(self,main_window):
        menuBar = QMenuBar(main_window)
        fileMenu = QMenu("&File", main_window)
        self.newAction = QAction("&New",main_window)
        # Creating actions using the second constructor
        self.openAction = QAction("&Open...", main_window)
        self.saveAction = QAction("&Save", main_window)
        self.exitAction = QAction("&Exit", main_window)
        self.copyAction = QAction("&Copy", main_window)
        self.pasteAction = QAction("&Paste", main_window)
        self.cutAction = QAction("C&ut", main_window)
        self.helpContentAction = QAction("&Help Content", main_window)
        self.aboutAction = QAction("&About", main_window)

        self.openAction.triggered.connect(lambda checked: self.file_open(checked))
        self.saveAction.triggered.connect(lambda checked: self.file_save(checked))


        self.openAction.setShortcut("Ctrl+Shift+O")
        self.saveAction.setShortcut("Ctrl+S")
        #self.openAction.trigger()

        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        fileMenu.addAction(self.copyAction)
        fileMenu.addAction(self.pasteAction)
        fileMenu.addAction(self.cutAction)


        menuBar.addMenu(fileMenu)
        main_window.setMenuBar(menuBar)

    def file_open(self,checked):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        #file.setFilter()
        filenames = []
        if file.exec_():
            #print(Settings.Highlighting)
            filesnames = file.selectedFiles()
            for file in filesnames:
                with open(file) as f:
                    tab = FileTab(self.main_window.tab_widget,Settings.Highlighting, path = file)
                    tab.setPlainText(f.read())
                    z = self.main_window.tab_widget.tabs.addTab(tab,filesnames[0].split('/')[-1])
                    self.main_window.tab_widget.tabs.setCurrentIndex(z)
    
    def file_save(self,checked):
        active = self.main_window.tab_widget.tabs.currentIndex()
        current = self.main_window.tab_widget.tabs.currentWidget()
        with open(f"{current.path}",'w') as f:
            f.write(self.main_window.tab_widget.tabs.currentWidget().toPlainText())
            current.save()

class FileTab(QTextEdit):
    def __init__(self,widget,highlighting, path=None):
        super().__init__()
        self.layout = QVBoxLayout(widget)
        #self.setLayout(self.layout)
        self.highlight = Highlighting.ReadFromFile('src/styles/languages/Python.toml',highlighting)
        self.setTabStopDistance(
            QFontMetricsF(self.font()).horizontalAdvance(' ') * 4)

        self.setPlainText("#Test Comment")
        self.autoFormatting()
        self.setup_editor()

        self.path = path
        self.saved=True
        self.widget = widget

        self.textChanged.connect(self.changed)
    
    def setup_editor(self):
        self.highlight.setDocument(self.document())
    
    def changed(self):
        id = self.widget.tabs.indexOf(self)
        current = self.widget.tabs.tabText(id)
        if not '~' in current: self.widget.tabs.setTabText(id,f'~{current}')

    
    def save(self):
        id = self.widget.tabs.indexOf(self)
        current = self.widget.tabs.tabText(id)
        self.widget.tabs.setTabText(id,f'{current}'.replace('~',''))