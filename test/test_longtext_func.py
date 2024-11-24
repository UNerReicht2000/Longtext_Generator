# -*- coding: utf-8 -*-

import pytest

from os import path

from src.core.longtext_func import delete_content
from src.core.longtext_func import create_file_with_list
from src.core.longtext_func import validated_datname
from src.core.longtext_func import lode_user_files
from src.core.longtext_func import delete_comment
from src.core.longtext_func import add_in_longtext
from src.core.longtext_func import delete_all_empty_lines
from src.core.longtext_func import Buffer
from src.core.longtext_func import Creat_Error_String
from src.core.longtext_func import validated_datpath
from src.core.longtext_func import clean_up_longtext

CreatErrStr = Creat_Error_String()
Errorbuffer = Buffer()

def test_delete_content():
    assert delete_content([1,2,3,5,5,5,5],5) == [1,2,3]
    assert delete_content(['a','a','b'],'a') == ['b']
    assert delete_content([1.1,1.1,1.1,2],1.1) == [2]
    assert delete_content('test01','0') == 'test1'
    assert delete_content('test01       ',' ') == 'test01'

    with pytest.raises(TypeError):
        delete_content()
    with pytest.raises(TypeError):
        delete_content(1)
    with pytest.raises(TypeError):
        delete_content(1.1)
    with pytest.raises(TypeError):
        delete_content({'1': 1})

    #--------------------
def test_create_file_with_list():
    with pytest.raises(TypeError):
        create_file_with_list()
    #--------------------
def test_validated_datname():
    assert validated_datname('Text') == 'Text'
    assert validated_datname('Test01') == 'Test01'
    assert validated_datname('Text_a') == 'Text_a'
    assert validated_datname('Text/') == 'Langtext'
    assert validated_datname('Text*Text') == 'Langtext'
    assert validated_datname('|Text|') == 'Langtext'
    assert validated_datname('|*/Text') == 'Langtext'
    assert validated_datname('') == 'Langtext'
    with pytest.raises(TypeError):
        validated_datname()
    #--------------------
def test_lode_user_files():
    if False:
        list_of_files = [
            r"C:\Users\ungerd\Desktop\Testdateien\test_file_01.txt",
            r"C:\Users\ungerd\Desktop\Testdateien\test_file_02.txt",
            ]
        assert lode_user_files(list_of_files) == [
                                            '1some data',
                                            '2some data',
                                            '3some data',
                                            '1some data',
                                            '2some data',
                                            '3some data',
                                            ]
        list_of_files = [
            r"C:\Users\ungerd\Desktop\Testdateien\test_file_01.txt",
            ]
        assert lode_user_files(list_of_files) == [
                                            '1some data',
                                            '2some data',
                                            '3some data',
                                            ]
        list_of_files = [
            r"C:\Users\ungerd\Desktop\Testdateien\test_file_02.txt",
            ]
        assert lode_user_files(list_of_files) == [
                                            '1some data',
                                            '2some data',
                                            '3some data',
                                            ]
    with pytest.raises(TypeError):
        lode_user_files()
    #--------------------
def test_delete_comments():
    assert delete_comment('1TextTextTextText.001;TextText') == '1TextTextTextText.001'
    assert delete_comment(r'2TextTextTextText112110.002;TextText1112110') == r'2TextTextTextText112110.002'
    assert delete_comment('3TextTextTextText1112110.003 ; TextText1112110') == '3TextTextTextText1112110.003'
    assert delete_comment('4TextTextTextText1112110.004#TextText1112110') == '4TextTextTextText1112110.004#TextText1112110'
    assert delete_comment('5TextTextTextText1112110.005#TextText1112110','#') == '5TextTextTextText1112110.005'

    with pytest.raises(TypeError):
        delete_comment()
    # with pytest.raises(TypeError):
        # delete_comment(1)
    #--------------------    
def test_CreatErrStr_wrong_length():
    TestList = []
    assert CreatErrStr.wrong_length(TestList) == 'Error: String konnte nicht Gebildet werden! Errorliste ist nicht mehr Valide'
    assert CreatErrStr.wrong_length(TestList,1) == 'Error: Variabel konnte nicht erkannt werden (WrongLength)'
    assert CreatErrStr.wrong_length(TestList,2) == 'Error: Variabel konnte nicht erkannt werden (WrongLength)'
    TestList = ['BITestTest1']
    assert CreatErrStr.wrong_length(TestList,1) == 'Invalide Variable:"BITestTest1" Soll IO-Zuweisungen=1 Ist IO-Zuweisungen=0 (WrongLength)'
    TestList = ['BITestTest2']
    assert CreatErrStr.wrong_length(TestList,2) == 'Invalide Variable:"BITestTest2" Soll IO-Zuweisungen=2 Ist IO-Zuweisungen=0 (WrongLength)'
    with pytest.raises(TypeError):
        CreatErrStr.wrong_length()
    #--------------------
def test_CreatErrStr_no_decimal():
    pass
    assert CreatErrStr.no_decimal([]) == 'Error: Variabel konnte nicht erkannt werden (NoDecimal)'
    assert CreatErrStr.no_decimal([r'BITestTest1']) == 'Invalide Variable: Unerwartete zeichen erkannt:BITestTest1 (NoDecimal)'
    with pytest.raises(TypeError):
        CreatErrStr.no_decimal()
    #--------------------
def test_ErrorBuffer():
    pass
    ''''''
    #--------------------
def test_validated_datpath():
    assert validated_datpath('das_gibt_es_nicht') == False
    #assert validated_datpath(r'C:\Users\ungerd\Desktop\Testdateien') == True
    assert validated_datpath(r'C:\Users\ungerd\Desktop\Testdateien*') == False
    assert validated_datpath(r'C:\Users\ungerd\Desktop\Testdeien*') == False

    with pytest.raises(TypeError):validated_datpath()
    with pytest.raises(TypeError):validated_datpath(1)
    with pytest.raises(TypeError):validated_datpath([1])
    with pytest.raises(TypeError):validated_datpath(1.1)
    with pytest.raises(TypeError):validated_datpath(['test'])
    #--------------------
def test_clen_up_longtext():
    test_basedata = ['sting ; sting;;;','string;',';',]
    result_data = ['sting ; sting','string','',]
    assert clean_up_longtext(test_basedata,0) == result_data

    test_basedata = ['sting ; sting;;;;;;;;;;','string;',';',]
    result_data = ['sting ; sting','string','',]
    assert clean_up_longtext(test_basedata,0) == result_data

    test_basedata = ['sting ; sting;;;','string;',';',]
    result_data = ['sting   sting','string','',]
    assert clean_up_longtext(test_basedata,1) == result_data

    with pytest.raises(TypeError):clean_up_longtext()
    with pytest.raises(TypeError):clean_up_longtext(1,1)
    #--------------------