# -*- coding: utf-8 -*-

import pytest

from os import path

from src.core.longtext_func import validated_datpath
from src.core.longtext_func import extract_number

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
def test_extract_number():
    assert extract_number('Test01') == 1
    assert extract_number('Test010') == 10
    assert extract_number('Test01ghg5') == 1