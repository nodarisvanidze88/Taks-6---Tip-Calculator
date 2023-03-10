nums = {                                                                            # number dictionary to get integers from string
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, ".": ".", ",": "."
    }
def numberGen(x,y):                                                                 # number generator from string
    x = x.strip()                                                                          # removes extra spaces
    num = list(x)                                                                          # split string to list
    newRes = []                                                                            # create empty list
    for i in num:                                                                          # run loop for check each item in dictionary
        if i in y:                                                                         # check list item in dictionary
            newRes.append(str(y[i]))                                                       # append new list with numbers as string
    return float("".join(newRes))                                                          # generate float number from list

dollars = numberGen(input("How much was the meal? "),nums)                          # !!! important write number generator function before insert this function in input variable
percent = numberGen(input("What percentage would you like to tip? "),nums)          
result = dollars*percent/100
print(f"Leave {result:.2f}")                                                        # print final result
