# -*- coding: utf-8 -*-

import pytest
from os import remove as os_remove
from tempfile import TemporaryFile
from src.core.kuka import Longtext
from src.core.kuka import Marking

def test_init():
    lt = Longtext()
    assert lt.base_data == {}
    assert lt.log == []
    assert lt.log_name == ''
    assert lt.log == []

@pytest.mark.parametrize("expanded", [True, False, None, "string", 123])
def test_create_template(expanded):
    lt = Longtext()

    if expanded is True:
        lt.create_template(expanded)
        assert len(lt.longtext) == 17823
    elif expanded is False:
        lt.create_template(expanded)
        assert len(lt.longtext) == 9631
    elif isinstance(expanded, (str, int)):
        with pytest.raises(TypeError):
            lt.create_template(expanded)
    else:# expanded is None:
        lt.create_template()
        assert len(lt.longtext) == 9631

@pytest.fixture(scope="module")
def user_inputs():
    def _created_user_inputs(test_case):
        match test_case:
            case 1:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=("di", "Di")),
                    Marking(aktiv=True, name="Digital Output", var_prefix=("di", "Di")),
                    Marking(aktiv=True, name="Analog Input", var_prefix=("di", "Di")),
                    Marking(aktiv=True, name="Analog Output", var_prefix=("di", "Di")),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=("di", "Di")),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=("go", "Go")),
                ]
            case 2:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=()),
                    Marking(aktiv=True, name="Digital Output", var_prefix=()),
                    Marking(aktiv=True, name="Analog Input", var_prefix=()),
                    Marking(aktiv=True, name="Analog Output", var_prefix=()),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=()),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=()),
                ]
            case 3:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=("         ")),
                    Marking(aktiv=True, name="Digital Output", var_prefix=("      ")),
                    Marking(aktiv=True, name="Analog Input", var_prefix=("   ")),
                    Marking(aktiv=True, name="Analog Output", var_prefix=(" ")),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=(" ")),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=(" ")),
                ]
            case 4:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=("     s")),
                    Marking(aktiv=True, name="Digital Output", var_prefix=("    s")),
                    Marking(aktiv=True, name="Analog Input", var_prefix=("      s")),
                    Marking(aktiv=True, name="Analog Output", var_prefix=(" ")),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=(" ")),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=(" ")),
                ]
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
                    Marking(aktiv=True, name="Digital Input", var_prefix=(" ")),
                    Marking(aktiv=True, name="Digital Output", var_prefix=(" ")),
                    Marking(aktiv=True, name="Analog Input", var_prefix=(" ")),
                    Marking(aktiv=True, name="Analog Output", var_prefix=(" ")),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=(" ")),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=(" ")),
                ]
    return _created_user_inputs

def test_impot_prefix(user_inputs):
    lt = Longtext()
    lt.impot_prefix(user_inputs(1))
    for i in range(len(lt.var_markings)):
        assert len(lt.var_markings[i].var_prefix) == 2
        assert lt.var_markings[i].aktiv is True
        assert lt.var_markings[i].name == user_inputs(1)[i].name

    lt.impot_prefix(user_inputs(2))
    for i in range(len(lt.var_markings)):
        assert len(lt.var_markings[i].var_prefix) == 0
        assert lt.var_markings[i].aktiv is True
        assert lt.var_markings[i].name == user_inputs(2)[i].name

    for test_item in ["not a list", 123, True, 3.136, ["not a list"]]:
        with pytest.raises(TypeError):
            lt.impot_prefix(test_item)
    with pytest.raises(ValueError):
        lt.impot_prefix(user_inputs(3))
    with pytest.raises(ValueError):
        lt.impot_prefix(user_inputs(4))


@pytest.fixture()
def dat_files():
    dat_file_sampel = b"""
    ;Test file template for KUKA Longtext
    GLOBAL SIGNAL test_input_1 = $IN[1]
    GLOBAL SIGNAL test_input_2=$IN[2]
    GLOBAL SIGNAL test_input_3 = $IN[3]
    GLOBAL SIGNAL test_input_4 = $IN[4]
    GLOBAL SIGNAL test_input_5 = $IN[5]
    GLOBAL SIGNAL test_input_6 = $IN[6]
    GLOBAL SIGNAL test_input_7 = $IN[7]
    GLOBAL SIGNAL test_input_8 = $IN[8]
    GLOBAL SIGNAL test_group_input_1 = $IN[9] TO $IN[16]
    GLOBAL SIGNAL test_group_input_2=$IN[17] TO $IN[24]

    GLOBAL SIGNAL test_anin_1 = $ANIN[1]
    GLOBAL SIGNAL test_anin_2=$ANIN[2]

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
    files = []
    
    for i in range(2):
        files += [TemporaryFile(prefix ='dat_file_', suffix='.dat', mode='w+b',delete_on_close=False)]
        files[i].write(dat_file_sampel)
        files[i].seek(0)

    files_names = []

    for file in files:
        files_names += [file.name]

    for file in files:
        file.close()

    yield files_names

    for file in files:
        os_remove(file.name)

def test_read_dat(dat_files):

    lt = Longtext()
    lt.read_dat(dat_files)
    assert len(lt.base_data) == 2

    dat_files.pop(1)
    lt = Longtext()
    lt.read_dat(dat_files)
    assert len(lt.base_data) == 1

    with pytest.raises(TypeError):lt.read_dat()

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
                    GLOBAL SIGNAL test_input_4 = $In[4]
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
                file = TemporaryFile(
                    prefix="dat_file_", suffix=".dat", mode="w+b", delete_on_close=False
                )
                file.write(dat_file_sampel)
                file.seek(0)
                file.close()
                prep_lt.read_dat(file.name)
                os_remove(file.name)
                return prep_lt.base_data
            case 20:
                prep_lt = Longtext()
                dat_file_sampel = b"""
                    ;Test file template for KUKA Longtext
                    GLOBAL SIGNAL test_input_1 = $IN[1]
                    GLOBAL SIGNAL test_input_2=$IN[2]
                    GLOBAL SIGNAL test_input_3 = $IN[3]
                    GLOBAL SIGNAL test_input_4 = $IN[4]
                    GLOBAL SIGNAL test_input_5 = $IN[5]
                    GLOBAL SIGNAL test_input_6 = $IN[6]
                    GLOBAL SIGNAL test_input_7 = $IN[7]
                    GLOBAL SIGNAL test_input_8 = $IN[8]
                    GLOBAL SIGNAL test_group_input_1 = $IN[9] TO $IN[16]
                    GLOBAL SIGNAL test_group_input_2=$IN[17] TO $IN[24]

                    GLOBAL SIGNAL test_anin_1 = $ANIN[1]
                    GLOBAL SIGNAL test_anin_2=$ANIN[2]

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
                file = TemporaryFile(
                    prefix="dat_file_", suffix=".dat", mode="w+b", delete_on_close=False
                )
                file.write(dat_file_sampel)
                file.seek(0)
                file.close()
                prep_lt.read_dat(file.name)
                os_remove(file.name)
                return prep_lt.base_data
    return _create_var_data

def test_scan_dat(kuka_var_data):
    lt = Longtext()
    lt.impot_prefix(user_inputs(10))
    lt.base_data = kuka_var_data(10)
    lt.scan_data()
    assert len(lt.longtext) == 52
    assert lt.longtext['$IN[8]'] == ['test_input_8']

    lt = Longtext()
    lt.impot_prefix(user_inputs(11))
    lt.base_data = kuka_var_data(10)
    lt.scan_data()
    assert len(lt.longtext) == 0
