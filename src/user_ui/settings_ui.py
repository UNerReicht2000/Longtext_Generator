from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QDialogButtonBox

from PyQt6.QtCore import Qt

from core.kuka import Longtext

from PyQt6.QtWidgets import QApplication

class PrefixSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        prefix_settings = Longtext().var_markings
        self.setWindowTitle("Markings Settings")
        self.setGeometry(100, 100, 250, 300)
        self.setFixedSize(250, 300)

        self.markings_list = QTableWidget()
        self.markings_list.setRowCount(6)
        self.markings_list.setColumnCount(2)
        self.markings_list.setHorizontalHeaderLabels(['Name','Prefixes'])
        self.markings_list.setColumnWidth(1, 110)
        self.markings_list.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.markings_list.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        row = 0
        for item in Longtext().var_markings:
            name = QTableWidgetItem(item.name)
            name.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.markings_list.setItem(row, 0, name)
            if item.var_prefix:
                prefix = QTableWidgetItem(str(item.var_prefix).strip('(').strip(')'))
            else:
                prefix = QTableWidgetItem('')
            prefix.setToolTip("wiht ',' to separate multiple prefixes")
            self.markings_list.setItem(row, 1, prefix)
            row += 1

        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel)
        def save_settings():
            for i in range(self.markings_list.rowCount()):
                item = self.markings_list.item(i, 1)
                print(item.text())
                prefix_settings[i].var_prefix = tuple(item.text().split(','))
            self.close()
        self.buttons.accepted.connect(save_settings)
        self.buttons.rejected.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.markings_list)
        layout.addWidget(self.buttons)
        self.setLayout(layout)
       
#app = QApplication([])
#window = PrefixSettings()
#window.show()
#app.exec()