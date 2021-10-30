import re, toml
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QSyntaxHighlighter, QTextCharFormat

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._mapping = {}
    
    def add_mapping(self, pattern, pattern_format):
        self._mapping[pattern] = pattern_format
    
    def highlightBlock(self, text_block):
        for pattern, fmt in self._mapping.items():
            for match in re.finditer(pattern, text_block):
                start, end = match.span()
                self.setFormat(start,end-start, fmt)

def ReadFromFile(filename, theme):
    with open(filename) as f:
        file = toml.loads(f.read())
    highlighter = Highlighter()
    for x in file["Rules"].keys():
        j = file["Rules"][x]
        class_format = QTextCharFormat()
        #print(j["Color"])
        class_format.setForeground(QColor(theme[j["Color"]]))
        highlighter.add_mapping(j["Rule"],class_format)
    return highlighter
