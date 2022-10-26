
import os
from os import listdir
from os.path import isfile, join

#handle taking LPARs and QMs names from table, puts those values in a dictionary
cpath = raw_input("Please enter customer name used for e drive path, for example, 'abcbank': ")

f= open("lpar_list/Distinct_LPAR_QMGR.txt", "r")
file_list = f.readlines()
formatted_fl = []
for x in file_list[2:]:
    formatted_fl.append(x.strip())
f.close()

while('' in formatted_fl):
    formatted_fl.remove('')

dict = {}
lpars = []
qmgrs = []
print(dict.items())
for x in formatted_fl:
    if x[0:4] not in lpars:
        dict[x[0:4]] = []

for key in dict:
    temp = key
    for x in formatted_fl:
        if temp == x[0:4]:
            dict[temp].append(x[5:])

parent_directory = os.getcwd()
filenames = [f for f in listdir(parent_directory) if isfile(join(parent_directory, f))]

for key, value in dict.items():
    lpar = key
    qmgrs = value
    
    #list all the generic files to be modified

    # #loop through each file in the directory, only pay attention to files with txt extensions
    for filename in filenames:
        if filename.endswith(".txt"):
            for qm in qmgrs:
            #Specify variables that need to be replaced in this dictionary
                replacements = {'++LPAR': lpar, '++QMGR': qm, '**CustomerPath**': cpath}
                # print(replacements)
                #create title with appropriate replacements
                title = replacements['++LPAR']+replacements['++QMGR']
                #print(title)
                #replace contents of generic text file with appropriate LPAR or QMGR, write replacements to a new file for each generic file in list
                for file in filenames:
                    with open(filename) as infile, open(title+filename[7:], 'w') as outfile:
                        for line in infile:
                            for src, target in replacements.items():                        
                                line = line.replace(src, target)
                            outfile.write(line)   

        else:
            continue


    #references: 
    # https://stackoverflow.com/questions/13089234/replacing-text-in-a-file-with-python/13089373
    # https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory