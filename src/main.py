# -*- coding: utf-8 -*-

from dev_func import debug_print

from user_ui.main_ui import MainWindowLtG

def __init__() -> None:
    debug_print('init')
    pass


if __name__ == '__main__':
    test_mode = False
    if test_mode:
        debug_print('Start')
        userinterface = MainWindowLtG()
    else:
        debug_print('test_mode aktiv')
        pass