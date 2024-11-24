# -*- coding: utf-8 -*-

from dev_func import debug_print
from dev_func import print_list
from dev_func import print_dict
from dev_func import Cycle_Time

from json import loads
from json import dumps

from os import path

from core.longtext_func import Buffer
from core.longtext_func import lode_user_files
from core.longtext_func import delete_all_empty_lines
from core.longtext_func import validated_datname
from core.longtext_func import validated_datpath
from core.longtext_func import create_file_with_list
from core.longtext_func import clean_up_longtext

from core.kuka.kuka_standard import create_longtext as kuka_create_longtext
from core.kuka.kio_standard import create_longtext as kio_create_longtext

class Process():
    def __init__(self) -> None:
        pass
        #--------------------
    def start(self) -> None:
        """start the Process
        """

        current_directory = path.dirname(path.abspath(__file__))
        file_path = path.join(current_directory, 'workdata.json')
        dat = open(file_path, 'r')
        workdata = loads(dat.read())
        dat.close()

        self.longtextname = validated_datname(workdata['longtextname'])
        self.list_of_files = workdata['list_of_files']
        self.list_of_longtext_config = workdata['list_of_longtext_config']
        self.delete_var_macker = workdata['delete_var_macker']
        self.data_typ = workdata['data_typ']
        self.decl_typ = workdata['decl_typ']
        self.delete_empty_lines = workdata['delete_empty_lines']

        self.ErrorBuffer = Buffer()

        if self.decl_typ == 0:
            cycle_time_kuka = Cycle_Time('cycle time KUKA')
            cycle_time_kuka.start()
            self.longtext = kuka_create_longtext(lode_user_files(self.list_of_files),
                                            self.list_of_longtext_config,
                                            self.delete_var_macker,
                                            self.data_typ,
                                            self.ErrorBuffer,
                                            )
            cycle_time_kuka.stop()
            self.ErrorBuffer.append(f'calculate time: {cycle_time_kuka.read()}s')

        elif self.decl_typ == 1:
            cycle_time_kio = Cycle_Time('cycle time KUKA')
            cycle_time_kio.start()
            self.longtext = kio_create_longtext(lode_user_files(self.list_of_files),
                                                self.list_of_longtext_config,
                                                self.delete_var_macker,
                                                self.data_typ,
                                                self.ErrorBuffer,
                                                )
            cycle_time_kio.stop()
            self.ErrorBuffer.append(f'calculate time: {cycle_time_kio.read()}s')

        else:
            self.ErrorBuffer.append('critical error')

        if self.delete_empty_lines:
            self.longtext = delete_all_empty_lines(self.longtext)
        #--------------------
    def save_longtext(self) -> None:

        current_directory = path.dirname(path.abspath(__file__))
        file_path = path.join(current_directory, 'workdata.json')
        dat = open(file_path, 'r') 
        workdata = loads(dat.read())

        self.file_part = workdata['file_part']
        if validated_datpath(self.file_part):
            self.ErrorBuffer.append('filepart is not okay')

        final_name = create_file_with_list(
            self.longtextname,
            self.file_part,
            self.longtext,
            self.data_typ,
            )
        
        self.ErrorBuffer.export_dat('Error_List_'+self.longtextname,workdata['file_part'])
        self.ErrorBuffer.clear()  
        #--------------------

class Workdat():
    def __init__(self) -> None:
        """checks the json file for errors and fixes them
        """
        self.data_structure = {
            "longtextname": '',
            "file_part": '',
            "list_of_files": [''],
            "list_of_longtext_config": [0],
            "delete_var_macker": False,
            "data_typ": 999,
            "decl_typ": 999,
            "delete_empty_lines": False,
        }

        current_directory = path.dirname(path.abspath(__file__))
        file_path = path.join(current_directory, 'workdata.json')
        dat = open(file_path, 'r+')
        data = dat.read()
        if len(data) > 0:
            data = loads(data)  
            if not data.keys() == self.data_structure.keys():    
                dat.write(dumps(self.data_structure))
                print('Warnung:1000')
        else:
            dat.write(dumps(self.data_structure))
            print('Warnung:1000')    
        
        dat.close()       
        #--------------------
    def read(self) -> dict:
        """read data from a json file

        Returns:
            dict: returns a dict with all config infos 
        """
        current_directory = path.dirname(path.abspath(__file__))
        file_path = path.join(current_directory, 'workdata.json')
        dat = open(file_path, 'r')
        workdata = loads(dat.read())
        dat.close()

        return workdata
        #--------------------
    def write(self,in_dict: dict):
        """write data in to a json file

        Args:
            in_dict (dict): a dict with the config infos 
        """
        json_string = dumps(in_dict)

        current_directory = path.dirname(path.abspath(__file__))
        file_path = path.join(current_directory, 'workdata.json')
        dat = open(file_path, 'w')   
        dat.write(json_string)
        dat.close()
        #--------------------
    def clear(self) -> None:
        """clear the workdata.json
        """
        json_string = dumps(self.data_structure)

        current_directory = path.dirname(path.abspath(__file__))
        file_path = path.join(current_directory, 'workdata.json')
        dat = open(file_path, 'w')   
        dat.write(json_string)
        dat.close()
        #--------------------

class LongtextTools():
    def __init__(self) -> None:
        pass
        #--------------------
    def clen_up(self,file_path: str) -> bool:

        self.longtext = []
        debug_print(validated_datpath(file_path))
        if validated_datpath(file_path):
            self.longtext = lode_user_files([file_path])
            self.longtext = clean_up_longtext(self.longtext,0)
            # print_list(self.longtext)
            return True
        else:
            False
        debug_print('end')
        self.longtext.clear()
        #--------------------
    def delete_empty_lines(self,file_path: str) -> bool:
        """_summary_

        Args:
            file_path (str): file path

        Returns:
            bool: result
        """
        self.longtext = []
        debug_print(validated_datpath(file_path))
        if validated_datpath(file_path):
            self.longtext = lode_user_files([file_path])
            self.longtext = delete_all_empty_lines(self.longtext)

            result = True
        else:
            result = False

        self.longtext.clear()
        debug_print(f'delete_empty_lines result = {result}')
        return result
        #--------------------
    def save_file(self,file_path: str):
        """save the new longtext

        Args:
            file_path (str): file path
        """
        with open(file_path, "w") as dat:
            for index in range(len(self.longtext)): 
                dat.write(self.longtext[index]+'\n')
        dat.close()
        #--------------------