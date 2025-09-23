def averagescore(*score):
    total=sum(score)/len(score)
    return total
sachin=averagescore(100,70,80,90)
virat=averagescore(50,60,78)
msdhoni=averagescore(90,66,120,67,43,20)
print(sachin)
print(virat)
print(msdhoni)

def empdata(**data):
    if len(data)==0:
        print("no data provided")
    else:
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
empdata(name='teja',age=25,department='Developer')