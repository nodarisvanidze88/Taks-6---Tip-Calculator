nums = [                                                                            # number list
    "0", "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "."
    ]
def numberGen(x,y):                                                                 # number generator from string
    x = x.strip()                                                                          # removes extra spaces
    num = list(x)                                                                          # split string to list
    newRes = []                                                                            # create empty list
    for i in num:
        if i == ",":
            newRes.append(".")                                                             # run loop for check each item in dictionary
        elif i in y:                                                                       # check list item in dictionary
            newRes.append(i)                                                       # append new list with numbers as string
    return float("".join(newRes))                                                          # generate float number from list

dollars = numberGen(input("How much was the meal? "),nums)                         # !!! important write number generator function before insert this function in input variable
percent = numberGen(input("What percentage would you like to tip? "),nums)

print("Leave "+ str(dollars*percent/100))                                          # print final result
