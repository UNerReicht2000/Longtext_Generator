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
from os import remove as os_remove
from tempfile import NamedTemporaryFile
from src.core.kuka import Longtext
from src.core.kuka import Marking

@pytest.fixture(scope="module")
def user_inputs():
    def _created_user_inputs(test_case):
        match test_case:
            case 10:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=()),
                    Marking(aktiv=True, name="Digital Output", var_prefix=()),
                    Marking(aktiv=True, name="Analog Input", var_prefix=()),
                    Marking(aktiv=True, name="Analog Output", var_prefix=()),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=()),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=()),
                ]
            case 11:
                return [
                    Marking(aktiv=False, name="Digital Input", var_prefix=()),
                    Marking(aktiv=False, name="Digital Output", var_prefix=()),
                    Marking(aktiv=False, name="Analog Input", var_prefix=()),
                    Marking(aktiv=False, name="Analog Output", var_prefix=()),
                    Marking(aktiv=False, name="Grouped Input", var_prefix=()),
                    Marking(aktiv=False, name="Grouped Output", var_prefix=()),
                ]
            case 12:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=("x")),
                    Marking(aktiv=True, name="Digital Output", var_prefix=("x")),
                    Marking(aktiv=True, name="Analog Input", var_prefix=("x")),
                    Marking(aktiv=True, name="Analog Output", var_prefix=("x")),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=("x")),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=("x")),
                ]
            case 13:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=()),
                    Marking(aktiv=True, name="Digital Output", var_prefix=()),
                    Marking(aktiv=False, name="Analog Input", var_prefix=()),
                    Marking(aktiv=False, name="Analog Output", var_prefix=()),
                    Marking(aktiv=False, name="Grouped Input", var_prefix=()),
                    Marking(aktiv=False, name="Grouped Output", var_prefix=()),
                ]
            case 14:
                return [
                    Marking(aktiv=False, name="Digital Input", var_prefix=()),
                    Marking(aktiv=False, name="Digital Output", var_prefix=()),
                    Marking(aktiv=True, name="Analog Input", var_prefix=()),
                    Marking(aktiv=True, name="Analog Output", var_prefix=()),
                    Marking(aktiv=False, name="Grouped Input", var_prefix=()),
                    Marking(aktiv=False, name="Grouped Output", var_prefix=()),
                ]
            case 15:
                return [
                    Marking(aktiv=False, name="Digital Input", var_prefix=()),
                    Marking(aktiv=False, name="Digital Output", var_prefix=()),
                    Marking(aktiv=False, name="Analog Input", var_prefix=()),
                    Marking(aktiv=False, name="Analog Output", var_prefix=()),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=()),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=()),
                ]
            case 20:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=("di")),
                    Marking(aktiv=True, name="Digital Output", var_prefix=("do")),
                    Marking(aktiv=False, name="Analog Input", var_prefix=("ai")),
                    Marking(aktiv=False, name="Analog Output", var_prefix=("ao")),
                    Marking(aktiv=False, name="Grouped Input", var_prefix=("gi")),
                    Marking(aktiv=False, name="Grouped Output", var_prefix=("go")),
                ]
            case 21:
                return [
                    Marking(aktiv=False, name="Digital Input", var_prefix=("di")),
                    Marking(aktiv=False, name="Digital Output", var_prefix=("do")),
                    Marking(aktiv=True, name="Analog Input", var_prefix=("ai")),
                    Marking(aktiv=True, name="Analog Output", var_prefix=("ao")),
                    Marking(aktiv=False, name="Grouped Input", var_prefix=("gi")),
                    Marking(aktiv=False, name="Grouped Output", var_prefix=("go")),
                ]
            case 22:
                return [
                    Marking(aktiv=False, name="Digital Input", var_prefix=("di")),
                    Marking(aktiv=False, name="Digital Output", var_prefix=("do")),
                    Marking(aktiv=False, name="Analog Input", var_prefix=("ai")),
                    Marking(aktiv=False, name="Analog Output", var_prefix=("ao")),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=("gi")),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=("go")),
                ]
            case 30:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=("di")),
                    Marking(aktiv=True, name="Digital Output", var_prefix=("do")),
                    Marking(aktiv=False, name="Analog Input", var_prefix=("ai")),
                    Marking(aktiv=False, name="Analog Output", var_prefix=("ao")),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=("gi")),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=("go")),
                ]
    return _created_user_inputs

