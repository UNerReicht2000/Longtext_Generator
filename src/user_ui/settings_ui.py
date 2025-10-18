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

from pprint import pprint

from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QTableWidget,
    QTableWidgetItem,
    QDialogButtonBox,
)

from PyQt6.QtCore import Qt

from core.kuka import Longtext

from PyQt6.QtWidgets import QApplication

TEST_MODE = False

class ConfigManager():
    def __init__(self):
        self.PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.CONFIG_PATH = os.path.join(self.PROJECT_DIR, "longtext_config.json")
        self.WITH_LIST = ['Default','Prefix_Settings']
        
        prefix_settings = {}
        for i in Longtext().var_markings:
            prefix_settings[i.name] = i.var_prefix

        self.DEFAULT_CONFIG = {
            'Prefix_Settings': prefix_settings,
        }
        
        self.config = self.DEFAULT_CONFIG
    
        if os.path.exists(self.CONFIG_PATH):
            with open(self.CONFIG_PATH, 'r') as f:
                self.config = json.load(f)
        else:
            with open(self.CONFIG_PATH,'w') as f:
                json.dump(self.DEFAULT_CONFIG, f ,indent=2)
                self.config = self.DEFAULT_CONFIG
            print('Longtext_Config.json not found. Created default config.')
    
    def dump(self):
        
        with open(self.CONFIG_PATH,'w') as f:
            json.dump(self.config, f, indent=2)
    
    def loed(self):
        if os.path.exists(self.CONFIG_PATH):
            with open(self.CONFIG_PATH, 'r') as f:
                self.config = json.load(f)
        else:
            with open(self.CONFIG_PATH,'w') as f:
                json.dump(self.DEFAULT_CONFIG, f, indent=2)
                self.config = self.DEFAULT_CONFIG
            print('Longtext_Config.json not found. Created default config.')
        return self.config
    
    def lord_prefix(self):
        self.loed()
        prefix_config = self.config['Prefix_Settings']
        for i in prefix_config:
            prefix_config[i] = tuple(prefix_config[i])
            
        return prefix_config

class PrefixSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        config_manager = ConfigManager()
        
        layout = QGridLayout()
        self.setLayout(layout)
            
        self.setWindowTitle("Markings Settings")
        self.setGeometry(100, 100, 270, 300)
        self.setFixedSize(270, 300)
        
        self.markings_list = QTableWidget()
        self.markings_list.setRowCount(6)
        self.markings_list.setColumnCount(2)
        self.markings_list.setHorizontalHeaderLabels(['Name','Prefixes'])
        self.markings_list.setColumnWidth(1, 110)
        self.markings_list.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.markings_list.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        temp_config = config_manager.lord_prefix()
        row = 0
        for key in temp_config:
            name = QTableWidgetItem(key)
            name.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.markings_list.setItem(row, 0, name)
            if temp_config[key]:
                prefix = QTableWidgetItem(str(temp_config[key]).strip('(').strip(')').replace("'",'').removesuffix(','))
                print(prefix.text())
            else:
                prefix = QTableWidgetItem('')
            prefix.setToolTip("wiht ';' to separate multiple prefixes")
            self.markings_list.setItem(row, 1, prefix)
            row += 1

        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel)
        def save_settings():
            prefix_settings = {}
            for i in range(self.markings_list.rowCount()):
                key = self.markings_list.item(i, 0).text()
                item = self.markings_list.item(i, 1).text()
                #if key in prefix_settings:
                prefix_settings[key] = tuple(item.split(';'))
                prefix_settings[key] = tuple(x for x in prefix_settings[key] if x != '' or x.isalpha())
                print(f'Key: {key} item: {item}')    
                
            config_manager.config['Prefix_Settings'] = prefix_settings
            config_manager.dump()


            self.close()
        self.buttons.accepted.connect(save_settings)
        self.buttons.rejected.connect(self.close)

        layout.addWidget(self.markings_list, 0, 0)
        layout.addWidget(self.buttons, 1, 0)

if TEST_MODE:
    app = QApplication([])
    window = PrefixSettings()
    window.show()
    app.exec()