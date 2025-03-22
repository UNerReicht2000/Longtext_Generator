# -*- coding: utf-8 -*-

from dev_func import debug_print
from dev_func import print_list

from os import getcwd

from PyQt6.QtWidgets import QMainWindow
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

from PyQt6.QtGui import QAction

from src.core.process import LongtextTools




    #-------------------- 
    class menu_bar_ui(Me):
        """menubar ui
        """
        def __init__(self):
            super().__init__()
            #button_action = QAction(QIcon("bug.png"), "&Your button", self)
            self.import_data_button = QAction('Import Dat', self)
            #self.import_data_button.setStatusTip("Import VarXXX.dat")
            self.import_data_button.triggered.connect(self.get_file_names)
            self.import_data_button.setCheckable(True)

            self.menu = self.menuBar()

            self.file_menu = self.menu.addMenu('&File')
            self.file_menu.addAction(self.import_data_button)
            self.file_menu.addSeparator()

            self.clen_longtext = QAction('Clean Longtext', self)
            self.clen_longtext.triggered.connect(self.clean_longtext)
            self.clen_longtext.setCheckable(True)

            self.update_longtext = QAction('Delete Empty Lines', self)
            self.update_longtext.triggered.connect(self.delete_empty_lines_in_longtext)
            self.update_longtext.setCheckable(True)
            #merge
            self.merge_longtext = QAction('merge Longtext', self)
            #self.merge_longtext.triggered.connect(dummy_prog)
            self.merge_longtext.setCheckable(True)
            #edit
            self.longtext_editor = QAction('Longtext editor', self)
            #self.merge_longtext.triggered.connect(dummy_prog)
            self.longtext_editor.setCheckable(True)

            self.tool_menu = self.menu.addMenu('&Tools')
            self.tool_menu.addAction(self.clen_longtext)
            self.tool_menu.addAction(self.update_longtext)
            self.tool_menu.addAction(self.merge_longtext)
            self.tool_menu.addAction(self.longtext_editor)
            self.tool_menu.addSeparator()
        #-------------------- 

        #-------------------- 
        def get_file_names(self):
            """get file names for import in the prozess
            """
            #--------------------
            self.import_data_button.setChecked(False)
            #--------------------
            file_filter = 'Dat File (*.dat)'
            #file_filter = 'Dat File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls);; Image File (*.png *.jpg)'
            response = QFileDialog.getOpenFileNames(
                parent = self,
                caption = 'Select file(s)',
                directory = getcwd(),
                filter = file_filter,
            )
            debug_print(response[0])
            debug_print(len(response[0]))
            #if not len(response[0] == 0):
            for index in range(len(response[0])):
                self.list_of_file_viso.addItem(QListWidgetItem(response[0][index]))
                self.list_of_files.append(response[0][index])
            #--------------------
        def clean_longtext(self):
            """get file names for import in the prozess
            """
            longtext = LongtextTools()
            #--------------------
            self.clen_longtext.setChecked(False)
            #--------------------
            file_filter = 'Longtext (*.xlsx *.csv);; Longtext (*.txt)'
            response = QFileDialog.getOpenFileName(
                parent=self,
                caption='Select a file',
                directory=getcwd(),
                filter=file_filter,
            )
            debug_print(str(response[0]))
            if longtext.clen_up(response[0]) and (not len(response[0]) == 0):

                response = QFileDialog.getSaveFileName(
                    parent=self,
                    caption='Select a data file',
                    directory= 'Roboter1.en.csv',
                    filter=response[1],
                    #initialFilter='Excel File (*.xlsx *.xls)'
                    )
                debug_print(str(response))
                longtext.save_file(response[0])
            else:
                debug_print('abort')
        def delete_empty_lines_in_longtext(self):
            """get file names for import in the prozess
            """
            longtext = LongtextTools()
            #--------------------
            self.update_longtext.setChecked(False)
            #--------------------
            file_filter = 'Longtext (*.xlsx *.csv);; Longtext (*.txt)'
            response = QFileDialog.getOpenFileName(
                parent=self,
                caption='Select a file',
                directory=getcwd(),
                filter=file_filter,
                )
            debug_print(str(response[0]))

            if longtext.delete_empty_lines(response[0]) and (not len(response[0]) == 0):

                response = QFileDialog.getSaveFileName(
                    parent=self,
                    caption='Select a data file',
                    directory= 'Roboter1.en.csv',
                    filter=response[1],
                    initialFilter='Longtext (*.xlsx *.csv); Longtext (*.txt)'
                    )
                debug_print(str(response))
                longtext.save_file(response[0])
            else:
                debug_print('abort')
            #--------------------
        def merge_longtext(self):
                pass
            #--------------------
        def longtext_editor(self):
                pass
            #--------------------
        #-------------------- 












class DragDropListWidget(QListWidget):
    """A custom QListWidget that accepts drag-and-drop for file paths."""

    def __init__(self, parent=None):
        """Initializes the DragDropListWidget."""
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        """Accepts the event if it contains URLs.

        Args:
            event: The drag enter event.
        """
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dropEvent(self, event):
        """Handles the drop event and adds file paths to the list.

        Args:
            event: The drop event.
        """
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                self.addItem(file_path)
            event.acceptProposedAction()
        else:
            super().dropEvent(event)