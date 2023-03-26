def find(m,y):
    big=[1,3,5,7,8,10,12]
    small=[4,6,9,11]
    if(m==2):
        if((y%4==0 and y%100!=0) or (y%400==0 and y%100==0)):
            return ("this month has 29 days and its a leap year!")
        else:
            return("this month has 28 days")
    elif m in big:
        return("this month has 31 days")
    elif m in small:
        return("this month has 30 days")
    else:
        return("please check the data you have entered")

m=int(input("enter the month"))
y=int(input("enter the year"))

result=find(m,y)
print(result)


"""
import re
stri="Hello!, he said and went!!"
stri2= re.sub(r"[^a-zA-Z0-9]"," ",stri)
print(stri2)
"""
