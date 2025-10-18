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
import pytest
import random
from pprint import pprint
from tempfile import NamedTemporaryFile
from src.core.kuka import Longtext
from src.core.kuka import Marking

@pytest.fixture(scope="module")
def prep_longtext():
    def _create_longtext(test_case):
        prep_lt = Longtext()
        count = 0
        
        match test_case:
            case 1:
                prep_lt.longtext = {
                    '$IN[1]': ['diTest'],
                    '$IN[2]': ['diTest','diTest'],
                    '$IN[3]': ['diTest','diTest','diTest'],
                    '$IN[4]': ['diTest','diTest','diTest','diTest'],
                    '$IN[5]': [],
                    '$IN[6]': [],
                    '$IN[7]': [],
                    '$IN[8]': [],
                }
                count = 3
            case 2:
                for i1 in range(random.randint(100,4000)):
                    match random.randint(1,2):
                        case 1:
                            n = str(f'$IN[{i1}]')
                        case 2:
                            n = str(f'$OUT[{i1}]')
                    prep_lt.longtext[n] = []
                    for i2 in range(random.randint(0,4)):
                        if i2 > 0:
                            prep_lt.longtext[n] += [f'Test {i2}']
                    if len(prep_lt.longtext[n]) > 1:
                        count += 1
        return prep_lt.longtext, count
    return _create_longtext
 
def test_check_for_double_declarations(prep_longtext):
    lt = Longtext()
    prep_lt, count = prep_longtext(1)
    lt.longtext = prep_lt.copy()
    assert lt.check_for_double_declarations() == count
    
    lt = Longtext()
    prep_lt, count = prep_longtext(2)
    lt.longtext = prep_lt.copy()
    assert lt.check_for_double_declarations() == count