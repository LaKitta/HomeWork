import os
from fnmatch import fnmatch, fnmatchcase
import shutil

# delete (file || empty folder || folder) doesn't match *.trf 
def delete_nottrf(dir):
    a = [] # array of folders under 02_testreports
    for i in os.listdir(dir):
        if not fnmatch(i, '*xlsx'):
            a.append(i)
    # print(a)

    c =[] # array of folders has .trf inside under 02_testreports

    for i in a:
        path = os.path.join(dir, i)    
        # print(path)

        for i2 in os.listdir(path):
            if fnmatch(i2, '*.trf'):
                c.append(i)

    # print(c)

    for i in c:
        path = os.path.join(dir, i)
        for i2 in os.listdir(path):
            # delete (file || empty folder || folder) doesn't match *.trf 
            if not fnmatch(i2, '*.trf'):            
                dir2 = os.path.join(dir, i)
                i3 = os.path.join(dir2, i2)
                print("Deleting %s ..." % (i3))
                try:
                    os.remove(i3)
                except OSError as e:
                    try:
                        os.rmdir(i3)
                    except OSError as ex:
                        shutil.rmtree(i3)

testreport = [] # arrary of all folder match *02_testreports

for dirpath, dirname, files in os.walk('.'): 
    if fnmatch(dirpath, '*02_TestReports'):
        print(f'Found directory: {dirpath}')
        testreport.append(dirpath)    

print(len(testreport))

# loop all 02_testreports folder to delete
for dir in testreport:
    delete_nottrf(dir)







