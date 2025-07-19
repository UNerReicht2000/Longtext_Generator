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

class MarkingsSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Markings Settings")
        self.setGeometry(100, 100, 400, 300)

        # Create UI elements
        self.markings_list = QListWidget()
        self.add_marking_button = QPushButton("Add Marking")
        self.remove_marking_button = QPushButton("Remove Marking")
        self.save_button = QPushButton("Save Settings")
        self.load_button = QPushButton("Load Settings")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Markings:"))
        layout.addWidget(self.markings_list)
        layout.addWidget(self.add_marking_button)
        layout.addWidget(self.remove_marking_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)
        self.setLayout(layout)

        # Connect signals
        #self.add_marking_button.clicked.connect(self.add_marking)
        #self.remove_marking_button.clicked.connect(self.remove_marking)
        #self.save_button.clicked.connect(self.save_settings)
        #self.load_button.clicked.connect(self.load_settings)
    pass

app = QApplication([])
window = MarkingsSettings()
window.show()
app.exec()