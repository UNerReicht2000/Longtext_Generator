# -*- coding: utf-8 -*-

from dev_func import debug_print

from os import getcwd

from core.kuka.process import Process
from core.kuka.process import Workdat

from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QGroupBox
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFileDialog


class StartAndSavePopUp(QWidget):
    def __init__(self,titel):
        self.core_process = Process()
        self.workdat = Workdat()
        super().__init__()
        self.titel = titel

        self.resize(500,200)
        self.setFixedSize(500,200)
        self.setWindowTitle(self.titel)

        screen_geometry =  QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()       
        center_point = screen_geometry.center()        
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())
        
        #Start PushButten
        x_pos = 10
        y_pos = 160
        self.start_butten = QPushButton('Start',self)
        self.start_butten.setGeometry(x_pos,y_pos,110,24)
        self.start_butten.setCheckable(False)
        self.start_butten.setEnabled(False)
        self.start_butten.clicked.connect(self.process_start)

        #Abort PushButten
        x_pos = 380
        y_pos = 160
        self.abort_butten = QPushButton('Abbrechen',self)
        self.abort_butten.setGeometry(380,y_pos,110,24)
        self.abort_butten.setCheckable(True)
        self.abort_butten.clicked.connect(self.abort)        

        x_pos = 10
        y_pos = 10
        self.save_filepart_box = QGroupBox('Langtext Speichern unter',self)
        self.save_filepart_box.setGeometry(x_pos,y_pos, 480, 55)
        #Longtextname Label
        self.save_filepart_label = QLabel('Path:',self)       
        self.save_filepart_label.setGeometry(x_pos+10,y_pos+20,30,20)    
        #Eingabe Feld fur langtext nahme
        self.save_filepart_edit = QLineEdit(self)
        self.save_filepart_edit.setGeometry(x_pos+45,y_pos+20,400,20) 
        self.save_filepart_edit.setClearButtonEnabled(True)   
        self.save_filepart_edit.textChanged.connect(self.on_text_changed)

        self.open_explorer_butten = QPushButton('...',self)
        self.open_explorer_butten.setGeometry(x_pos+446,y_pos+20,30,21)
        self.open_explorer_butten.setCheckable(True)
        self.open_explorer_butten.clicked.connect(self.get_directory) 
        #--------------------
    def on_text_changed(self):
        debug_print(len(self.save_filepart_edit.text()))
        if len(self.save_filepart_edit.text()) > 0:
            self.start_butten.setCheckable(True)
            self.start_butten.setEnabled(True) 
        else:
            self.start_butten.setCheckable(False)
            self.start_butten.setEnabled(False)
        #--------------------
    def abort(self):
        self.abort_butten.setDefault(False)
        debug_print('Abort Butten = True')
        self.close()
        #--------------------
    def process_start(self):
        debug_print('Start Butten = True')
        self.start_butten.setChecked(False)
        self.setDisabled(True)
        self.data = self.workdat.read()
        self.data['file_part'] = self.save_filepart_edit.text()
        self.workdat.write(self.data)
        self.core_process.start()
        self.core_process.save_longtext()

        self.workdat.clear()
        self.setDisabled(False)
        self.close()
        #--------------------
    def get_file_names(self):
        '''get file names for import in the prozess
        
        '''
        file_filter = 'Data File (*.dat)'
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select file(s)',
            directory=getcwd(),
            filter=file_filter,
            initial_filter='Data File (*.dat)'
        )
        debug_print(response)
        #--------------------
    def save_file(self):
        '''
        
        '''
        file_filter = 'Data File (*.dat)'
        response = QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a data file',
            directory= 'Data File.dat',
            filter=file_filter,
            initial_filter='Data File (*.dat)'
        )
        debug_print(response)
        #--------------------
    def get_directory(self):
        '''Get the directory to save the file or import more than two items

        '''
        self.open_explorer_butten.setChecked(False)
        response = QFileDialog.getExistingDirectory(
            self,
            #caption='Select a folder'
        )
        debug_print(response)
        if len(response) > 0:
            self.save_filepart_edit.setText(response)
        #--------------------