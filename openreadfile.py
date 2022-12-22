import os
print(os.path.abspath(__file__))
print(os.getcwd())
print(os.listdir())
print(os.listdir('D:\\IT'))

f=open('D:\\IT\\testtextfile.txt','w+')
f.write('This is test only')
f.close()

# os.unlink(path) - Delete a file
# os.rmdir(path) - Delete a folder
# shutil.rmtree(path) - Remove all file and folder - most dangerous

import shutil
shutil.move('D:\\IT\\testtextfile.txt','D:\\IT\\python')

os.unlink('D:\\IT\\python\\testtextfile.txt')

#Safer way to delete file
#import send2trash
#send2trash.send2trash('D:\\IT\\python\\testtextfile.txt')



for folder, sub_folders,files in os.walk('D:\\Home\\'):

    print(f'Currently looking at {folder}')
    print('\n')

    print('The subfloders are:')
    for sub_fold in sub_folders:
        print(f'\t Sunfolder: {sub_fold}')

    print('\n')
    print('the filers are:')
    for f in files:
        print(f'\t file:{f}')
    print('\n')

