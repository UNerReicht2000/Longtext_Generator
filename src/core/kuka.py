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
from os import path
from enum import Enum
from dataclasses import dataclass
from typing import Tuple
from .longtext_func import extract_number
from .longtext_func import validated_file_name

class IoType(Enum):
    INPUT = '$IN'
    OUTPUT = '$OUT'
    NOT_DEFINED = 'NOT_DEFINED'

@dataclass
class Marking:
    aktiv: bool#if the marking is active
    name: str  #name of the marking for ui
    io_type: IoType = None  #INPUT, OUTPUT
    length: int = 0 
    var_syktax: Tuple[str, ...] = () #var $IN[x],var $IN[x] TO $IN[x],var $ANIN[x]
    var_prefix: Tuple[str, ...] = () #var di, DO #not use

    def __str__(self):
        return f'Marking(ui={self.name}, type={self.io_type}, length={self.length}, var_syktax={self.var_syktax}, var_präfix={self.var_prefix})'

class Longtext:
    def __init__(self):
        self.base_data = {}
        self.longtext = {}
        self.var_markings = [
            Marking(aktiv = True,name = 'Digital Input',io_type = IoType.INPUT,length = 2,var_syktax = ('$in[','$In[','$IN['),var_prefix = ()),
            Marking(aktiv = True,name = 'Digital Output',io_type = IoType.OUTPUT,length = 2,var_syktax = ('$out[','$Out[','$OUT['),var_prefix = ()),
            Marking(aktiv = True,name = 'Analog Input',io_type = IoType.INPUT,length = 2,var_syktax = ('$anin[','$AnIn[','$ANIN['),var_prefix = ()),
            Marking(aktiv = True,name = 'Analog Output',io_type = IoType.OUTPUT,length = 2,var_syktax = ('$anout[','$AnOut[','$ANOUT['),var_prefix = ()),
            Marking(aktiv = True,name = 'Grouped Input',io_type = IoType.INPUT,length = 3, var_syktax = ('$in[','$In[','$IN['),var_prefix = ()),
            Marking(aktiv = True,name = 'Grouped Output',io_type = IoType.OUTPUT,length = 3, var_syktax = ('$out[','$Out[','$OUT['),var_prefix = ())
                             ]
        self.log_name = ''
        self.log = []

    def __call__(self):
        return self.longtext
    
    def set_selection(self,selection: dict):
        """Sets the markings based on a dictionary where the key is compared with the name.

        Args:
            selection (dict): dict 
            
        Raises:
            TypeError: selection must be a dictionary
            TypeError: all keys in selection must be strings
            TypeError: all values in selection must be booleans
        """
        
        if not isinstance(selection, dict):
            raise TypeError('selection must be a dictionary')
        if not all(isinstance(key, str) for key in selection.keys()):
            raise TypeError('all keys in selection must be strings')
        if not all(isinstance(value, bool) for value in selection.values()):
            raise TypeError('all values in selection must be booleans')
        def set_aktiv(marking):
            if marking.name in selection:
                marking.aktiv = selection[marking.name]
            return marking
        self.var_markings = list(map(set_aktiv,self.var_markings))
    
    def set_prefixes(self,prefixes):
        """Sets the prefixes based on a dictionary where the key is compared with the name.

        Args:
            prefixes (dict): dict 
            
        Raises:
            TypeError: prefixes must be a dictionary
            TypeError: all keys in prefixes must be strings
            TypeError: all values in prefixes must be tuples
            TypeError: all items in the tuples must be strings
        """
        
        if not isinstance(prefixes, dict):
            raise TypeError('prefixes must be a dictionary')
        if not all(isinstance(key, str) for key in prefixes.keys()):
            raise TypeError('all keys in prefixes must be strings')
        if not all(isinstance(value, tuple) for value in prefixes.values()):
            raise TypeError('all values in prefixes must be tuples')
        if not all(isinstance(item, str) for value in prefixes.values() for item in value):
            raise TypeError('all items in the tuples must be strings')
        def set_prefixes(marking):
            if marking.name in prefixes:
                marking.var_prefix = prefixes[marking.name]
            return marking
        self.var_markings = list(map(set_prefixes,self.var_markings))
    
    def create_template(self,expanded: bool = False):
        if type(expanded) != bool:
            raise TypeError('expanded must be a boolean')
        
        self.longtext = {}
        if not expanded:
            longtext_items = {'$TIMER[': 60,'$COUNT_I[': 60,'$FLAG[': 999,'$CYC_FLAG[': 256,'$ANIN[': 32,'$ANOUT[': 32,'$IN[': 4096,'$OUT[': 4096}
        else:  
            longtext_items = {'$TIMER[': 60,'$COUNT_I[': 60,'$FLAG[': 999,'$CYC_FLAG[': 256,'$ANIN[': 32,'$ANOUT[': 32,'$IN[': 8192,'$OUT[': 8192}

        for key in longtext_items:
            for index in range(1,longtext_items[key]+1):
                self.longtext[key+str(index)+']'] = []

    def set_lt_settings(self,markings: list):
        """imports a the markings for the ui

        Args:
            markings (list[Marking]): list of markings to import
        """
        
        def set_marking_settings(marking):
            if self.var_markings[index].name == marking.name:
                self.var_markings[index].aktiv = marking.aktiv
                self.var_markings[index].var_prefix = marking.var_prefix
        if not isinstance(markings, list):
            raise TypeError('markings must be a list of Marking')
        
        for marking in markings:
            if not isinstance(marking, Marking):
                raise TypeError(f'{marking} is not a Marking')
            if not marking.var_prefix:
                continue
            for prefix in marking.var_prefix:
                if not prefix.isascii():
                    raise ValueError(f'a non-ascii character was found. ({prefix})')       
                elif prefix.isspace():
                    raise ValueError(f'the prefix consists only of spaces.') 
                
        if len(markings) != len(self.var_markings):
            raise ValueError(f'Error: {len(markings)} markings were given, but {len(self.var_markings)} markings are expected')
            
        for marking in markings:
            for index in range(len(self.var_markings)):
                if self.var_markings[index].name == marking.name:
                    self.var_markings[index].aktiv = marking.aktiv
                    self.var_markings[index].var_prefix = marking.var_prefix

    def read_dat(self,files: list):
        """turns a list of files in to the base data

        Args:
            files (list): list of files directory
        """

        result = {}
        if type(files) == list:
            for index in range(len(files)):
                if path.exists(files[index]):    
                    importdat = open(files[index],'r')
                    data = importdat.read()
                    importdat.close()
                    result[files[index]] = data.split("\n")
                else:
                    self.log += [f'File {files[index]} not found']
                    raise FileNotFoundError(f'File {files[index]} not found')
            self.base_data = result
        else:
            raise TypeError('files must be a list')

    def read_txt(self,file: str):
        """turns a file in to the base data

        Args:
            file (str): file directory
        """
        result = {}
        if type(file) == str:
            if path.exists(file):    
                importdat = open(file,'r')
                data = importdat.read()
                importdat.close()
                result[file] = data.split("\n")
            else:
                self.log += [f'File {file} not found']
                raise FileNotFoundError(f'File {file} not found')    
            self.base_data = result 
        else:
            raise TypeError('files must be a string')

    def read_csv(self,file: str):
        """turns a file in to the base data

        Args:
            file (str): file directory
        """
        result = {}
        if type(file) == str:
            if path.exists(file):    
                importdat = open(file,'r')
                data = importdat.read()
                importdat.close()
                result[file] = data.split("\n")
            else:
                self.log += [f'File {file} not found']
                raise FileNotFoundError(f'File {file} not found')    
            self.longtext = result 
        else:
            raise TypeError('files must be a string')

    def scan_data(self,with_comments: bool = False):
        """scans the base data for the variables and creates a dictionary with the variables as keys and the declarations as values
        """
        for file in self.base_data:
            for line in range(len(self.base_data[file])):
                if with_comments:
                    self.base_data[file][line] = self.base_data[file][line].lstrip().lstrip(';')
                self.base_data[file][line] = self.base_data[file][line].split(';')[0]
                for item in ['Decl','Global','Const','Int','Signal','Bool','Defdat','Public','Enddat']:
                    self.base_data[file][line] = self.base_data[file][line].replace(item,'').replace(item.upper(),'').replace(item.lower(),'')
                for item in ['To','=']:
                    self.base_data[file][line] = self.base_data[file][line].replace(item,' ').replace(item.upper(),' ').replace(item.lower(),' ')
                self.base_data[file][line] = self.base_data[file][line].strip()

            self.base_data[file] = [x for x in self.base_data[file] if x != '']

            for line in range(len(self.base_data[file])):
                self.base_data[file][line] = self.base_data[file][line].split(' ')
                self.base_data[file][line] = [x for x in self.base_data[file][line] if x != '']
            
            for line in self.base_data[file]:
                for marking in self.var_markings:
                    if not marking.aktiv:
                        continue

                    elif len(line) == 0:
                        continue

                    #single io
                    elif len(line) == 2 == marking.length and line[1].startswith(marking.var_syktax) and (not marking.var_prefix or line[0].startswith(marking.var_prefix)):
                        if line[1] not in self.longtext:
                            self.longtext[line[1].upper()] = []
                        self.longtext[line[1].upper()] += [line[0]]

                    #grouped io
                    elif len(line) == 3 == marking.length and (line[1].startswith(marking.var_syktax) and line[2].startswith(marking.var_syktax)) and (not marking.var_prefix or line[0].startswith(marking.var_prefix)):
                        start_point = extract_number(line[1])
                        end_point = extract_number(line[2])
                        var_type = marking.io_type.value
                        sub_index = 0
                        
                        for index in range(start_point,end_point + 1):
                            if var_type+'['+str(index)+']' not in self.longtext:
                                self.longtext[var_type+'['+str(index)+']'] = []
                            self.longtext[var_type+'['+str(index)+']'] += [line[0] + ' 2**' + str(sub_index)]
                            sub_index += 1

        markings = '$ANIN[','$ANOUT[','$IN[','$OUT['
        keys_to_remove = [key for key in self.longtext if not key.startswith(markings)]
        for key in keys_to_remove:
            del self.longtext[key]
            
    def merge(self, other):
        if isinstance(other,Longtext):
            raise TypeError('only Longtext can be added')
        for key, value in other.longtext.items():
            if key in self.longtext:
                self.longtext[key].extend(value)
            else:
                self.longtext[key] = value
        return self.longtext

    def delete_präfix(self):
        """deletes the prefix (diTest -> Test)
        """
        for marking in self.var_markings:
            for key in self.longtext:
                if self.longtext[key]:
                    for index in len(range(self.longtext[key])):
                        self.longtext[key][index] = self.longtext[key][index].lstrip(marking.var_prefix)
            
    def delete_empty_lines(self):
        keys_to_remove = [key for key in self.longtext if self.longtext[key] == []]
        for key in keys_to_remove:
            del self.longtext[key]

    def check_for_errors(self):
        pass

    def check_for_double_declarations(self):
        self.log += ['Double declarations:']
        count = 0
        for key in self.longtext:
            if len(self.longtext[key]) > 1:
                count += 1
                error = f'{key} has multiple declarations({self.longtext[key]})'
                print(error)
                self.log += [error]
        self.log += [f'{count} Double declarations were found']

    def export_csv(self,file_name: str,directory: str):
        if type(directory) == str:   
            final_file_name = validated_file_name(file_name)
            error_count = 0

            while (path.isfile(path.join(directory, final_file_name))):
                if path.isfile(path.join(directory, final_file_name)):
                    basename, extension = path.splitext(final_file_name)
                    final_file_name = f"{basename}_copy{extension}"

                error_count += 1
            final_file_name = final_file_name
            self.log_name = final_file_name

            with open(path.join(directory, final_file_name), "w") as file:
                for key,value in self.longtext.items():
                    file.write(f'{key};{';'.join(value)}'.rstrip(';') + '\n')
            file.close()
        else:
            raise TypeError('directory must be a string')

    def export_txt(self,file_name: str,directory: str):
        if type(directory) == str:   
            final_file_name = validated_file_name(file_name)
            error_count = 0
            while (path.isfile(path.join(directory, final_file_name))):
                if path.isfile(path.join(directory, final_file_name)):
                    basename, extension = path.splitext(final_file_name)
                    final_file_name = f"{basename}_copy{extension}"

                error_count += 1
            final_file_name = final_file_name
            self.log_name = final_file_name

            with open(path.join(directory, final_file_name), "w") as file:
                for key,value in self.longtext.items():
                    file.write(f'{key} {' '.join(value)}'.rstrip() + '\n')
            file.close()
        else:
            raise TypeError('directory must be a string')

    def export_log(self,file_name: str,directory: str):
        line = ''
        for line in self.log:
            print(line)
        return
        if type(directory) == str:   
            final_file_name = validated_file_name(file_name)
            error_count = 0
            while (path.isfile(path.join(directory, final_file_name + '.txt'))):
                if path.isfile(path.join(directory, final_file_name + '.txt')):
                    basename, extension = path.splitext(final_file_name)
                    final_file_name = f"{basename}_copy{extension}"

                error_count += 1
            final_file_name = final_file_name+'.txt'

            with open(path.join(directory, final_file_name), "w") as file:
                file.write(self.log_name + '\n')
                for line in self.log:
                    file.write(line + '\n')
            file.close()
        else:
            raise TypeError('directory must be a string')