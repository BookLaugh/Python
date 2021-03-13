# importing modules 

import os
import shutil
import send2trash  # Make sure pip install send2trash

os.getcwd() # Current directory

os.listdir() # By deafault gives list of files & folders in your current directory

shutil.move(source,destination) # moves file to the given destination

os.unlink(path) # deletes FILE at the path you give

os.rmdir(path) # deletes FOLDER at the path you give (Folder MUST be EMPTY)

shutil.rmtree(path) # this func is dangerous to use.Once u delete all files & folders  at the given path.It WON'T be possible to recover all of them.


os.listdir('C:\Users\ULAN\Desktop')

send2trash.send2trash('BST.text')
print(os.listdir("C:/Users/ULAN/Desktop")) # we have deleted our file BST.text 

# Walk through a dir

os.listdir("C:/Users/ULAN/Desktop") # current dir

for folders,sub_folder,files in os.walk("C:/Users/ULAN/Desktop"): # Looking for all files & Folder in Desktop. Let' see it ! ALL RIGHT !
  print(f"Currently looking at Folder: {folders}")
  print('\n')
  print("The Subfolders are: ")
  for sub_fold in sub_folder:
    print("\t Subfolder:" + sub_fold)
    
  print('\n')
  
  print("The Files are: ")
  for file in files:
    print("\t Flies:" + file)
   print('\n')
  
  
 
  os.listdir("C:/Users/ULAN/Desktop")
  
for folders, sub_folder, files in os.walk("C:/Users/ULAN/Desktop/Test"): # Walking through my Test Folder
    print(f"Currently looking at Folder: {folders}")
    print('\n')
    print("The Subfolders are: ")
    for sub_fold in sub_folder:
        print("\t Subfolder:" + sub_fold)

    print('\n')

    print("The Files are: ")
    for file in files:
        print("\t Flies:" + file)
    print('\n')

  
  # --- OUTPUT LOOK LIKE THIS BELOW
  """
  C:\Users\ULAN\AppData\Local\Programs\Python\Python39\python.exe C:/Users/ULAN/Desktop/Python2/main3.py
  
Currently looking at Folder: C:/Users/ULAN/Desktop/Test


The Subfolders are: 
	 Subfolder:1
	 Subfolder:2


The Files are: 
	 Flies:BSt.txt


Currently looking at Folder: C:/Users/ULAN/Desktop/Test\1


The Subfolders are: 


The Files are: 
	 Flies:binary_search.py
	 Flies:linked_list.py


Currently looking at Folder: C:/Users/ULAN/Desktop/Test\2


The Subfolders are: 


The Files are: 



Process finished with exit code 0

  
  """
