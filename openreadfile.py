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




