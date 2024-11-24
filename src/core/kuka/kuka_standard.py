# -*- coding: utf-8 -*-

from dev_func import debug_print
from dev_func import print_list

from os import path

from copy import deepcopy

from core.longtext_func import Creat_Error_String
from core.longtext_func import delete_comment
from core.longtext_func import delete_content
from core.longtext_func import add_in_longtext

CreatErrStr = Creat_Error_String()
#==================

def create_longtext(in_data,config,delet_marker,dat_typ,BufferInstanz):  
    BufferInstanz.append('created according to KUKA standard')

    longtext = []

    current_directory = path.dirname(__file__)
    file_path = path.join(current_directory, 'emtpy_longtext.csv')
    longtextdat = open(file_path, 'r')      
    longtext = longtextdat.read()
    longtext = longtext.split("\n")

    for index in range(len(in_data)):
        in_data[index] = in_data[index].replace("GLOBAL","")
        in_data[index] = in_data[index].replace("Global","")
        in_data[index] = in_data[index].replace("global","")
        in_data[index] = in_data[index].replace("SIGNAL","")
        in_data[index] = in_data[index].replace("Signal","")
        in_data[index] = in_data[index].replace("signal","")
        in_data[index] = in_data[index].replace("BOOL","")
        in_data[index] = in_data[index].replace("Bool","")
        in_data[index] = in_data[index].replace("bool","")
        in_data[index] = delete_comment(in_data[index],';')   
        in_data[index] = in_data[index].strip()
  
    for index in range(len(config)):
        if (config[index] == 10):
            debug_print('Import Timer')
            BufferInstanz.append('Timer==========')
            pass
        if (config[index] == 20):
            debug_print('Import Counter')
            BufferInstanz.append('Counter========')
            pass
        if (config[index] == 30):
            debug_print('Import Flag')
            BufferInstanz.append('Flag===========')
            pass
        if (config[index] == 40):
            debug_print('Import CYCFlag')
            BufferInstanz.append('CYCFlag========')
            BufferInstanz.append('Not available at the moment')
            pass
        if (config[index] == 50):
            debug_print('Import ANIN')
            BufferInstanz.append('ANIN===========')
            pass
        if (config[index] == -50):
            debug_print('Import ANOUT')
            BufferInstanz.append('ANOUT==========')
            pass
        if (config[index] == 100):
            debug_print('Import BI')
            BufferInstanz.append('BI=============')
            longtext = add_in_longtext(find_singel_objects(in_data,'BI',delet_marker,BufferInstanz),longtext,1439,'IN[',dat_typ)

        if (config[index] == -100):
            debug_print('Import BO')
            BufferInstanz.append('BO=============')
            longtext = add_in_longtext(find_singel_objects(in_data,'BO',delet_marker,BufferInstanz),longtext,5535,'OUT[',dat_typ)

        if (config[index] == 200):
            debug_print('Import GI')
            BufferInstanz.append('GI=============')
            longtext = add_in_longtext(find_group_objects(in_data,'GI',delet_marker,BufferInstanz),longtext,1439,'IN[',dat_typ)

        if (config[index] == -200):
            debug_print('Import GO')
            BufferInstanz.append('GO=============')
            longtext = add_in_longtext(find_group_objects(in_data,'GO',delet_marker,BufferInstanz),longtext,5535,'OUT[',dat_typ)

        if (config[index] == 300):
            debug_print('Import II')
            BufferInstanz.append('II=============')
            longtext = add_in_longtext(find_group_objects(in_data,'II',delet_marker,BufferInstanz),longtext,1439,'IN[',dat_typ)

        if (config[index] == -300):
            debug_print('Import IO')
            BufferInstanz.append('IO=============')
            longtext = add_in_longtext(find_group_objects(in_data,'IO',delet_marker,BufferInstanz),longtext,5535,'OUT[',dat_typ)

        if (config[index] == 400):
            debug_print('Import RI')
            BufferInstanz.append('RI=============')
            longtext = add_in_longtext(find_group_objects(in_data,'RI',delet_marker,BufferInstanz),longtext,1439,'IN[',dat_typ)

        if (config[index] == -400):
            debug_print('Import RO')
            BufferInstanz.append('RI=============')
            longtext = add_in_longtext(find_group_objects(in_data,'RO',delet_marker,BufferInstanz),longtext,5535,'OUT[',dat_typ)

        if (config[index] == 500):
            debug_print('Import CI')
            BufferInstanz.append('CI=============')
            longtext = add_in_longtext(find_group_objects(in_data,'CI',delet_marker,BufferInstanz),longtext,1439,'IN[',dat_typ)

        if (config[index] == -500):
            debug_print('Import CO')
            BufferInstanz.append('CO=============')
            longtext = add_in_longtext(find_group_objects(in_data,'CO',delet_marker,BufferInstanz),longtext,5535,'OUT[',dat_typ)
            
    longtextdat.close()
    
    return longtext

