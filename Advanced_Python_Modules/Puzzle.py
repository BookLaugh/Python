import os
import re

result = []

def search(file,pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()

    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return None

for folders,sub_folders,files in os.walk(os.getcwd()+'\\Assesment\\extracted_content'):
    for f in files:
        full_path = folders + '\\' +f
        result.append(search(full_path))
for r in result:
    if r is not None:
        print(r.group())
