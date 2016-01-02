#!/usr/bin/env python3
'''
\section{manual\_at\_structure.py}

\\hyperlink{content}{Содержание}

В данной программе используются следующие модули:



Программа предназначена для построения конфигураций межузельных атомов на основе исходной 
идеальной структуры.



На вход подается файл manual\_at\_structure.in

Данная программа может быть как импортируемой, так и исполняемой

\\newpage
'''
if __name__ == '__main__':

    from read_write_i import ReadWrite as RW
    import copy
    # Функция, создающая файл в rv_at формате с дефектом на основе идеальной решетки
    def w_def_rv_at(num_vac_list, num_int_list, int_mass_at, rv_at_dict, name_rv_at_def):
        d_def = copy.deepcopy(rv_at_dict)
        d_def_visual = copy.deepcopy(rv_at_dict)
        list_at_vac = []
        list_at_int = []
        d_def['i_sort_at'] = [2 for a in d_def['i_sort_at']]
        for i in num_int_list:
            if num_int_list == []: break
            list_at_int.append(d_def['r_at'][i-1])
            d_def['mass_at'][i-1] = int_mass_at
            d_def['i_sort_at'][i-1] = 1 
            
        count = 0
        for i in num_vac_list:
            if num_vac_list == []: break
            j = i - count
            list_at_vac.append(d_def['r_at'][j-1])
            d_def['r_at'].remove(d_def['r_at'][j-1])
            d_def['n_at'] -= 1
            d_def['v_at'].remove(d_def['v_at'][j-1])
            d_def['mass_at'].remove(d_def['mass_at'][j-1])
            d_def['num_at_r'].remove(d_def['num_at_r'][-1])
            d_def['mark_green'].remove(d_def['mark_green'][-1])
            d_def['mark_at'].remove(d_def['mark_at'][j-1])
            d_def['i_sort_at'].remove(d_def['i_sort_at'][-1])
            count += 1
        a2 = RW()
        a2.w_rv_at(name_rv_at_def, d_def)
        w_def_rv_at.list_at = d_def['r_at']
        w_def_rv_at.list_at_vac = list_at_vac
        w_def_rv_at.list_at_int = list_at_int

    # Функция, преобразующая список атомов в xyz формат
    def xyz_format(list_at, list_at_vac, list_at_int, name_xyz):
        f2 = open(name_xyz, 'w')
        f2.write(str(len(list_at)+len(list_at_vac))+'\n')
        f2.write('# Crystal lattice\n') 
        for i in list_at:
            if i in list_at_int: continue
            f2.write('Ba '+str(i[0])+' '+str(i[1])+' '+str(i[2])+'\n')
        for i in list_at_vac:
            if list_at_vac == []: break
            f2.write('N '+str(i[0])+' '+str(i[1])+' '+str(i[2])+'\n')
        for i in list_at_int:
            if list_at_int == []: break
            f2.write('Se '+str(i[0])+' '+str(i[1])+' '+str(i[2])+'\n')
        f2.close() 

    # Считывание входного файла
    f = open('manual_at_structure.in')
    number_vacancy_list = []
    number_interstitial_list = []
    for line in f:
        if line[0]=='#' or len(line)==0 or len(line)==1: continue
        line1 = line.split()
        if 'number_vacancy_list' in line1: number_vacancy_list = [int(i) for i in line1[1:]]
        elif 'number_interstitial_list' in line1: number_interstitial_list = [int(i) for i in line1[1:]]
        elif 'file_lattice_at' in line1: file_lattice_at = line1[1]
        elif 'interstitial_mass_at' in line1: interstitial_mass_at = float(line1[1])
        elif 'name_final_structure' in line1: name_final_structure = line1[1]

    # Считывание идеальной решетки в словарь d
    a1 = RW()
    a1.r_rv_at(file_lattice_at)
    d = a1.r_rv_at_dict

    # Построение ячейки с нужным количеством вакансий в заданных
    # позициях и её визуализация в *.xyz формате
    w_def_rv_at(number_vacancy_list, number_interstitial_list, interstitial_mass_at, d, name_final_structure+'.at')
    xyz_format(w_def_rv_at.list_at, w_def_rv_at.list_at_vac, w_def_rv_at.list_at_int, name_final_structure+'.xyz')









