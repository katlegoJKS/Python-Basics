import calendar
import datetime
import random
import os
import ctypes

a = [1,2,3,4,5]                                         #Array declaration and their elelments
b = [11,22,33,44,55]    
c = a + b                                               #Adding Array a and Array b

#Adding two Arrays
print("Addition of Arrrays 'a' and 'b':\n")
print("Array a is equal to:",a)
print("Array b is equal to:",b)
print("\nArray a + Array b =",c,"\n")
print("\n")

#Swapping Array elements
a,b = b,a
print("----------Swapping a with b----------")           #Swap elements of Array 'a' with elements of Array 'b'
print("Now a is equals to:",a)
print("Now b is equals to:",b)
print("\n")

#Listing elements of Array a
a = list(a)
print("listing the elements of a: ")                     #list the elements of 'a'
print(a)
print("\n")

#Joining text
msg = ['hello','world']
print(msg)
print("Here is the joint text of the above message.")
msg=''.join(msg)                                         #outputs the joined message of 'msg'
print(msg)
print("\n")

#Display todays date and time, after importing 'datetime' syt. function
date = datetime.datetime.now()          
date = date.strftime("%d-%m-%Y %I:%M:%S %p")
print("The date and time right now is: ")
print(date)
print("\n")

#Using randomness after importing 'random' syst. function
print("A random element of Array a: ")
print(random.choice(a))                                    #picks a random element in Array a
print("A random element of Array b: ")
print(random.choice(b))                                    #picks a random element in Array b
print("\n")

#Using color after importing 'os' syst. function
#os.system('color A')
print('\u001b[31mHello \u001b[33mWorld! \u001b[32min \u001b[34mdifferent \u001b[36mcolors: ')       #copy color code from 'ansi color codes' on google

#Creating message box after importing 'ctypes' syst. function
#ctypes.windll.user32.MessageBoxA(O,'This is great','message',O)

#Displays the calender after importing 'calender' syst. function
print("\n \u001b[0m")                                      #resets color to default                
print(calendar.month(1992,3))