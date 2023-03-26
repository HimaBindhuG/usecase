month=int(input("enter the month : "))
year=int(input("enter the year : "))

    
if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
    print("Number of days is 29")

elif(month==2) :
    print("Number of days is 28")

elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
    print("Number of days is 31")

else :
    print("Number of days is 30")

"""import re
st="hello2347@#%@%$GAG"
newst=re.sub(r"[^a-zA-Z]","",st)
print(newst.lower())
"""this is new line added