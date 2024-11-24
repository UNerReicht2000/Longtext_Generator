# -*- coding: utf-8 -*-

from time import time

def dummy_prog() -> None:
    """it doesn't do anything
    """
    print('Dummy Prog')
    #--------------------
def debug_print(debug_msg: any) -> None:
    """send a debug message

    Args:
        debug_msg (any): debug text or info
    """

    if True: 
        print(debug_msg)
    #--------------------
def print_list(in_list: list) -> None:
    """Print a list pretty with the length of the list.

    Args:
        in_list (list): some list
    """

    print("==============")
    print(f'len={len(in_list)}')
    for entry in in_list:
        print(entry)
    print("==============")
    #--------------------
def print_dict(in_dict: dict) -> None:
    """Print a dictionary pretty with the length of the dictionary.

    Args:
        in_list (dict): some dict
    """

    print("==============")
    print(f'len={len(in_dict)}')
    for key in in_dict:
        print(f'Key:{key} Value:{in_dict[key]}')    
    print("==============")
    #--------------------
def in_range(value: int|float,min_value: int|float,max_value: int|float) -> bool:
    """check is a Value in range 

    Args:
        value (int, float): Value to be checked
        min_value (int, float): min Value
        max_value (int, float): max Value

    Returns:
        bool: If the value is in the range then true is returned
    """
    
    return min_value <= value <= max_value   
    #--------------------
def in_tolerance(value1: int|float,value2: int|float,tolerance: int|float) -> bool:
    """checks whether value 1 is in the tolerance range of value 2

    Args:
        value1 (int | float): check velue
        value2 (int | float): anchor velue
        tolerance (int | float): tolerance range

    Returns:
        bool: is in the tolerant or not
    """

    return abs(value1 - value2) <= tolerance
    #--------------------
class Cycle_Time():
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
    def name(self) -> str:
        """name of cycletimer

        Returns:
            str: return name of cycletimer
        """
        return self.timer_name 
        #--------------------
    def pretty_print(self) -> str:
        """print pretty the cycle time
        """
        result_string = f'the measured time of {self.timer_name} is: {self.cycle_time}'
        print(result_string)
        return result_string
        #--------------------
    #--------------------