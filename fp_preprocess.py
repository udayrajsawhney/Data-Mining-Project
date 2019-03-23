
from __future__ import print_function

import csv
from collections import Counter
file_name = 'Iris.csv'
csv_file = list(csv.reader(open(file_name)))
info_dict = {}
indexs = []
for i,row in enumerate(csv_file):
    if i>0: 
        for j, col in enumerate(row[1:-1]):
            if info_dict[indexs[j]]['max'] < float(col):
                info_dict[indexs[j]]['max'] = float(col)
            if info_dict[indexs[j]]['min'] > float(col):
                info_dict[indexs[j]]['min'] = float(col)
            info_dict[indexs[j]][row[-1].strip()].update([col])
    else:
        indexs = row[1:-1]
        for col in row[1:-1]:
            info_dict[col]= {
                'max' : -1,
                'min' : 10,
                'Iris-setosa' : Counter(),
                'Iris-virginica' : Counter(),
                'Iris-versicolor' : Counter(),
            }    
for key in info_dict:
    print(key)
    for k2 in info_dict[key]:
        if k2[0] != 'I':
            print('\t', k2, info_dict[key][k2])
        else:
            print('\t', k2)
            for k3 in sorted(info_dict[key][k2], key=lambda v: float(v)):
                print('\t\t', k3, info_dict[key][k2][k3])
    print()

split_dict = {}
for key in info_dict:
    if key not in split_dict:
        split_dict[key] = []

    _max = info_dict[key]['max']
    _min = info_dict[key]['min']
    gap = (_max - _min)/3
    split_dict[key] += [round(_min + gap,2), round(_min + 2*gap,2)]

print(split_dict)

new_file = open('new_Iris.csv', 'w')
csv_writer = csv.writer(new_file)
indexs = list(split_dict.keys())
for i,row in enumerate(csv_file):
    if i == 0:
        csv_writer.writerow([str(split_dict)])
        """ new_r = []
        new_r.append(row[0])
        for x in row[1:-1]:
            new_r.append(x+'_1')
            new_r.append(x+'_2')
            new_r.append(x+'_3')
        new_r.append('class')
        csv_writer.writerow(new_r) """
    else:
        new_r = []
        #new_r.append(row[0])
        if float(row[1]) < split_dict[indexs[0]][0]:
            new_r += ['SL_1']
        elif float(row[1]) >= split_dict[indexs[0]][0] and float(row[1]) < split_dict[indexs[0]][1]:
            new_r += ['SL_2']
        else:
            new_r += ['SL_3']

        if float(row[2]) < split_dict[indexs[1]][0]:
            new_r += ['SW_1']
        elif float(row[2]) >= split_dict[indexs[1]][0] and float(row[2]) < split_dict[indexs[1]][1]:
            new_r += ['SW_2']
        else:
            new_r += ['SW_3']
        
        if float(row[3]) < split_dict[indexs[2]][0]:
            new_r += ['PL_1']
        elif float(row[3]) >= split_dict[indexs[2]][0] and float(row[3]) < split_dict[indexs[2]][1]:
            new_r += ['PL_2']
        else:
            new_r += ['PL_3']
        
        if float(row[4]) < split_dict[indexs[3]][0]:
            new_r += ['PW_1']
        elif float(row[4]) >= split_dict[indexs[3]][0] and float(row[4]) < split_dict[indexs[3]][1]:
            new_r += ['PW_2']
        else:
            new_r += ['PW_3']

        new_r += [row[-1]]
        csv_writer.writerow(new_r)

new_file.close()