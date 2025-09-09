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
import os
import json

from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QDialogButtonBox,
)

from PyQt6.QtCore import Qt

from core.kuka import Longtext

#from PyQt6.QtWidgets import QApplication #only for testing

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(PROJECT_DIR, "longtext_config.json")

DEFAULT_CONFIG = {
    'Prefixes_Settings': {
        'Digital Input': (),
        'Digital Output': (),
        'Analog Input': (),
        'Analog Output': (),
        'Grouped Input': (),
        'Grouped Output': (),
    },
}

class PrefixSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)
        prefix_settings = Longtext().var_markings
        self.setWindowTitle("Markings Settings")
        self.setGeometry(100, 100, 270, 300)
        self.setFixedSize(270, 300)
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'r') as f:
                config = json.load(f)
        else:
            with open(CONFIG_PATH,'w') as f:
                json.dump(DEFAULT_CONFIG, f ,indent=2)
                config = DEFAULT_CONFIG
            print('Longtext_Config.json not found. Created default config.')

        for key in config['Prefixes_Settings']:
            for item in prefix_settings:
                if item.name == key:
                    item.var_prefix = tuple(config['Prefixes_Settings'][key])
    
        self.markings_list = QTableWidget()
        self.markings_list.setRowCount(6)
        self.markings_list.setColumnCount(2)
        self.markings_list.setHorizontalHeaderLabels(['Name','Prefixes'])
        self.markings_list.setColumnWidth(1, 110)
        self.markings_list.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.markings_list.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        row = 0
        for item in prefix_settings:
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

        #layout = QVBoxLayout()
        layout.addWidget(self.markings_list, 0, 0)
        layout.addWidget(self.buttons, 1, 0)
        #self.setLayout(layout)
    def get_settings(self):
        pass
    def set_settings(self):
        pass
#app = QApplication([])
#window = PrefixSettings()
#window.show()
#app.exec()