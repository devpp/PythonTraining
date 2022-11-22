class task3:
    def smalllarge(self):
        #Get inputs from user
        mylist = [int(input("Enter number 1 :- ")),int(input("Enter number 2 :- ")),int(input("Enter number 3 :- "))]

        small = 0
        large = 0

        if mylist[0] < mylist[1] and mylist[0] < mylist[2] :
            small = mylist[0]
        elif mylist[1] < mylist[2] :
            small = mylist[1]
        else :
            small = mylist[2]
    #Largest
        if mylist[0] > mylist[1] and mylist[0] > mylist[2] :
            large = mylist[0]
        elif mylist[1] > mylist[2] :
            large = mylist[1]
        else :
            large = mylist[2]
        myTup = (small,large)
        return myTup
a = task3()
c = a.smalllarge()
print("The smallest number is " , c[0])
print("The largest number is " , c[1])



#3        if mylist[0] > mylist[1] and mylist[0] > mylist[2] :
 #           large = mylist[0]
  #      elif mylist[1] > mylist[2] :
   #         large = mylist[1]
    #    else :
     #       large = mylist[2]
#     #   print(large, "is the largest")
