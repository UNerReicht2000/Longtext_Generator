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

from user_ui.popup_ui import StartAndSavePopUp

#from user_ui.ui_func import DragDropListWidget


'''read my
    sort cuts
        LtG = Longtextgenerator
'''

class MainWindowLtG(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        
        #self.workdat = Workdat()

        self.list_of_files = []
        self.list_of_drops = []

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
        #self.declaration_system_ui(225,30)
        #self.longtext_name_ui(225,100)
        self.longtext_config_ui(585,30)       
        self.file_import_ui(10,30)
        self.text_options_ui(225,170)
    
    #-------------------- 
    def menu_bar_ui(self):
        """menubar ui
        """
        
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
        self.clen_longtext.setChecked(False)
        #--------------------
        file_filter = 'Longtext (*.xlsx *.csv);; Longtext (*.txt)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=getcwd(),
            filter=file_filter,
        )
        print(str(response[0]))
        if False:
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
        #longtext = LongtextTools()
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

        if False:
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
    
    #--------------------    
    def declaration_system_ui(self,x_pos: int,y_pos: int):
        self.longtext_name_box = QGroupBox('Declarationssystem',self)
        self.longtext_name_box.setGeometry(x_pos,y_pos, 351, 71)

        self.decl_typ = QComboBox(self)
        self.decl_typ.setGeometry(x_pos+130,y_pos+20,110,21)
        self.list_of_options = ['KUKA Standart','KIO Standart']
        self.decl_typ.addItem('KUKA Standart') 
        self.decl_typ.addItem('KIO Standart') 
        self.decl_typ.currentIndexChanged.connect(self.set_decl_typ)

        self.decl_typ_label = QLabel('Declarationssystem:',self)       
        self.decl_typ_label.setGeometry(x_pos+10,y_pos+20,151,21)
        self.decl_typ_info_label = QLabel('z.B. : GLOBAL SIGNAL BOVarName $OUT[2000]',self)       
        self.decl_typ_info_label.setGeometry(x_pos+10,y_pos+40,301,21)   
    def set_decl_typ(self,index: int):
        info_text = {
            0 : 'z.B. : GLOBAL SIGNAL BOVarName $OUT[2000]',
            1 : 'z.B. : GLOBAL CONST INT BOVarName = 2000',    
        }

        self.decl_typ_info_label.setText(info_text[index])   
    #--------------------

    #--------------------
    def longtext_name_ui(self,x_pos: int,y_pos: int):
        self.longtext_name_box = QGroupBox('Langtext Name Einstellungen',self)
        self.longtext_name_box.setGeometry(x_pos,y_pos, 351, 71)
        #Longtextname Label
        self.longtext_name_label = QLabel('Langtext Name:',self)       
        self.longtext_name_label.setGeometry(x_pos+10,y_pos+20,91,21)
        self.longtext_info_label = QLabel('Nicht erlaubte Zeichen: / * |',self)       
        self.longtext_info_label.setGeometry(x_pos+10,y_pos+45,221,21)      
        #Eingabe Feld fur langtext nahme
        self.lontextname_edit = QLineEdit(self)
        self.lontextname_edit.setGeometry(x_pos+95,y_pos+20,221,21)
        self.lontextname_edit.setMaxLength(39)   
        self.lontextname_edit.setClearButtonEnabled(True)   
        self.lontextname_edit.setPlaceholderText('Roboter1.de')   
    #--------------------

    #--------------------    
    def longtext_config_ui(self,x_pos: int,y_pos: int):
            self.list_of_lontext_config = []

            self.longtext_confic_box = QGroupBox('Longtext Confi',self)
            self.longtext_confic_box.setGeometry(x_pos, y_pos,175,330)
            self.longtext_check_box = {}
            self.name_of_check_box = {
                0:'without filters',
                #10:'Timer',
                #20:'Counter',
                #30:'Flag s',
                #40:'CYCFlag s',
                #50:'Analogue Inputs',
                #-50:'Analogue Outputs',
                100:'Digital Inputs',
                -100:'Digital Outputs',
                200:'Grouped Inputs',
                -200:'Grouped Outputs',
                #300:'Integer Inputs',
                #-300:'Integer Outputs',
                #400:'Real Inputs',
                #-400:'Real Outputs',
                #500:'Char Inputs',
                #-500:'Char Outputs',
                }   

            x_pos += 10
            for key in self.name_of_check_box:
                self.longtext_check_box.update({key:QCheckBox(self.name_of_check_box[key],self)})
                y_pos += 20
                self.longtext_check_box[key].setGeometry(x_pos,y_pos,150,21)
                self.longtext_check_box[key].setCheckable(True)
                self.longtext_check_box[key].setEnabled(True)
                self.longtext_check_box[key].clicked.connect(self.set_longtext_config)
             
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
        debug_print('Select All Butten = True')
        self.select_all_butten.setChecked(False)
        for key in  self.longtext_check_box:
            if key != 0:
                self.longtext_check_box[key].setChecked(True)
        self.set_longtext_config()
        #
    def reset_all(self):
        debug_print('ResetAllButten = True')
        self.reset_all_butten.setChecked(False)
        for key in  self.longtext_check_box:
            self.longtext_check_box[key].setChecked(False)  
        self.set_longtext_config()
        #            
    def set_longtext_config(self):
        for key in  self.longtext_check_box:
            if self.longtext_check_box[key].isChecked():
                if not key in self.list_of_lontext_config:
                    self.list_of_lontext_config += [key]
            else:
                if key in self.list_of_lontext_config:
                    self.list_of_lontext_config.remove(key)
        # print_list(self.list_of_lontext_config)
    #--------------------

    #--------------------
    def file_import_ui(self,x_pos: int,y_pos: int):
        
        boxlayout = QVBoxLayout()
        
        #file_urls = []
        # QGroupBox erstellen
        #event.acceptProposedAction()
        self.dat_import_box = QGroupBox('Importirte Dateien',self)
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
        #self.list_of_file_viso.acceptDrops()
        #self.list_of_file_viso.setAcceptDrops(True)
        self.list_of_file_viso.setGeometry(x_pos+10,y_pos+20,185,265)
        self.list_of_file_viso.itemClicked.connect(self.clicked_list_event)
        #
    def drag_enter_event(self,event):
        debug_print('Dragevent')
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().drag_enter_event(event)
        #--------------------    
    def drop_event(self,event):
        debug_print('Dorp Datei Event')

        file_urls = [url.toLocalFile() for url in event.mimeData().urls()]
        print(file_urls)
        for index in range(len(file_urls)):
                if not file_urls in self.list_of_drops:
                    self.list_of_drops.append(file_urls[index])
        self.list_of_file_viso.clear()            
        self.list_of_files.clear()
        for index in range(len(self.list_of_drops)):
            self.list_of_file_viso.addItem(QListWidgetItem(self.list_of_drops[index]))
            self.list_of_files.append(self.list_of_drops[index])

        print_list(self.list_of_drops)
        #
    def clicked_list_event(self):
        debug_print(self.list_of_file_viso.currentRow())
        SelectedItem = self.list_of_file_viso.item(self.list_of_file_viso.currentRow()).text()
        debug_print(SelectedItem)
        debug_print('Click')           
    def delete_item(self):
        debug_print('DeleteItemButten = True')
        self.del_item_butten.setChecked(False)
        if len(self.list_of_file_viso) > 0:
            try:
                self.list_of_file_viso.takeItem(self.list_of_file_viso.currentRow())
                self.list_of_files.pop(self.list_of_file_viso.currentRow())
            except:
                pass
        print_list(self.list_of_files)
        #du.printList(self.WindowListOfFiles)
    def clear_list(self):
        debug_print('DeleteListButten = True')
        self.clean_list_butten.setChecked(False)
        self.list_of_file_viso.clear()  
        self.list_of_files.clear() 
    #--------------------

    #--------------------
    def text_options_ui(self,IPosX: int,IPosY: int):

        self.other_options_box = QGroupBox('General settings',self)
        self.other_options_box.setGeometry(IPosX,IPosY,351,190)

        self.data_typ_label = QLabel('Datatyp:',self)       
        self.data_typ_label.setGeometry(IPosX+10,IPosY+20,60,21)

        self.data_typ = QComboBox(self)
        self.data_typ.setGeometry(IPosX+70,IPosY+20,50,21)
        self.data_typ.addItem('csv')
        self.data_typ.addItem('txt')             

        self.delete_var_macker = QCheckBox('BI,BO,GI... delete',self)
        self.delete_var_macker.setGeometry(IPosX+10,IPosY+45,151,21)
        self.delete_var_macker.setCheckable(True)
        self.delete_var_macker.setEnabled(True)

        self.delete_all_empty_lines = QCheckBox('Create update Longtext ',self)
        self.delete_all_empty_lines.setGeometry(IPosX+10,IPosY+65,201,21)
        self.delete_all_empty_lines.setCheckable(True)
        self.delete_all_empty_lines.setEnabled(True)
        self.delete_all_empty_lines_label = QLabel('(delete all empty lines)',self)
        self.delete_all_empty_lines_label.setGeometry(IPosX+30,IPosY+85,301,21)
    #--------------------  
          
    #-------------------- 
    def go_back(self):
        pass
        # self.BackPushButten.setChecked(False)
        # debug_print('AbortPushButten = True')
        # self.close()  # Schlieen Sie das Fenster
        # #QCoreApplication.quit()  
        # # Beenden Sie die Anwendung
    def start_prozess(self):
        self.start_butten.setChecked(False)
      
        debug_print('StartPushButten = True')        
        self.data = self.workdat.read()
        self.data['longtextname'] = self.lontextname_edit.text()
        self.data['list_of_files'] = self.list_of_files
        self.data['list_of_longtext_config'] = self.list_of_lontext_config
        self.data['delete_var_macker'] = self.delete_var_macker.isChecked()
        self.data['data_typ'] = self.data_typ.currentIndex()
        self.data['decl_typ'] = self.decl_typ.currentIndex()
        self.data['delete_empty_lines'] = self.delete_all_empty_lines.isChecked()
        self.workdat.write(self.data)

        popup.show()   
    #-------------------- 

app = QApplication([])
window = MainWindowLtG()
popup = StartAndSavePopUp('Save Longtext')
window.show()
app.exec()