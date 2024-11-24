# -*- coding: utf-8 -*-

import pytest

from time import sleep

from src.dev_func import dummy_prog
from src.dev_func import debug_print
from src.dev_func import print_list
from src.dev_func import print_dict
from src.dev_func import in_range
from src.dev_func import in_tolerance
from src.dev_func import Cycle_Time

def test_dummy_prog(capsys):
    dummy_prog()
    captured = capsys.readouterr()
    assert captured.out == 'Dummy Prog\n'    
    #--------------------
def test_debug_print(capsys):
    debug_print(True)
    captured = capsys.readouterr()
    assert captured.out == 'True\n'
    debug_print('String')
    captured = capsys.readouterr()
    assert captured.out == 'String\n'
    debug_print(10)
    captured = capsys.readouterr()
    assert captured.out == '10\n'
    debug_print(10.0)
    captured = capsys.readouterr()
    assert captured.out == '10.0\n'
    debug_print([1,2])
    captured = capsys.readouterr()
    assert captured.out == '[1, 2]\n'
    debug_print({1: '1',2: '2'})
    captured = capsys.readouterr()
    assert captured.out == '''{1: '1', 2: '2'}\n'''
    #-------------------- 
def test_print_list(capsys):
  
    print_list([1,2,3,4,5])
    captured = capsys.readouterr()
    assert captured.out == '''==============\nlen=5\n1\n2\n3\n4\n5\n==============\n'''

    with pytest.raises(TypeError):print_list() 
    with pytest.raises(TypeError):print_list(True)   
    with pytest.raises(TypeError):print_list(10)
    with pytest.raises(TypeError):print_list(10.0)
    #--------------------
def test_print_dict(capsys):

    print_dict({1:'1',2:'2'})
    captured = capsys.readouterr()
    assert captured.out == '''==============\nlen=2\nKey:1 Value:1\nKey:2 Value:2\n==============\n'''
    '''==============
    len=2
    Key:1 Value:1
    Key:2 Value:2
    =============='''

    with pytest.raises(TypeError):print_dict() 
    with pytest.raises(TypeError):print_dict(True)   
    with pytest.raises(TypeError):print_dict(10)
    with pytest.raises(TypeError):print_dict(10.0)
    with pytest.raises(TypeError):print_dict('String')
    # with pytest.raises(TypeError):print_dict([1,2,3])
    #--------------------
def test_in_range():

    assert in_range(5,0,10) == True
    assert in_range(5,0,10.1) == True
    assert in_range(5.5,0,10.1) == True
    assert in_range(-1,0,10) == False
    assert in_range(-1.1,0,10) == False
    assert in_range(10,100,1) == False
    assert in_range([5],[1],[10]) == True
    assert in_range([5,5],[1,1],[10,10]) == True
    assert in_range(True,False,False) == False
    assert in_range(False,False,False) == True
    assert in_range(True,True,True) == True

    with  pytest.raises(TypeError):in_range()
    with  pytest.raises(TypeError):in_range(1)
    with  pytest.raises(TypeError):in_range(50,10)
    #--------------------
def test_in_in_tolerance():
    assert in_tolerance(9,10,1.5) == True
    assert in_tolerance(9.0,10.0,1) == True
    assert in_tolerance(95.5,100.0,15.5) == True
    assert in_tolerance(7,10,1.5) == False
    assert in_tolerance(95.5,10,1.5) == False

    with  pytest.raises(TypeError):in_tolerance()
    with  pytest.raises(TypeError):in_tolerance(95)
    with  pytest.raises(TypeError):in_tolerance(95,100)
    with  pytest.raises(TypeError):in_tolerance(95,100,[10])
    #--------------------
def test_Cycle_Time():
    cycle_time_test01 = Cycle_Time('cycle_time_test01')
    cycle_time_test02 = Cycle_Time('cycle_time_test02')
    cycle_time_test01.start()
    cycle_time_test02.start()
    sleep(0.5)
    cycle_time_test01.stop()
    cycle_time_test02.stop()
    assert cycle_time_test01.name() == 'cycle_time_test01'
    assert in_tolerance(cycle_time_test01.read(),0.5,0.01) == True
    assert in_tolerance(cycle_time_test02.read(),0.5,0.01) == True
    cycle_time_test01.start()
    sleep(0.5)
    cycle_time_test01.stop()
    assert in_tolerance(cycle_time_test01.read(),0.5,0.01) == True