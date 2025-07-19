# -*- coding: utf-8 -*-

from dev_func import debug_print

from core.kuka import Longtext

from user_ui.main_ui import MainWindowLtG

def __init__() -> None:
    pass


if __name__ == '__main__':
    test_mode = True
    if test_mode:
        print('Start')
        userinterface = MainWindowLtG()
    else:
        print('test_mode aktiv')
        longtext_raw = Longtext()
        longtext = Longtext()
        longtext.create_template()

        list_of_fils = [r'C:\Users\dunger\Desktop\Vardat\VarStandardSig.dat',
                        r'C:\Users\dunger\Desktop\Vardat\VarUserSig.dat']
        #longtext_raw.read_dat(list_of_fils)
        longtext_raw.read_dat([r'C:\Users\dunger\Desktop\Vardat\VarUserSig.dat'])
        #test_longtext.impot_macker(Markings(singel = ('di','do'),multi = ('gi','go')))
        longtext_raw.scan_data()
        longtext.merge(longtext_raw)
        #print_dict(longtext())
        #longtext.export_txt('longtext_test',r'C:\Users\dunger\Desktop\Vardat\test')
        #print(longtext.log_name)
        longtext.export_csv('longtext_test',r'C:\Users\dunger\Desktop\Vardat\test')
        #print(longtext.log_name)  