@pytest.fixture(scope="module")
def kuka_var_data():
    def _create_var_data(test_case):
        match test_case:
            case 10:
                prep_lt = Longtext()
                dat_file_sampel = b"""
                    ;Test file template for KUKA Longtext
                    GLOBAL SIGNAL test_input_1 = $IN[1]
                    GLOBAL SIGNAL test_input_2=$IN[2]
                    GLOBAL SIGNAL test_input_3 = $in[3]
                    GLOBAL SIGNAL test_input_4=$In[4]
                    GLOBAL SIGNAL test_input_5 = $IN[5]
                    GLOBAL SIGNAL test_input_6 = $IN[6]
                    GLOBAL SIGNAL test_input_7 = $IN[7]
                    GLOBAL SIGNAL test_input_8 = $IN[8]
                    GLOBAL SIGNAL test_group_input_1 = $In[9] TO $IN[16]
                    GLOBAL SIGNAL test_group_input_2=$IN[17] TO $IN[24]

                    GLOBAL SIGNAL test_anin_1 = $ANIN[1]
                    GLOBAL SIGNAL test_anin_2=$anin[2]

                    GLOBAL SIGNAL test_output_1 = $OUT[1]
                    GLOBAL SIGNAL test_output_2=$OUT[2]
                    GLOBAL SIGNAL test_output_3 = $OUT[3]
                    GLOBAL SIGNAL test_output_4 = $OUT[4]
                    GLOBAL SIGNAL test_output_5 = $OUT[5]
                    GLOBAL SIGNAL test_output_6 = $OUT[6]
                    GLOBAL SIGNAL test_output_7 = $OUT[7]
                    GLOBAL SIGNAL test_output_8 = $OUT[8]
                    GLOBAL SIGNAL test_group_output_1 = $OUT[9] TO $OUT[16]
                    GLOBAL SIGNAL test_group_output_2=$OUT[17] TO $OUT[24]

                    GLOBAL SIGNAL test_anout_1 = $ANOUT[1]
                    GLOBAL SIGNAL test_anout_2=$ANOUT[2]
                    """
                file = NamedTemporaryFile(
                    prefix="dat_file_", suffix=".dat", mode="w+b", delete_on_close=False
                )
                file.write(dat_file_sampel)
                file.seek(0)
                file.close()
                prep_lt.read_dat([file.name])
                os_remove(file.name)
                return prep_lt.base_data
            case 20:
                prep_lt = Longtext()
                dat_file_sampel = b"""
                    ;Test file template for KUKA Longtext
                    GLOBAL SIGNAL di_test_input_1 = $IN[1]
                    GLOBAL SIGNAL di_test_input_2=$IN[2]
                    GLOBAL SIGNAL di_test_input_3 = $IN[3]
                    GLOBAL SIGNAL di_test_input_4 = $IN[4]
                    GLOBAL SIGNAL di_test_input_5 = $IN[5]
                    GLOBAL SIGNAL di_test_input_6 = $IN[6]
                    GLOBAL SIGNAL test_input_7 = $IN[7]
                    ;GLOBAL SIGNAL di_test_input_8 = $IN[8]
                    
                    GLOBAL SIGNAL gi_test_group_input_1 = $IN[9] TO $IN[10]
                    GLOBAL SIGNAL gi_test_group_input_2=$IN[11] TO $IN[12]
                    GLOBAL SIGNAL test_group_input_3=$IN[13] TO $IN[14]
                    ;GLOBAL SIGNAL gi_test_group_input_4=$IN[15] TO $IN[16]

                    GLOBAL SIGNAL ai_test_anin_1 = $ANIN[1]
                    GLOBAL SIGNAL ai_test_anin_2=$ANIN[2]
                    GLOBAL SIGNAL test_anin_3=$ANIN[3]
                    ;GLOBAL SIGNAL ai_test_anin_4=$ANIN[4]

                    GLOBAL SIGNAL do_test_output_1 = $OUT[1]
                    GLOBAL SIGNAL do_test_output_2=$OUT[2]
                    GLOBAL SIGNAL do_test_output_3 = $OUT[3]
                    GLOBAL SIGNAL do_test_output_4 = $OUT[4]
                    GLOBAL SIGNAL do_test_output_5 = $OUT[5]
                    GLOBAL SIGNAL do_test_output_6 = $OUT[6]
                    GLOBAL SIGNAL test_output_7 = $OUT[7]
                    ;GLOBAL SIGNAL do_test_output_8 = $OUT[8]
                    
                    GLOBAL SIGNAL go_test_group_output_1 = $OUT[9] TO $OUT[10]
                    GLOBAL SIGNAL go_test_group_output_2=$OUT[11] TO $OUT[12]
                    GLOBAL SIGNAL test_group_output_3=$OUT[13] TO $OUT[14]
                    ;GLOBAL SIGNAL go_test_group_output_4=$OUT[15] TO $OUT[16]

                    GLOBAL SIGNAL ao_test_anout_1 = $ANOUT[1]
                    GLOBAL SIGNAL ao_test_anout_2=$ANOUT[2]
                    GLOBAL SIGNAL test_anout_3=$ANOUT[3]
                    ;GLOBAL SIGNAL ao_test_anout_4=$ANOUT[4]
                    """
                file = NamedTemporaryFile(
                    prefix="dat_file_", suffix=".dat", mode="w+b", delete_on_close=False
                )
                file.write(dat_file_sampel)
                file.seek(0)
                file.close()
                prep_lt.read_dat([file.name])
                os_remove(file.name)
                return prep_lt.base_data
            case 30:
                prep_lt = Longtext()
                dat_file_sampel = b"""
                    ;Test file template for KUKA Longtext
                    GLOBAL SIGNAL di_test_input_1 = $IN[1]
                    GLOBAL SIGNAL di_test_input_2=$OUT[2]
                    
                    GLOBAL SIGNAL gi_test_group_input_1 = $IN[9] TO $IN[10]
                    GLOBAL SIGNAL gi_test_group_input_2=$OUT[11] TO $OUT[12]
                    GLOBAL SIGNAL gi_test_group_input_3=$IN[13] TO $OUT[14]

                    GLOBAL SIGNAL do_test_output_1 = $OUT[1]
                    GLOBAL SIGNAL do_test_output_2=$IN[2]
                    
                    GLOBAL SIGNAL go_test_group_output_1 = $OUT[9] TO $OUT[10]
                    GLOBAL SIGNAL go_test_group_output_2=$OUT[11] TO $OUT[12]
                    GLOBAL SIGNAL go_test_group_output_3=$IN[13] TO $OUT[14]
                    """
                file = NamedTemporaryFile(
                    prefix="dat_file_", suffix=".dat", mode="w+b", delete_on_close=False
                )
                file.write(dat_file_sampel)
                file.seek(0)
                file.close()
                prep_lt.read_dat([file.name])
                os_remove(file.name)
                return prep_lt.base_data
    return _create_var_data

