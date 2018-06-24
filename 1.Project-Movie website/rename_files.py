import os

def rename_files():
    file_list = os.listdir(r"C:\test")
    print(file_list)
    
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)

    # change working directory
    os.chdir(r"C:\test")

    for file_name in file_list:
        print file_name
        os.rename(file_name, file_name.translate(None, "0123456789"))

    # ex: we try to rename a file that does not exist, eg. aa.txt
    # method 1
    if os.path.exists("aa.txt") == True:
        os.raname("aa.txt", "bb.txt")
    else:
        print "src file name not exist"

    # method 2
    try:
        os.rename("aa.txt", "bb.txt")
    except OSError:
        print "src file name not exist"

    # ex: we try to rename a file that already exists in the folder
    try:
        os.rename("cc.txt", "bb.txt")
    except OSError:
        print "file name already exists!"

    # return saved working path
    os.chdir(saved_path)

rename_files()

