def rectangle_area(length,width):
    area=length*width
    print(area)
rectangle_area(12,4)

#default parameters
def cost(price,dicount,tax=0.05):
    totalprice=price-price*(dicount/100)+price*(tax/100)
    print(totalprice)
cost(1000,10)#tax default is applied since we have not given any value while calling function
cost(900,5,0.1)

#issue with default argiuments
#def cost(price,dicount,tax=0.05,servicetax):
#   totalprice=price-price*(dicount/100)+price*(tax/100)-price*(servicetax/100)
#   print(totalprice)
#cost(1000,5,0.1) 
#since default should be last elment or after default all parameter should be default

def newcost(price,dicount,tax=0.05,servicetax=0.1):
    totalprice=price-price*(dicount/100)+price*(tax/100)-price*(servicetax/100)
    print(totalprice)
newcost(1000,10)
newcost(1000,10,0.1)
newcost(1000,10,0.1,0.2)

def student(school,name,age,grade):
    info={}
    info['name']=name
    info['age']=age
    info['grade']=grade
    info['school']=school
    print(info)
student('sainadh','viveka school','A',23)#since function follows positional arguments we have to use keywords
student(name='sainadh',school='viveka school',age=20,grade='A')




