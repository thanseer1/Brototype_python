Food=["null","beef curry","porotta","chicken curry","biriyani"]

print(
    " 1 is beef curry \n 2 is  porotta \n 3 is  chicken curry \n 4 is  bririyani"

)

select=int(input("please the enter the order number\n"))



if(select==1):
    print(Food[1])
elif(select==2):
    print(Food[2])
elif(select==3):
    print(Food[3])
elif(select==4):
    print(Food[4])
else:
   print("invalid")                