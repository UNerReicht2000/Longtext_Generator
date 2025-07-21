# -*- coding: utf-8 -*-

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

from PyQt6.QtCore import QSettings
from PyQt6.QtCore import QStandardPaths

from core.kuka import Marking
from core.kuka import Longtext

#from user_ui.ui_func import DragDropListWidget

'''read my
    sort cuts
        LtG = Longtextgenerator
'''

class MainWindowLtG(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        
        self.list_of_files = []
        self.list_of_drops = []

        self.settings = QSettings('DU Software','Langtext Generator')
        self.default_directory = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation)

        self.list_of_lontext_config = []
        self.setGeometry(300,300,773,403)
        self.setMinimumSize(773,403)
        self.setFixedSize(773,403)
        self.setWindowTitle('Langtext Generator')      
        
        x_pos = 590
        y_pos = 370

        self.start_butten = QPushButton('Start',self)
        self.start_butten.setGeometry(x_pos,y_pos,86,24)
        self.start_butten.setCheckable(True)
        self.start_butten.clicked.connect(self.start_prozess)

        self.menu_bar_ui()       
        self.file_import_ui(10,30)
        self.general_options_ui(225,30)
        self.longtext_settings_ui(585,30)
        self.setAcceptDrops(True)
    #-------------------- 
    def menu_bar_ui(self):
        """menubar ui
        """

        self.menu = self.menuBar()

        self.import_data_button = QAction('Import Dat', self)
        self.import_data_button.triggered.connect(self.get_file_names)
        self.import_data_button.setCheckable(True)

        self.file_menu = self.menu.addMenu('&File')
        self.file_menu.addAction(self.import_data_button)
        self.file_menu.addSeparator()

        self.tb_clen_longtext = QAction('Clean Longtext', self)
        self.tb_clen_longtext.triggered.connect(self.clean_longtext)
        self.tb_clen_longtext.setCheckable(True)

        self.tb_update_longtext = QAction('Delete Empty Lines', self)
        self.tb_update_longtext.triggered.connect(self.delete_empty_lines_in_longtext)
        self.tb_update_longtext.setCheckable(True)
        #merge
        self.tb_merge_longtext = QAction('merge Longtext', self)
        #self.merge_longtext.triggered.connect(dummy_prog)
        self.tb_merge_longtext.setCheckable(True)
        #edit
        self.tb_longtext_editor = QAction('Longtext Editor', self)
        #self.merge_longtext.triggered.connect(dummy_prog)
        self.tb_longtext_editor.setCheckable(True)

        self.tb_check_longtext = QAction('Check Longtext', self)
        self.tb_check_longtext.triggered.connect(self.check_longtext)
        self.tb_check_longtext.setCheckable(True)

        self.tool_menu = self.menu.addMenu('&Tools')
        self.tool_menu.addAction(self.tb_clen_longtext)
        self.tool_menu.addAction(self.tb_update_longtext)
        self.tool_menu.addAction(self.tb_merge_longtext)
        self.tool_menu.addAction(self.tb_longtext_editor)
        self.tool_menu.addSeparator()
        self.tool_menu.addAction(self.tb_check_longtext)
        self.tool_menu.addSeparator()

        self.tool_menu = self.menu.addMenu('&Settings')
        
        self.tb_setup_markings = QAction('setup Prefixes', self)
        self.tb_setup_markings.triggered.connect(self.setup_prefix)
        self.tb_setup_markings.setCheckable(True)

        self.tool_menu.addAction(self.tb_setup_markings)
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
            directory = self.default_directory,
            filter = file_filter,
        )
        print(response[0])
        print(len(response[0]))
        #if not len(response[0] == 0):
        for index in range(len(response[0])):
            self.list_of_file_viso.addItem(QListWidgetItem(response[0][index]))
            self.list_of_files.append(response[0][index])
        #--------------------
    def clean_longtext(self):
        """get file names for import in the prozess
        """
        #longtext = LongtextTools()
        #--------------------
        self.tb_clen_longtext.setChecked(False)
        #--------------------
        file_filter = 'Longtext (*.csv);; Longtext (*.txt)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=getcwd(),
            filter=file_filter,
        )
        print(str(response[0]))

    def delete_empty_lines_in_longtext(self):
        """get file names for import in the prozess
        """
        print('Delete Empty Lines')
        #--------------------
    def merge_longtext(self):
        print('Merge Longtext')
        #--------------------
    def longtext_editor(self):
        print('Longtext Editor')
        #--------------------
    def check_longtext(self):
        print('Check Longtext')

    def setup_prefix(self):
        print('Setup Prefix')
        #
    #-------------------- 

    #--------------------
    def file_import_ui(self,x_pos: int,y_pos: int):
        
        boxlayout = QVBoxLayout()
        
        #file_urls = []
        # QGroupBox erstellen
        #event.acceptProposedAction()
        self.dat_import_box = QGroupBox('Imported Files',self)
        self.dat_import_box.setGeometry(x_pos,y_pos,205,330)
        self.dat_import_box.setLayout(boxlayout)   
        self.dat_import_box.setAcceptDrops(True) 
        
        #Delete Item PushButten
        self.del_item_butten = QPushButton('Delete',self)
        self.del_item_butten.setGeometry(x_pos+10,y_pos+295,90,24)
        self.del_item_butten.setCheckable(True)
        self.del_item_butten.setEnabled(True)
        self.del_item_butten.clicked.connect(self.delete_item)
        
        #Delete List PushButten
        self.clean_list_butten = QPushButton('Delete all',self)
        self.clean_list_butten.setGeometry(x_pos+105,y_pos+295,90,24)
        self.clean_list_butten.setCheckable(True)
        self.clean_list_butten.setEnabled(True)
        self.clean_list_butten.clicked.connect(self.clear_list)

        self.list_of_file_viso = QListWidget(self)
        self.list_of_file_viso.acceptDrops()
        self.list_of_file_viso.setAcceptDrops(True)
        self.list_of_file_viso.setGeometry(x_pos+10,y_pos+20,185,265)
        self.list_of_file_viso.itemClicked.connect(self.clicked_list_event)
        #
    def dragEnterEvent(self,event):
        print('Dragevent')
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)
        #--------------------    
    def dropEvent(self,event):
        file_urls = [url.toLocalFile() for url in event.mimeData().urls()]
        for file_url in file_urls:
            if file_url not in self.list_of_drops:
                self.list_of_drops.append(file_url)
        self.list_of_file_viso.clear()
        self.list_of_files.clear()
        for file_url in self.list_of_drops:
            self.list_of_file_viso.addItem(QListWidgetItem(file_url))
            self.list_of_files.append(file_url)
        print(self.list_of_drops)
        #
    def clicked_list_event(self):
        print(self.list_of_file_viso.currentRow())
        SelectedItem = self.list_of_file_viso.item(self.list_of_file_viso.currentRow()).text()
        print(SelectedItem)
        print('Click')           
    def delete_item(self):
        print('DeleteItemButten = True')
        self.del_item_butten.setChecked(False)
        if len(self.list_of_file_viso) > 0:
            try:
                self.list_of_file_viso.takeItem(self.list_of_file_viso.currentRow())
                self.list_of_files.pop(self.list_of_file_viso.currentRow())
            except:
                pass
        print(self.list_of_files)
        #du.printList(self.WindowListOfFiles)
    def clear_list(self):
        print('DeleteListButten = True')
        self.clean_list_butten.setChecked(False)
        self.list_of_file_viso.clear()  
        self.list_of_files.clear() 
    #--------------------

    #--------------------
    def general_options_ui(self,x_pos: int,y_pos: int):

        self.other_options_box = QGroupBox('General settings',self)
        self.other_options_box.setGeometry(x_pos,y_pos,351,330)         

        self.delete_var_macker = QCheckBox('Delete Signal Prefix (di,do,gi...)',self)
        self.delete_var_macker.setGeometry(x_pos+10,y_pos+20,301,21)
        self.delete_var_macker.setCheckable(True)

        self.delete_all_empty_lines = QCheckBox('Create update Longtext (delete all empty lines)',self)
        self.delete_all_empty_lines.setGeometry(x_pos+10,y_pos+40,301,21)
        self.delete_all_empty_lines.setCheckable(True)

        self.expanded_interfase = QCheckBox('expanded Interfase (8192 Input,8192 Output)',self)
        self.expanded_interfase.setGeometry(x_pos+10,y_pos+60,301,21)
        self.expanded_interfase.setCheckable(True)

        self.export_log = QCheckBox('Export Log Dat',self)
        self.export_log.setGeometry(x_pos+10,y_pos+80,301,21)
        self.export_log.setCheckable(True)

    def longtext_settings_ui(self,x_pos,y_pos):
        self.lt_config_box = QGroupBox('Longtext settings',self)
        self.lt_config_box.setGeometry(x_pos,y_pos,181,330) 
        #Select All PushButten
        self.select_all_butten = QPushButton('All',self)
        self.select_all_butten.setGeometry(x_pos,325,75,24)
        self.select_all_butten.setCheckable(True)
        self.select_all_butten.setEnabled(True)
        self.select_all_butten.clicked.connect(self.select_all)

        #Rest All PushButten
        self.reset_all_butten = QPushButton('Reset',self)
        self.reset_all_butten.setGeometry(x_pos+80,325,75,24)
        self.reset_all_butten.setCheckable(True)
        self.reset_all_butten.setEnabled(True)
        self.reset_all_butten.clicked.connect(self.reset_all)
    def select_all(self):
        print('Select All Butten = True')
        return
        self.select_all_butten.setChecked(False)
        for key in  self.longtext_check_box:
            self.longtext_check_box[key].setChecked(True)
        self.set_longtext_config()
        #
    def reset_all(self):
        print('ResetAllButten = True')
        return
        self.reset_all_butten.setChecked(False)
        for key in  self.longtext_check_box:
            self.longtext_check_box[key].setChecked(False)  
        self.set_longtext_config()
        #    
    def start_prozess(self):
        self.start_butten.setChecked(False)
        file_filter = 'Longtext (*.csv *.txt)'
        response = QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a data file',
            directory= self.default_directory,
            filter=file_filter,
            initialFilter='Longtext (*.csv *.txt)'
            )
        directory = response[0].replace(response[0].split('/')[-1],'')
        file_name = response[0].split('/')[-1]

        print(directory)
        if len(directory) > 0:
            longtext = Longtext()
            raw_longtext = Longtext()
            longtext.create_template(self.expanded_interfase.isChecked())
            raw_longtext.read_dat(self.list_of_files)
            raw_longtext.scan_data()
            longtext.merge(raw_longtext)
            if self.delete_all_empty_lines.isChecked():
                longtext.delete_empty_lines()
            if self.delete_var_macker.isChecked():
                pass
            if self.export_log.isChecked():
                longtext.check_for_double_declarations()
                longtext.export_log(file_name,directory)
            if (file_name[-4:] == '.Csv') or (file_name[-4:] == '.csv'.upper()) or (file_name[-4:] == '.csv'):
                longtext.export_csv(file_name,directory)
            elif (file_name[-4:] == '.Txt') or (file_name[-4:] == '.txt'.upper()) or (file_name[-4:] == '.txt'):
                longtext.export_txt(file_name,directory)
            else:
                print('Error wrong file format')
        else:
            print('abort')

    #-------------------- 

app = QApplication([])
window = MainWindowLtG()
window.show()
app.exec()