def test_basic_fct(user_inputs,kuka_var_data):
    lt = Longtext()
    lt.set_lt_settings(user_inputs(10))
    lt.base_data = kuka_var_data(10)
    lt.scan_data()

    assert len(lt.longtext) == 52
    assert lt.longtext['$IN[1]'] == ['test_input_1']
    assert lt.longtext['$IN[9]'] == ['test_group_input_1 2**0']
    assert lt.longtext['$ANIN[1]'] == ['test_anin_1']
    assert lt.longtext['$OUT[1]'] == ['test_output_1']
    assert lt.longtext['$OUT[17]'] == ['test_group_output_2 2**0']
    assert lt.longtext['$ANOUT[2]'] == ['test_anout_2']

def test_without_prefix(user_inputs,kuka_var_data):  
    lt = Longtext()
    lt.set_lt_settings(user_inputs(11))
    lt.base_data = kuka_var_data(10)
    lt.scan_data()
    assert not lt.longtext
    assert len(lt.longtext) == 0
    
    lt = Longtext()
    lt.set_lt_settings(user_inputs(13))
    lt.base_data = kuka_var_data(10)
    lt.scan_data()
    assert len(lt.longtext) == 16
    for i in [1,2,3,4,5,6,7,8]:
        assert f'$IN[{i}]' in lt.longtext
        assert f'$OUT[{i}]' in lt.longtext
    
    lt = Longtext()
    lt.set_lt_settings(user_inputs(14))
    lt.base_data = kuka_var_data(10)
    lt.scan_data()

    assert len(lt.longtext) == 4
    for i in [1,2]:
        assert f'$ANIN[{i}]' in lt.longtext
        assert f'$ANOUT[{i}]' in lt.longtext
    
    lt = Longtext()
    lt.set_lt_settings(user_inputs(15))
    lt.base_data = kuka_var_data(10)
    lt.scan_data()
    assert len(lt.longtext) == 32
    for i in [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]:
        assert f'$IN[{i}]' in lt.longtext
        assert f'$OUT[{i}]' in lt.longtext

