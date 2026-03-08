f = open("file ops/example.txt", "w+")

f.write("Hello Python")

f.seek(0)   
data = f.read()

print(data)

f.close()