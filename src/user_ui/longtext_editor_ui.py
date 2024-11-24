# -*- coding: utf-8 -*-
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QGroupBox
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QListWidget
from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFileDialog


class longtext_editor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.longtexts        
        self.setGeometry(300,100,500,700)
        self.setWindowTitle('Longtext Editor')
        self.setAcceptDrops(True)

        self.resizeEvent = self.on_resize

    def on_resize(self, event):
        size = self.size()
        print(f"Aktuelle Größe: Breite={size.width()}, Höhe={size.height()}")
        super().resizeEvent(event)

app = QApplication([])
longtext_editor_test = longtext_editor()
longtext_editor_test.show()
app.exec()
