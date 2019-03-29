import os
import shutil


for foldername, subfolders, filenames in os.walk("./chapter9"):

    for filename in filenames:

        if filename.endswith(".pdf") or filename.endswith(".jpg"):

            print("File name %s..." % filename)
            shutil.copy(os.path.join(foldername, filename), "./chapter9/new_folder")
