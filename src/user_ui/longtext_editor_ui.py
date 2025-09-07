# -*- coding: utf-8 -*-
#
# Longtext Generator for KRL
# Copyright (C) 2025  Dennis Unger
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# --------------------------------------------------------------------
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


class longtext_editor(QWidget):
    def __init__(self):
        super().__init__()
      
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
