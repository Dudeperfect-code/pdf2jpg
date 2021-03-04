import os
from pdf2image import convert_from_path
 
print(f"Current Dir: {os.getcwd()}")

fname = input("Enter image Folder Path, to--: ")    
if os.path.exists(fname):
    print("Already Exist")
else:
    os.mkdir(fname)
    
pdf_dir_name = input("Enter PDF Folder Path, From--: ")
os.chdir(pdf_dir_name)       #Move to pdf folder folder.

for item in os.listdir():
    path = os.path.join(os.getcwd(),item)   #a pdf file complete path   
    image = convert_from_path(path)
    for i in range(len(image)):
        os.chdir(fname)         #move to image folder
        image[i].save(item.replace(".pdf","") +"_"+ str(int(i+1)) +".jpg","JPEG")
    os.chdir(pdf_dir_name)      #move back to pdf folder
    
print("Successfully Converted!")