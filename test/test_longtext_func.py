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