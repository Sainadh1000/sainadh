with open("file ops/example.txt", "r") as file:
    # print(file.read())
    first_line=file.readline()
    print(first_line)
    rest_of_lines=file.readlines()
    print(rest_of_lines)
    
    for i in first_line:
        print(i)


with open("file ops/newfile.txt","w") as file:
    file.write(first_line)
