import os
import shutil

from_dir = r"C:\Vanya Raina\Python Classes\C-112\from"
to_dir = r"C:\Vanya Raina\Python Classes\C-112\to"

list_of_files = os.listdir(from_dir)

for i in list_of_files:
    name,extension = os.path.splitext(i)
    if extension == " ":
        continue
    if extension in [".png", ".jpeg", ".jpg", ".pptx",".pdf", ".wav", ".dotx"]:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "newfiles"
        path3 = to_dir + "/" + "newfiles" + "/" + i

        if os.path.exists(path2):
            print("moving: ", i)
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("creating: ", i)
            print("moving: ", i)
            shutil.move(path1,path3)
