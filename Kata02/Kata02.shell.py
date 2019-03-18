import Kata02_1
#Main code
searchvalue = input("Choose a value:\n")
searchvalue = int(searchvalue)
chopresult = Kata02_1.chop(searchvalue, [1, 5, 44, 45, 51, 600, 710, 711, 900])
if chopresult != -1:
    print("That is in place number:", chopresult+1)
else:
    print("U tryin' to fool me??? SUCKER!!!!")