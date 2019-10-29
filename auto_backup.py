import os
import csv
import shutil
from datetime import datetime

os.chdir('/home/imharjyotbagga/Documents/Source')
#print(os.getcwd())
#print(os.listdir())
filename="source_loc.csv"

with open(filename, 'r') as csv_file:
    source_locs=[]
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        source_locs.append(row[0])
#print (source_locs)

os.chdir('..')
os.chdir('Backup')
now =datetime.now()
name=now.strftime("%Y-%m-%d %H:%M:%S")
os.mkdir(name)
dest_loc=os.getcwd()
dest_loc=dest_loc + '/' + name
#print(dest_loc)

#os.chdir('..')
#os.chdir('Source')
#source_loc=os.getcwd()
#print (source_loc)        
for source_loc in source_locs:
    os.chdir(source_loc)
    #print(os.getcwd())
    for file in os.listdir(source_loc):
        #print (file)
        if os.path.isdir(file):
            dest_loc1=dest_loc+'/'+file
            shutil.copytree(file,dest_loc1)
        else:
            shutil.copy(file,dest_loc)
print ("Backup Done!!")