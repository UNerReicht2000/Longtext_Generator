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

import re

from time import time

def extract_number(input_string: str):
    """Extracts the first number from a given string.

    Args:
        input_string (str): The input string from which to extract the number.

    Returns:
        int: The extracted number as an integer. Returns None if no number is found.
    """
    match = re.search(r'\d+', input_string)
    if match:
        return int(match.group())
    return None
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
def validated_datpath(file_path: str) -> bool:
    """ check the filepart

    Args:
        file_path (str): input filepart.

    Returns:
        bool: test result 
    """
    if not os.path.exists(file_path):
        print('not path.exists(file_path)')
        return False
    
    if not os.access(file_path, os.R_OK | os.W_OK):
        print('not access(file_path, R_OK | W_OK)')
        return False
    
    # blacklist =['*','?','"','<','>','|'] 
    blacklist_of_characters=[
        '\\', '*', '?', '"', '<', '>', '|',  # Allgemein verbotene Zeichen
        '\0',  # Nullzeichen
        ]
    
    for item in blacklist_of_characters:
        if item in list(file_path):
            print(f'blacklist_of_characters ({item})')
            return False

    blacklist_of_names = [
        'CON', 'PRN', 'AUX', 'NUL',  # Reservierte Dateinamen unter Windows
        'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',  # Reservierte COM-Ports unter Windows
        'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'  # Reservierte LPT-Ports unter Windows
        ]
    
    for item in blacklist_of_names:
        if item in list(file_path):
            print(f'blacklist_of_names ({item})')
            return False
    return True
    #--------------------
class CycleTime():
    def __init__(self,name: str = 'Cycle_Time') -> None:
        """init the Cycle Time

        Args:
            name (str, optional): name of cycle timer. Defaults to 'Cycle_Time'.
        """
        self.timer_name = name
        self.cycle_time = 0.0 
        self.start_time = 0.0
        #--------------------
    def start(self) -> None:
        """start the timer
        """
        self.cycle_time = 0.0
        self.start_time = time()
        #--------------------
    def stop(self) -> None:
        """stop the timer
        """
        self.cycle_time = time() - self.start_time
        #--------------------
    def read(self) -> float:
        """read the time

        Returns:
            float: returns the measured time
        """
        return self.cycle_time
        #--------------------  
    def __call__(self) -> str:
        """print pretty the cycle time
        """
        result_string = f'the measured time of {self.timer_name} is: {self.cycle_time}'
        print(result_string)
        return result_string
        #--------------------
    #--------------------