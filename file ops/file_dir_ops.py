# Create File
with open("file ops/new.txt","w") as file_data:
    print(file_data)
    
import os
os.remove("file ops/new.txt")

current_working_directory=os.getcwd()
print(current_working_directory)

os.mkdir("file ops/newfolder")
os.rmdir("file ops/newfolder")

