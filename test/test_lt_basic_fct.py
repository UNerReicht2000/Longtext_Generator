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
    def created_user_inputs(test_case):
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
                    Marking(aktiv=True, name="Analog Output", var_prefix=(" s")),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=(" s")),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=(" s")),
                ]
            case 5:
                return [
                    Marking(aktiv=True, name="Digital Input", var_prefix=("ö")),
                    Marking(aktiv=True, name="Digital Output", var_prefix=()),
                    Marking(aktiv=True, name="Analog Input", var_prefix=()),
                    Marking(aktiv=True, name="Analog Output", var_prefix=()),
                    Marking(aktiv=True, name="Grouped Input", var_prefix=()),
                    Marking(aktiv=True, name="Grouped Output", var_prefix=()),
                ]
            
    return created_user_inputs

def test_impot_prefix(user_inputs):
    lt = Longtext()
    lt.impot_settings(user_inputs(1))
    for i in range(len(lt.var_markings)):
        assert len(lt.var_markings[i].var_prefix) == 2
        assert lt.var_markings[i].aktiv is True
        assert lt.var_markings[i].name == user_inputs(1)[i].name

    lt.impot_settings(user_inputs(2))
    for i in range(len(lt.var_markings)):
        assert len(lt.var_markings[i].var_prefix) == 0
        assert lt.var_markings[i].aktiv is True
        assert lt.var_markings[i].name == user_inputs(2)[i].name

    for test_item in ["not a list", 123, True, 3.136, ["not a list"]]:
        with pytest.raises(TypeError):
            lt.impot_settings(test_item)
    with pytest.raises(ValueError):
        lt.impot_settings(user_inputs(3))
        lt.impot_settings(user_inputs(4))

def test_set_prefixes_settings(user_inputs):
    lt = Longtext()
    lt.set_prefixes_settings({
        "Digital Input": ("di", "Di"),
        "Digital Output": ("do", "Do"),
        "Analog Input": ("ai", "Ai"),
        "Analog Output": ("ao", "Ao"),
        "Grouped Input": ("gi", "Gi"),
        "Grouped Output": ("go", "Go"),
    })
    for i in range(len(lt.var_markings)):
        assert len(lt.var_markings[i].var_prefix) == 2

    for test_item in ["not a dict", 123, True, 3.136, {"not a dict":123}]:
        with pytest.raises(TypeError):
            lt.set_prefixes_settings(test_item)

@pytest.fixture()
def dat_files():
    dat_file_sampel = b";Test file template for KUKA Longtext"
    files = []

    for i in range(2):
        files += [NamedTemporaryFile(prefix ='dat_file_', suffix='.dat', mode='w+b',delete_on_close=False)]
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