def test_with_prefix(user_inputs,kuka_var_data):
    lt = Longtext()
    lt.set_lt_settings(user_inputs(20))
    lt.base_data = kuka_var_data(20)
    lt.scan_data()
    assert len(lt.longtext) == 12
    for i in [1,2,3,4,5,6]:
        assert f'$IN[{i}]' in lt.longtext
        assert f'$OUT[{i}]' in lt.longtext
    
    lt = Longtext()
    lt.set_lt_settings(user_inputs(21))
    lt.base_data = kuka_var_data(20)
    lt.scan_data()
    assert len(lt.longtext) == 4
    for i in [1,2]:
        assert f'$ANIN[{i}]' in lt.longtext
        assert f'$ANOUT[{i}]' in lt.longtext
    
    lt = Longtext()
    lt.set_lt_settings(user_inputs(22))
    lt.base_data = kuka_var_data(20)
    lt.scan_data()
    #for key in lt.longtext:
    #    print(f'{key}:{lt.longtext[key]}')
    assert len(lt.longtext) == 4*2
    
    for i in [9,10,11,12]:
        assert f'$IN[{i}]' in lt.longtext
        assert f'$OUT[{i}]' in lt.longtext

def test_with_comments(user_inputs,kuka_var_data):
    lt = Longtext()
    lt.set_lt_settings(user_inputs(20))
    lt.base_data = kuka_var_data(20)
    lt.scan_data(True)
    assert len(lt.longtext) == 14
    for i in [1,2,3,4,5,6,8]:
        assert f'$IN[{i}]' in lt.longtext
        assert f'$OUT[{i}]' in lt.longtext
    
    lt = Longtext()
    lt.set_lt_settings(user_inputs(21))
    lt.base_data = kuka_var_data(20)
    lt.scan_data(True)
    assert len(lt.longtext) == 6
    for i in [1,2,4]:
        assert f'$ANIN[{i}]' in lt.longtext
        assert f'$ANOUT[{i}]' in lt.longtext
    
    lt = Longtext()
    lt.set_lt_settings(user_inputs(22))
    lt.base_data = kuka_var_data(20)
    lt.scan_data(True)
    assert len(lt.longtext) == 6*2
    for i in [9,10,11,12,15,16]:
        assert f'$IN[{i}]' in lt.longtext
        assert f'$OUT[{i}]' in lt.longtext
        
def test_wrong_decl(user_inputs,kuka_var_data):
    lt = Longtext()
    lt.set_lt_settings(user_inputs(30))
    lt.base_data = kuka_var_data(30)
    lt.scan_data(True)
    assert len(lt.longtext) == 8
    for i in [1,9,10]:
        assert f'$IN[{i}]' in lt.longtext
        assert f'$OUT[{i}]' in lt.longtext