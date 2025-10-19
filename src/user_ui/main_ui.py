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

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QGridLayout,
    QGroupBox,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from PyQt6.QtGui import QAction
from PyQt6.QtCore import QStandardPaths

from core.kuka import Longtext
from user_ui.settings_ui import PrefixSettings,ConfigManager

DEFAULT_DIRECTORY = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(PROJECT_DIR, "longtext_config.json")

'''read my
    sort cuts
        LtG = Longtextgenerator
'''

class InfoDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Info")
        self.setFixedSize(300, 200)
        info_text = QLabel("""
                    Longtext Generator
                    
                    (c) 2025 by DU Software
                    
                    Version: V1.0.0.0 (Pre Relase)
                    """)
        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        self.buttons.rejected.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(info_text)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

class MainUi(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 100, 800, 450)
        self.setWindowTitle('Longtext Generator')
        self.setMaximumSize(1000, 800)
        
        
        self.core_ui = CoreUi(self)
        
        self.setCentralWidget(self.core_ui)

        self.menu_bar = self.menuBar()

        self.import_data_btn = QAction('Import Dat', self)
        self.import_data_btn.triggered.connect(self.get_file_names)
        self.import_data_btn.setCheckable(True)

        self.file_menu = self.menu_bar.addMenu('&File')
        self.file_menu.addAction(self.import_data_btn)
        self.file_menu.addSeparator()
        
        self.clen_longtext_btn = QAction('Clean Longtext', self)
        self.clen_longtext_btn.triggered.connect(self.clean_longtext)
        self.clen_longtext_btn.setCheckable(True)

        self.update_longtext_btn = QAction('Delete Empty Lines', self)
        self.update_longtext_btn.triggered.connect(self.delete_empty_lines_in_longtext)
        self.update_longtext_btn.setCheckable(True)

        self.merge_longtext_btn = QAction('Merge Longtext', self)
        #self.merge_longtext.triggered.connect()
        self.merge_longtext_btn.setCheckable(False)
        self.merge_longtext_btn.setEnabled(False)

        self.longtext_editor_btn = QAction('Longtext Editor', self)
        #self.merge_longtext.triggered.connect()
        self.longtext_editor_btn.setCheckable(False)
        self.longtext_editor_btn.setEnabled(False)

        self.check_longtext_btn = QAction('Check Longtext', self)
        self.check_longtext_btn.triggered.connect(self.check_longtext)
        self.check_longtext_btn.setCheckable(False)
        self.check_longtext_btn.setEnabled(False)

        self.tool_menu = self.menu_bar.addMenu('&Tools')
        self.tool_menu.addAction(self.clen_longtext_btn)
        self.tool_menu.addAction(self.update_longtext_btn)
        self.tool_menu.addAction(self.merge_longtext_btn)
        self.tool_menu.addAction(self.longtext_editor_btn)
        self.tool_menu.addSeparator()
        self.tool_menu.addAction(self.check_longtext_btn)
        self.tool_menu.addSeparator()

        
        self.setup_prefixes_btn = QAction('Setup Prefixes', self)
        self.setup_prefixes_btn.triggered.connect(self.setup_prefix)
        self.setup_prefixes_btn.setCheckable(True)
        
        self.info_btn = QAction('Info', self)
        self.info_btn.triggered.connect(self.show_info)
        self.info_btn.setCheckable(True)

        self.settings_menu = self.menu_bar.addMenu('&Settings')
        self.settings_menu.addAction(self.setup_prefixes_btn)
        self.settings_menu.addSeparator()
        self.settings_menu.addAction(self.info_btn)
        self.settings_menu.addSeparator()
        
        #self.statusBar().showMessage('Witing for Files...')

    def get_file_names(self):
        """get file names for import in the prozess
        """
        self.import_data_btn.setChecked(False)
        file_filter = 'Dat File (*.dat);; All Text Files (*)'
        #file_filter = 'Dat File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls);; Image File (*.png *.jpg)'
        response = QFileDialog.getOpenFileNames(
            parent = self,
            caption = 'Select File(s)',
            directory = DEFAULT_DIRECTORY,
            filter = file_filter,
        )
        print(response[0])
        print(len(response[0]))
        if len(response[0]) != 0:
            for item in response[0]:
                self.core_ui.file_handling.ui_files.addItem(QListWidgetItem(item))
                self.core_ui.file_handling.files.append(item)

    def clean_longtext(self):
        """get file names for import in the prozess
        """
        #longtext = LongtextTools()

        self.clen_longtext_btn.setChecked(False)

        file_filter = 'Longtext (*.csv);; Longtext (*.txt)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd(),
            filter=file_filter,
        )
        print(str(response[0]))

    def delete_empty_lines_in_longtext(self):
        """get file names for import in the prozess
        """
        self.update_longtext_btn.setChecked(False)
        print('Delete Empty Lines')

    def merge_longtext(self):
        """get file names for import in the prozess
        """
        self.merge_longtext_btn.setChecked(False)
        print('Merge Longtext')

    def longtext_editor(self):
        print('Longtext Editor')
        self.longtext_editor_btn.setChecked(False)

    def check_longtext(self):
        print('Check Longtext')
        self.check_longtext_btn.setChecked(False)

    def setup_prefix(self):
        self.setup_prefixes_btn.setChecked(False)
        self.core_ui.prefix_settings_ui.show()

    def show_info(self):
        info_page = InfoDialog()
        info_page.exec()
        self.info_btn.setChecked(False)

