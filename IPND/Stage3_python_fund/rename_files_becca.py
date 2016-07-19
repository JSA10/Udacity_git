import os

#create function 
def rename_files():
    # get file names from folder
    file_list = os.listdir("/Users/jeromeahye/Documents/DataScience/Udacity/Python/becca")
    print(file_list)

    # change working directory so rename function can find them
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir("/Users/jeromeahye/Documents/DataScience/Udacity/Python/becca")
    
    # rename files using for loop 
    for file_name in file_list:
            print("Old Name - "+file_name)
            print("New Name - "+file_name.translate(None, "0123456789"))
            os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)  # change working directory back to original

# run program
rename_files()
