# -*- coding: utf-8 -*-

try:
    from dev_func import debug_print
    from dev_func import print_list
    from dev_func import in_range
except ImportError:
    from src.dev_func import debug_print
    from src.dev_func import print_list
    from src.dev_func import in_range    

from os import path
from os import access
from os import R_OK
from os import W_OK

from re import search

def delete_content(in_data: list, delete: int|float|str) -> list:
    """_summary_

    Args:
        in_data (list): list to be edited
        delete (int | float | str): what should be deleted

    Returns:
        list: finished edited list
    """

    return_value = ''
    if type(in_data) == list:
        while delete in in_data:
            in_data.remove(delete)

        return in_data
    elif type(in_data) == str:
        in_data = list(in_data)
        while delete in in_data:
            in_data.remove(delete)
        return return_value.join(in_data)     
    #--------------------
def create_file_with_list (datname: str,file_part: str,data: list,data_typ: int = 0) -> str:
    """Creates a file with the contents of a list

    Args:
        datname (str): name of the file
        filepart (str): the storage location of the file
        data (list): the list with which the file is created
        data_typ (int, optional): datetyp (.csv = 0|.txt = 1). Defaults to 0.

    Returns:
        str: name of the File
    """

    data_types = {0: '.csv',1: '.txt'}

    final_dataname = datname 
    error_count = 0
    while (path.isfile(path.join(file_part, final_dataname+data_types[data_typ]))):
        if path.isfile(path.join(file_part, final_dataname+data_types[data_typ])):
            basename, extension = path.splitext(final_dataname)
            final_dataname = f"{basename}_copy{extension}"

        error_count += 1
    final_dataname = final_dataname+data_types[data_typ]  

    with open(path.join(file_part, final_dataname), "w") as dat:
        for index in range(len(data)): 
            dat.write(data[index]+'\n')
    dat.close()
    return final_dataname      
    #--------------------
def validated_file_name(file_name: str) -> str:
    """checkt the name 

    Args:
        datname (str): name to check

    Returns:
        str: if OK then input name else Langtext
    """

    default_name = 'Langtext'
    if file_name.isspace():
        return default_name
    
    if len(file_name) <= 0:
        return default_name
    
    if len(file_name) > 39:
        return default_name
    
    BlackList = ['/','*','|']
    for item in BlackList:
        if item in list(file_name):
            return default_name
    return file_name
    #--------------------
def lode_user_files(files_list: list) -> list:
    """turns a list of files into a list

    Args:
        files_list (list): list of files directory

    Returns:
        list: List with contents of the files
    """

    return_list = []

    for index in range(len(files_list)):
        if path.exists(files_list[index]):    
            importdat = open(files_list[index],'r')
            data = importdat.read()
            importdat.close()
            return_list = return_list + data.split("\n")    
    return return_list
    #--------------------
def delete_comment(string: str,comment_marker: str = ";") -> str:
    """delete the comment 

    Args:
        string (str): input string
        comment_marker (str, optional): commentmacker. Defaults to ";".

    Returns:
        str: output string without comment
    """

    if not (string.find(comment_marker) == -1) and not (comment_marker == ' ') and not (string == '') and not (len(string) == -1) and not (len(string) == 0):
        point_of_marker = string.find(comment_marker)
        string = list(string)
        for index in range(point_of_marker,len(string)):
            string[index] = string[index].replace(comment_marker," ")
            string[index] = string[index].replace(string[index]," ")
        new_string = ''.join(string)
        return new_string.strip()
    else:
        return string
    #--------------------
def add_in_longtext(data: list,longtext: list,start_index: int,typ: str,dat_typ: int) -> list:
    """imports the found variables into the longtext

    Args:
        data (list): list to be imported
        longtext (list): basis longtext
        start_index (int): start index
        typ (str): $IN or $OUT

    Returns:
        list: longtext wiht new data
    """

    """    
    1    = $TIMER[1]    Listindex 0
    61   = $COUNT_I[1]  Listindex 60
    221  = $Flag[1]     Listindex 220
    1220 = $CYCFlag[1]  Listindex 1219
    1440 = $IN[1]       Listindex 1539
    5536 = $OUT[1]      Listindex 5635
    """

    separation_macker = {0: ';',1: ' '}
    for index in range(len(data)):
        for write in range(len(longtext) - start_index):
            if (longtext[write + start_index].find(typ + str(data[index][1])+']') >= 0):
                longtext[write + start_index] += separation_macker[dat_typ]
                longtext[write + start_index] += data[index][0]
    return longtext
    #--------------------
def delete_all_empty_lines(data: list) -> list:
    """delete all empty lines 

    Args:
        data (list): raw longtext

    Returns:
        list: new longtext
    """

    for index in range(len(data)):
        
        if in_range(index,1439,1447) and (len(data[index]) <= 6):
            data[index] = ''
        elif (in_range(index,1448,1537) or in_range(index,5535,5543)) and (len(data[index]) <= 7):
            data[index] = ''
        elif (in_range(index,120,128) or in_range(index,1375,1383) or in_range(index,1538,2437) or in_range(index,5544,5633)) and (len(data[index]) <= 8):
            data[index] = ''  
        elif (in_range(index,1,8) or in_range(index,129,218) or in_range(index,1384,1415) or in_range(index,2438,5534) or in_range(index,5634,6533)) and (len(data[index]) <= 9):
            data[index] = ''
        elif (in_range(index,9,59) or in_range(index,219,1118) or in_range(index,1416,1438) or in_range(index,6534,9630)) and (len(data[index]) <= 10):
            data[index] = ''
        elif in_range(index,60,68) and (len(data[index]) <= 11):
            data[index] = ''
        elif (in_range(index,69,119) or in_range(index,1119,1127)) and (len(data[index]) <= 12):
            data[index] = ''
        elif (in_range(index,1128,1217) or index == 0) and (len(data[index]) <= 13):
            data[index] = ''
        elif in_range(index,1218,1374) and (len(data[index]) <= 14):
            data[index] = ''
    for index in range(data.count('')):
        data.remove('')
    return data
    #--------------------
