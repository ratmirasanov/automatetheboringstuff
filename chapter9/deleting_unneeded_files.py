import os


for foldername, subfolders, filenames in os.walk("./chapter9"):

    for filename in filenames:

        if os.path.getsize(os.path.join(foldername, filename)) > 1000000:

            print("File name is %s." % filename)
            print("File size is %s bytes." % os.path.getsize(os.path.join(foldername, filename)))
            print("Absolute path is %s." % os.path.abspath(os.path.join(foldername, filename)))
            print("-------")
