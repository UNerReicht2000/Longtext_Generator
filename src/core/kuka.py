# -*- coding: utf-8 -*-
from os import path
from dataclasses import dataclass
from .longtext_func import extract_number
from .longtext_func import validated_file_name

@dataclass
class Markings:
    aktiv: bool
    singel: dict
    multi: dict
    #--------------------

class Longtext:
    def __init__(self):
        self.base_data = {}
        self.longtext = {}
        self.var_markings = Markings(aktiv = False,singel = {'in':(''),'out':('')},multi = {'in':(''),'out':('')})
        self.log_name = ''
        self.info_log = []
        #--------------------
    def __call__(self):
        return self.longtext
        #--------------------
    def create_template(self,expanded: bool = False):
        self.longtext = {}
        if not expanded:
            longtext_items = {'$TIMER[': 60,'$COUNT_I[': 60,'$FLAG[': 999,'$CYC_FLAG[': 256,'$ANIN[': 32,'$ANOUT[': 32,'$IN[': 4096,'$OUT[': 4096}
        else:  
            longtext_items = {'$TIMER[': 60,'$COUNT_I[': 60,'$FLAG[': 999,'$CYC_FLAG[': 256,'$ANIN[': 32,'$ANOUT[': 32,'$IN[': 8192,'$OUT[': 8192}

        for key in longtext_items:
            for index in range(1,longtext_items[key]+1):
                self.longtext[key+str(index)+']'] = []
        #--------------------
    def impot_markings(self,markings: Markings):
        self.var_markings = Markings
        for item in markings.singel['in']:
            self.var_markings.singel['in'] = markings.singel['in'] + (item.upper(),item.lower(),item.capitalize())
        for item in markings.singel['out']:
            self.var_markings.singel['out'] = markings.singel['out'] + (item.upper(),item.lower(),item.capitalize())
        for item in markings.multi['in']:
            self.var_markings.multi['in'] = markings.multi['in'] + (item.upper(),item.lower(),item.capitalize())
        for item in markings.multi['out']:
            self.var_markings.multi['out'] = markings.multi['out'] + (item.upper(),item.lower(),item.capitalize())
        self.var_markings.aktiv = True
        #--------------------
    def clear_markings(self):
        self.var_markings = Markings(aktiv = False,singel = {'in':(''),'out':('')},multi = {'in':(''),'out':('')})
        #--------------------
    def read_dat(self,files: list):
        """turns a list of files in to the base data

        Args:
            files_list (list): list of files directory
        """

        result = {}
        if type(files) == list:
            for index in range(len(files)):
                if path.exists(files[index]):    
                    importdat = open(files[index],'r')
                    data = importdat.read()
                    importdat.close()
                    result[files[index]] = data.split("\n")
            self.base_data = result
        else:
            raise TypeError('files must be a list')
        #--------------------
    def read_txt(self,files: list):
        """turns a list of files in to the base data

        Args:
            files_list (list): list of files directory
        """
        pass
        #--------------------
    def read_csv(self,files: list):
        """turns a list of files in to the base data

        Args:
            files_list (list): list of files directory
        """
        pass
        #--------------------
    def scan_data(self):
        markings_in = ('$in[','$In[','$IN[')
        markings_out = ('$out[','$Out[','$OUT[')

        for file in self.base_data:
            for line in range(len(self.base_data[file])):
                self.base_data[file][line] = self.base_data[file][line].split(';')[0]
                for item in ['Decl','Global','Const','Int','Signal','Bool','Defdat','Public','Enddat']:
                    self.base_data[file][line] = self.base_data[file][line].replace(item,'').replace(item.upper(),'').replace(item.lower(),'')
                self.base_data[file][line] = self.base_data[file][line].strip()

            self.base_data[file] = [x for x in self.base_data[file] if x != '']

            for line in range(len(self.base_data[file])):
                self.base_data[file][line] = self.base_data[file][line].split(' ')
                self.base_data[file][line] = [x for x in self.base_data[file][line] if x != '']
            
            for line in range(len(self.base_data[file])):
                if len(self.base_data[file][line]) == 1 and ((self.base_data[file][line][0].startswith(self.var_markings.singel['in']) or self.base_data[file][line][0].startswith(self.var_markings.singel['out']) and self.var_markings.aktiv)):
                    print(self.base_data[file][line])
                elif len(self.base_data[file][line]) == 2 and ((self.base_data[file][line][0].startswith(self.var_markings.singel['in']) or self.base_data[file][line][0].startswith(self.var_markings.singel['out']) and self.var_markings.aktiv)):
                    if self.base_data[file][line][1] not in self.longtext:
                        self.longtext[self.base_data[file][line][1]] = []
                    self.longtext[self.base_data[file][line][1]] += [self.base_data[file][line][0]]
                elif len(self.base_data[file][line]) == 3 and ((self.base_data[file][line][0].startswith(self.var_markings.singel['in']) or self.base_data[file][line][0].startswith(self.var_markings.singel['out']) and self.var_markings.aktiv)):
                    #if self.base_data[file][line][1] not in self.longtext:
                    #    self.longtext[self.base_data[file][line][1]] = []
                    print(self.base_data[file][line])
                elif len(self.base_data[file][line]) == 4 and ((self.base_data[file][line][0].startswith(self.var_markings.multi['in']) or self.base_data[file][line][0].startswith(self.var_markings.multi['out']) and self.var_markings.aktiv) or not self.var_markings.aktiv):
                    start_point = extract_number(self.base_data[file][line][1])
                    end_point = extract_number(self.base_data[file][line][3])
                    if type(start_point) == int and type(end_point) == int:
                        if self.base_data[file][line][1].startswith(markings_in) and self.base_data[file][line][3].startswith(markings_in):
                            var_type = '$IN'
                        elif self.base_data[file][line][1].startswith(markings_out) and self.base_data[file][line][3].startswith(markings_out):
                            var_type = '$OUT'
                        else:
                            print(self.base_data[file][line])
                            var_type = None
                        if type(var_type) == str:
                            sub_index = 0
                            for index in range(start_point,end_point + 1):
                                if var_type+'['+str(index)+']' not in self.longtext:
                                    self.longtext[var_type+'['+str(index)+']'] = []
                                self.longtext[var_type+'['+str(index)+']'] += [self.base_data[file][line][0] + ' 2**' + str(sub_index)]
                                sub_index += 1
                else:
                    print(self.base_data[file][line])

                markings = '$TIMER[','$COUNT_I[','$FLAG[','$CYC_FLAG[','$ANIN[','$ANOUT[','$IN[','$OUT['
                keys_to_remove = [key for key in self.longtext if not key.startswith(markings)]
                for key in keys_to_remove:
                    del self.longtext[key]
    def merge(self, other):
        if isinstance(other,Longtext):
            for key, value in other.longtext.items():
                if key in self.longtext:
                    self.longtext[key].extend(value)
                else:
                    self.longtext[key] = value
            return self.longtext
        else:
            raise TypeError('only Longtext can be added')
        #--------------------
    def delete_markings(self):
        for key in self.longtext:
            for value in self.longtext[key]:
                if value.startswith('$'):
                    self.longtext[key].remove(value)
            self.longtext[key] = [x for x in value if not x.startswith('$')]
    def delete_empty_lines(self):
        keys_to_remove = [key for key in self.longtext if self.longtext[key] == []]
        for key in keys_to_remove:
            del self.longtext[key]
        #----------------
    def check_for_errors(self):
        pass
        #----------------
    def export_csv(self,file_name: str,directory: str):
        if type(directory) == str:   
            final_file_name = validated_file_name(file_name)
            error_count = 0

            while (path.isfile(path.join(directory, final_file_name + '.csv'))):
                if path.isfile(path.join(directory, final_file_name + '.csv')):
                    basename, extension = path.splitext(final_file_name)
                    final_file_name = f"{basename}_copy{extension}"

                error_count += 1
            final_file_name = final_file_name + '.csv'
            self.log_name = final_file_name

            with open(path.join(directory, final_file_name), "w") as file:
                for key,value in self.longtext.items():
                    file.write(f'{key};{';'.join(value)}'.rstrip(';') + '\n')
            file.close()
        else:
            raise TypeError('directory must be a string')
        #--------------------
    def export_txt(self,file_name: str,directory: str):
        if type(directory) == str:   
            final_file_name = validated_file_name(file_name)
            error_count = 0
            while (path.isfile(path.join(directory, final_file_name + '.txt'))):
                if path.isfile(path.join(directory, final_file_name + '.txt')):
                    basename, extension = path.splitext(final_file_name)
                    final_file_name = f"{basename}_copy{extension}"

                error_count += 1
            final_file_name = final_file_name + '.txt'
            self.log_name = final_file_name

            with open(path.join(directory, final_file_name), "w") as file:
                for key,value in self.longtext.items():
                    file.write(f'{key} {' '.join(value)}'.rstrip() + '\n')
            file.close()
        else:
            raise TypeError('directory must be a string')
        #--------------------
    def export_log(self,file_name: str,directory: str):
        line = ''
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
                for key,value in self.longtext.items():
                    file.write(f'{key} {' '.join(value)}'.rstrip() + '\n')
            file.close()
        else:
            raise TypeError('directory must be a string')
        #-------------------- 