class Buffer:
    def __init__(self):
        self.error_buffer = []
        self.data_typ = r'.txt'
        #--------------------
    def append(self,entry):
        """append the entry in the Buffer

        Args:
            entry (any): what should be entered
        """
        self.error_buffer.append(entry)
        #--------------------
    def clear(self):
        """clear the Buffer
        """
        self.error_buffer.clear()
        #--------------------                 
    def export_dat(self,datname: str, file_part: str):
        """Exports the buffer as a txt file

        Args:
            datname (str): datname of the export
            file_part (str): file part of the export
        """
        data_typ = r'.txt'
        
        final_dataname = datname 
        error_count = 0
        while (path.isfile(path.join(file_part, final_dataname+data_typ))):
            if path.isfile(path.join(file_part, final_dataname+data_typ)):
                SBasename, SExtension = path.splitext(final_dataname)
                final_dataname = f"{SBasename}_copy{SExtension}"

            error_count = error_count + 1
        final_dataname = final_dataname+data_typ  

        header = '''Liste mit Allen Fehlern die Beim Erstellen des Langtextes gefunden wurden.\nList of all Errors That were found when creating the Longtext.\n'''

        with open(path.join(file_part, final_dataname), "w") as Datei:
            Datei.write(header)
            for index in range(len(self.error_buffer)): 
                Datei.write(self.error_buffer[index]+'\n')      
        #--------------------
class Creat_Error_String():
    def wrong_length(self,in_data: list,normal_len: int = -1):
        errortext = ''
        if normal_len != -1:
            if (len(in_data) == 0):
                errortext = 'Error: Variabel konnte nicht erkannt werden (WrongLength)'
            elif(len(in_data) >= 1):
                temp_string = in_data[0]
                in_data.pop(0)
                if(len(in_data) == 0):                  
                    errortext = f'Invalide Variable:"{temp_string}" Soll IO-Zuweisungen={normal_len} Ist IO-Zuweisungen={len(in_data)} (WrongLength)'
                elif(len(in_data) != normal_len):
                    errortext = f'Invalide Variable:"{temp_string}" Soll IO-Zuweisungen={normal_len} Ist IO-Zuweisungen={len(in_data)} (IO´s:{in_data}) (WrongLength)'
                else: 
                    errortext = f'Invalide Variable:"{temp_string}" (IO`s:{in_data}) Not Manageable Error (WrongLength)'
        else:
            errortext = 'Error: String konnte nicht Gebildet werden! Errorliste ist nicht mehr Valide'     
            
        return errortext
        #--------------------
    def no_decimal(self,in_data: list) -> str:
        #.isdecimal()
        if (len(in_data) == 0):
            errortext = 'Error: Variabel konnte nicht erkannt werden (NoDecimal)'
        if(len(in_data) >= 1):
            if(len(in_data) == 1):
                errortext = f'Invalide Variable: Unerwartete zeichen erkannt:{in_data[0]} (NoDecimal)'
            elif(len(in_data) >= 1):  
                temp_string = in_data[0]
                in_data.pop(0)                
                errortext = f'Invalide Variable: Unerwartete zeichen erkannt:{temp_string}.-> {in_data} (NoDecimal)'   
        return errortext
        #--------------------
    #--------------------
def validated_datpath(file_path: str) -> bool:
    """ check the filepart

    Args:
        file_path (str): input filepart.

    Returns:
        bool: test result 
    """
    if not path.exists(file_path):
        debug_print('not path.exists(file_path)')
        return False
    
    if not access(file_path, R_OK | W_OK):
        debug_print('not access(file_path, R_OK | W_OK)')
        return False
    
    # blacklist =['*','?','"','<','>','|'] 
    blacklist_of_characters=[
        '\\', '*', '?', '"', '<', '>', '|',  # Allgemein verbotene Zeichen
        '\0',  # Nullzeichen
        ]
    
    for item in blacklist_of_characters:
        if item in list(file_path):
            debug_print(f'blacklist_of_characters ({item})')
            return False

    blacklist_of_names = [
        'CON', 'PRN', 'AUX', 'NUL',  # Reservierte Dateinamen unter Windows
        'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',  # Reservierte COM-Ports unter Windows
        'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'  # Reservierte LPT-Ports unter Windows
        ]
    
    for item in blacklist_of_names:
        if item in list(file_path):
            debug_print(f'blacklist_of_names ({item})')
            return False
    return True
    #--------------------
def clean_up_longtext(longtext: list,data_typ: int = 0) -> list:
    """clean the longtext for the KRC

    Args:
        longtext (list): longtext to clean up
        data_typ (int): datatyp (.csv = 0|.txt = 1). Defaults to 0.

    Returns:
        list: clean longtext
    """

    data_types = {0: '.csv',1: '.txt'}
    if data_typ == 0:
        for index in range(len(longtext)):
            longtext[index] = longtext[index].rstrip(';')
    elif data_typ == 1:
         for index in range(len(longtext)):
            longtext[index] = longtext[index].replace(';',' ')
            longtext[index] = longtext[index].strip()
    else:
        print('Error')      
    
    return longtext
    #--------------------
def extract_number(input_string: str):
    """Extracts the first number from a given string.

    Args:
        input_string (str): The input string from which to extract the number.

    Returns:
        int: The extracted number as an integer. Returns None if no number is found.
    """
    match = search(r'\d+', input_string)
    if match:
        return int(match.group())
    return None
    #--------------------