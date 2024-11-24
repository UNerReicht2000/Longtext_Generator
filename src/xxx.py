from PyQt6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import sys

from dev_func import debug_print

class DragDropTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                with open(file_path, 'r') as file:
                    self.append(file.read())
            event.acceptProposedAction()
        else:
            super().dropEvent(event)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.textEdit = DragDropTextEdit(self)
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        self.setLayout(layout)

        self.setWindowTitle('Drag and Drop Beispiel')
        self.setGeometry(100, 100, 600, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())