def find_singel_objects(in_data,scan,delet_marker,BufferInstanz):
    singel_objects = []
    located_objects = []

    found_something = False
    for index in range(len(in_data)):
        if(in_data[index].find(scan.upper()) == 0) or (in_data[index].find(scan.capitalize()) == 0) or (in_data[index].find(scan.lower()) == 0):
            located_objects.append(index)
            found_something = True
    if found_something:        
        #BI s in Separate liste 
        for index in located_objects :
            singel_objects.append(in_data[index])
       
        for index in range(len(singel_objects)): #Delete things you don t need
            singel_objects[index] = singel_objects[index].replace("IN[","")
            singel_objects[index] = singel_objects[index].replace("In[","") 
            singel_objects[index] = singel_objects[index].replace("in[","")
            singel_objects[index] = singel_objects[index].replace("OUT[","")
            singel_objects[index] = singel_objects[index].replace("Out[","") 
            singel_objects[index] = singel_objects[index].replace("out[","") 
            singel_objects[index] = singel_objects[index].replace("]","")
            singel_objects[index] = singel_objects[index].replace("TO","")
            singel_objects[index] = singel_objects[index].replace("To","")
            singel_objects[index] = singel_objects[index].replace("to","")
            singel_objects[index] = singel_objects[index].strip()
            singel_objects[index] = singel_objects[index].split("$")
            for sub_index in range(len(singel_objects[index])):
                pass
                # singel_objects[index][sub_index] = delete_content(singel_objects[index][sub_index],'')
                
        for index in range(len(singel_objects)):
            if (len(singel_objects[index]) == 2):
                singel_objects[index][0] = singel_objects[index][0].strip()
                singel_objects[index][1] = int(singel_objects[index][1].strip())
        
                if delet_marker:#delet BI or BO
                    singel_objects[index][0] = singel_objects[index][0].lstrip(scan.upper())
                    singel_objects[index][0] = singel_objects[index][0].lstrip(scan.capitalize())
                    singel_objects[index][0] = singel_objects[index][0].lstrip(scan.lower())
                singel_objects[index][0] = singel_objects[index][0].lstrip('_')    
            else:               
                BufferInstanz.append(CreatErrStr.wrong_length(singel_objects[index],1))
                singel_objects[index] = ''
        
        singel_objects = delete_content(singel_objects,'')

    return singel_objects

def find_group_objects(in_data,scan,delet_marker,BufferInstanz):
    group_objects = []
    located_objects = []
    tmp_list = []

    found_something = False
    for index in range(len(in_data)):
        if(in_data[index].find(scan.upper()) == 0) or (in_data[index].find(scan.capitalize()) == 0) or (in_data[index].find(scan.lower()) == 0):
            located_objects.append(index)
            found_something = True
        #II s in Separate liste
    if found_something: 
        for index in located_objects :
            group_objects.append(in_data[index])####
    
        for index in range(len(group_objects)):
            group_objects[index] = group_objects[index].replace("IN[","")
            group_objects[index] = group_objects[index].replace("In[","") 
            group_objects[index] = group_objects[index].replace("in[","")
            group_objects[index] = group_objects[index].replace("OUT[","")
            group_objects[index] = group_objects[index].replace("Out[","") 
            group_objects[index] = group_objects[index].replace("out[","")
            group_objects[index] = group_objects[index].replace("TO","")
            group_objects[index] = group_objects[index].replace("To","")
            group_objects[index] = group_objects[index].replace("to","")
            group_objects[index] = group_objects[index].replace("]","")
            group_objects[index] = group_objects[index].strip()
            group_objects[index] = group_objects[index].split("$")            
            for sub_index in range(len(group_objects[index])):
                pass
                # group_objects[index][sub_index] = delete_content(group_objects[index][sub_index],'')
        
        for index in range(len(group_objects)):
            if (len(group_objects[index]) ==3):
                group_objects[index][1] = group_objects[index][1].strip()
                group_objects[index][2] = group_objects[index][2].strip()
                if group_objects[index][1].isdecimal() and group_objects[index][2].isdecimal():
                    IStartBit = int(group_objects[index][1])
                    IEndBit   = int(group_objects[index][2])
                    ITmpBitNum = 0 
    
                    for sub_index in range(IStartBit,IEndBit+1): 
                        tmp_list.insert(sub_index,[group_objects[index][0]+' 2**'+str(ITmpBitNum)]+[str(IStartBit)])
                        IStartBit = IStartBit + 1
                        ITmpBitNum = ITmpBitNum + 1
                else:
                    BufferInstanz.append(CreatErrStr.no_decimal(group_objects[index]))
                    group_objects[index] = ''
                    pass
            else:
                TmpErrorString = CreatErrStr.wrong_length(group_objects[index],2)
                BufferInstanz.append(TmpErrorString)
                group_objects[index] = ''
                        
        group_objects.clear() 
        group_objects = deepcopy(tmp_list)
        if delet_marker:#delet BI or BO
            for index in range(len(group_objects)):
                group_objects[index][0] = group_objects[index][0].lstrip(scan.upper())
                group_objects[index][0] = group_objects[index][0].lstrip(scan.capitalize())
                group_objects[index][0] = group_objects[index][0].lstrip(scan.lower())   
            
        #ListOfGroupObjects[Itmp1][0] = ListOfGroupObjects[Itmp1][0].lstrip('_')
        group_objects = delete_content(group_objects,'')
   
    return group_objects