class CoreUi(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)
        
        #self.longtext_settings = Longtext().var_markings

        self.list_of_lontext_config = []

        self.prefix_settings_ui = PrefixSettings()
        self.file_handling = FileHandling()
        self.general_settings = GeneralSettings()
        self.prefixs_selection = ScanSelection()

        self.apply_btn = QDialogButtonBox(QDialogButtonBox.StandardButton.Apply)
        self.apply_btn.clicked.connect(self.start_process)
        
        layout.addWidget(self.file_handling, 0, 0)
        layout.addWidget(self.general_settings, 0, 1)
        layout.addWidget(self.prefixs_selection, 0, 2)
        layout.addWidget(self.apply_btn, 1, 0, 1, 3)
        
    def start_process(self):
        print('Start Prozess core')
        files = self.file_handling.files
        include_comments = self.general_settings.inclusion_comments.isChecked()
        del_var_prefixes = self.general_settings.del_var_prefixes.isChecked()
        del_empty_lines = self.general_settings.del_empty_lines.isChecked()
        expanded_interfase = self.general_settings.expanded_interfase.isChecked()
        export_log = self.general_settings.export_log.isChecked()
        selection = self.prefixs_selection.get_selection()
        prefixes = ConfigManager().lord_prefix()
        print(prefixes)
        
        if len(files) == 0:
            print('No files selected')
            return
        
        file_filter = 'Longtext (*.csv *.txt)'
        response = QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a Data File',
            directory= DEFAULT_DIRECTORY,
            filter=file_filter,
            initialFilter='Longtext (*.csv *.txt)'
            )
        directory = response[0].replace(response[0].split('/')[-1],'')
        file_name = response[0].split('/')[-1]

        if len(directory) == 0:
            print('Abort')
            return
        
        longtext = Longtext()
        raw_longtext = Longtext()
        longtext.create_template(expanded_interfase)
        raw_longtext.set_prefixes(prefixes)
        raw_longtext.set_selection(selection)
        raw_longtext.read_dat(files)
        ###raw_longtext.set_lt_settings(self.longtext_settings)
        raw_longtext.scan_data(include_comments)
        longtext.merge(raw_longtext)
        
        if del_empty_lines:
            longtext.del_empty_lines()
            
        if del_var_prefixes:
            longtext.del_präfixes()
            
        if export_log:
            longtext.check_for_double_declarations()
            longtext.export_log(file_name,directory)
            
        if (file_name[-4:] == '.Csv') or (file_name[-4:] == '.csv'.upper()) or (file_name[-4:] == '.csv'):
            longtext.export_csv(file_name,directory)
        elif (file_name[-4:] == '.Txt') or (file_name[-4:] == '.txt'.upper()) or (file_name[-4:] == '.txt'):
            longtext.export_txt(file_name,directory)
        else:
            print('Error wrong file format')

