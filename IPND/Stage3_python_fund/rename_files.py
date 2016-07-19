import os
def rename_files():
    # 1 get file names from a folder
    file_list = os.listdir("/Users/jeromeahye/Documents/DataScience/Udacity/Python/prank")
    #print(file_list)
    # 2 for each file, rename filena
    # need a loop as 50 files
    # still don't know how to remove numbers from filenames, so use Python shell window to test
    # need to change working directoy to specify location for Python to look for loop below
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir("/Users/jeromeahye/Documents/DataScience/Udacity/Python/prank")
    for file_name in file_list:
            print("Old Name - "+file_name)
            print("New Name - "+file_name.translate(None, "0123456789"))
            os.rename(file_name, file_name.translate(None, "0123456789"))
    # string.translate function takes two arguments a table of values (we don't have and the characters to remove from a set of strings)
    os.chdir(saved_path)    
rename_files()
#final recommendation was to add print statements everytie a file name changed

