import zipfile
import shutil

f = open('Text.txt',"w")
f.write('Hey My name is Ulan')
f.close()

f = open('Text2.txt','w')
f.write('Hey My name is Ulan2')
f.close()
# ------------------------------ ZIPFILE -----------------------------

comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('Text.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('Text2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_file')

# -------------------------------- SHUTIL ---------------------------------------------

to_zip = 'C:\\Users\\ULAN\\Desktop\\Python2\\extracted_file'
output_file = 'New_file'
shutil.make_archive(output_file,'zip',to_zip)
shutil.unpack_archive('new_file.zip','Final_file','zip')
