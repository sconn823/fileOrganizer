from os import walk
import shutil

#shutil.move('C:/Users/Sean/Documents/Code/Python/FileOrganizer/TestFolder/test.jpg', 
#            'C:/Users/Sean/Documents/Code/Python/FileOrganizer/TestFolder/newName.jpg')

files = []
for (dirpath, dirnames, filenames) in walk("C:/Users/Sean/Documents/Code/Python/FileOrganizer/TestFolder"):
    for name in filenames:
        files.append(dirpath + '/' + name)

print(files)
#https://stackoverflow.com/questions/12572362/how-to-get-a-string-after-a-specific-substring
#https://jaxenter.com/implement-switch-case-statement-python-138315.html