class FileHandling(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        
        self.setAcceptDrops(True)
        self.files = []
        self.list_of_drops = []
        
        self.setTitle('File Handling')
        self.setMinimumWidth(200)
        
        #Delete Item PushButten
        self.del_item_btn = QPushButton('Delete',self)
        self.del_item_btn.setCheckable(True)
        self.del_item_btn.setEnabled(True)
        self.del_item_btn.clicked.connect(self.delete_item)
        
        #Delete List PushButten
        self.clean_list_btn = QPushButton('Delete all',self)
        self.clean_list_btn.setCheckable(True)
        self.clean_list_btn.setEnabled(True)
        self.clean_list_btn.clicked.connect(self.clear_list)

        self.ui_files = QListWidget(self)
        self.ui_files.acceptDrops()
        self.ui_files.itemClicked.connect(self.clicked_list_event)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        layout.addWidget(self.ui_files)
        layout.addWidget(self.del_item_btn)
        layout.addWidget(self.clean_list_btn)

    def dragEnterEvent(self,event):
        print('Dragevent')
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dropEvent(self,event):
        print('DropEvent')
        file_urls = [url.toLocalFile() for url in event.mimeData().urls()]
        for file_url in file_urls:
            if file_url not in self.list_of_drops:
                self.list_of_drops.append(file_url)
        self.ui_files.clear()
        self.files.clear()
        for file_url in self.list_of_drops:
            self.ui_files.addItem(QListWidgetItem(file_url))
            self.files.append(file_url)
        print(self.list_of_drops)

    def clicked_list_event(self):
        SelectedItem = self.ui_files.item(self.ui_files.currentRow()).text()           
    def delete_item(self):
        print('DeleteItemButten = True')
        self.del_item_btn.setChecked(False)
        if len(self.ui_files) > 0:
            try:
                self.ui_files.takeItem(self.ui_files.currentRow())
                self.files.pop(self.ui_files.currentRow())
            except:
                pass
        print(self.files)
    def clear_list(self):
        print('DeleteListButten = True')
        self.clean_list_btn.setChecked(False)
        self.ui_files.clear()  
        self.files.clear() 
   
class GeneralSettings(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent=None)

        self.setTitle('General Settings')
        
        self.inclusion_comments = QCheckBox('Inclusion of Comments')
        self.del_var_prefixes = QCheckBox('Delete Signal Prefix (di,do,gi...)')
        self.del_empty_lines = QCheckBox('Create update Longtext (delete all empty lines)')
        self.expanded_interfase = QCheckBox('expanded Interfase (8192 Input,8192 Output)')
        self.export_log = QCheckBox('Export Log Dat')

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.inclusion_comments)
        layout.addWidget(self.del_var_prefixes)
        layout.addWidget(self.del_empty_lines)
        layout.addWidget(self.expanded_interfase)
        layout.addWidget(self.export_log)
        
        layout.addStretch()

class ScanSelection(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        
        self.prefixes_list = Longtext().var_markings
        
        self.setTitle('Prefix Selection')
        self.setMinimumWidth(175)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.markings = []
        line = 1
        for item in self.prefixes_list:
            if item.var_prefix:
                self.markings += [QCheckBox(f'{item.name}: {item.var_prefix}')]
            else:
                self.markings += [QCheckBox(f'{item.name}')]
            self.markings[-1].setCheckable(True)
            self.markings[-1].clicked.connect(self.set_lt_config)
            layout.addWidget(self.markings[-1])
            line += 1
        #Select All PushButten
        layout.addStretch()
        self.select_all_btn = QPushButton('Select All')
        self.select_all_btn.clicked.connect(self.select_all)
        layout.addWidget(self.select_all_btn)

        #Rest All PushButten
        self.reset_all_btn = QPushButton('Reset All',self)
        self.reset_all_btn.clicked.connect(self.reset_all)
        layout.addWidget(self.reset_all_btn)
        
    def set_lt_config(self):
        for i in range(len(self.prefixes_list)):
            self.prefixes_list[i].akriv = self.markings[i].isChecked()
            
    def build_lt_settings(self):
        pass
            
    def select_all(self):
        self.select_all_btn.setChecked(False)
        for item in self.markings:
            item.setChecked(True)
        self.set_lt_config()
        
    def reset_all(self):
        self.reset_all_btn.setChecked(False)
        for item in self.markings:
            item.setChecked(False) 
        self.set_lt_config()
        
    def get_selection(self):
        """get the current selection of the prefixs
        
        Returns:
            dict: dictionary with the current selection of the prefixs
        """
        selection = {}
        for i in range(len(self.prefixes_list)):
            selection[self.prefixes_list[i].name] = self.markings[i].isChecked()
        return selection
                    
app = QApplication([])
window = MainUi()
window.show()
app.exec()