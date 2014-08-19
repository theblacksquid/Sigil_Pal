#===============================================================================
#
#       Sigil_Pal v0.1
#           by theblacksquid, 2014
#       Basic Sigil-Writing Assistant
#       Free and Open-Source, Released under the MIT License
#
#===============================================================================


from tkinter import *

#===============================================================================
#                           FUNCTION LIBRARY
#===============================================================================
numerology = {
"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,
"J":10,"K":20,"L":30,"M":40,"N":50,"O":60,"P":70,"Q":80,"R":90,
"S":100,"T":200,"U":300,"V":400,"W":500,"X":600,"Y":700,"Z":800,
                }

def getNumList(string):
    index = 0                                #turns a string into a list
    result = []                              #of int values based off of
    for char in string:                      #Chaldean numerology
        if char == " ":
            index = index+1
            pass
        else:
            nums = numerology.get(string[index])
            result.append(nums)
            index = index+1
    return result

def getNumVal(int_list):
    index = 0                           #adds up a list of int
    result = 0                          #values into a single value
    for item in int_list:
        result = result+int_list[index]
        index = index+1
    return result

def getBaseNum(int_val):
    string = str(int_val)               #takes an int value and keeps
    while len(string) > 1:              #adding the digits together until
        result = 0                      #one digit is left, the "Base number"
        for digit in string:            #of the number
            result = result+int(digit)
        string = str(result)
    return string

def xtract_letters(string):
    index = 0
    result_string = ""
    for n in string:                        # this loop takes the
        t = string[index] ; t = t.upper()   # user input, uppercases
        chk = result_string.count(t)        # it and removes duplicates
        if chk < 1:
            result_string = result_string + t
        else:
            pass
        index = index + 1
    return result_string

#===============================================================================
#                             USER INTERFACE
#===============================================================================

def main():
    #PRE-INITIALIZATION
    root = Tk()
    root.title("Sigil_Pal")
    frame1 = Frame(root)
    frame2 = Frame(frame1, bd= 3, relief= GROOVE)
    frame3 = Frame(frame1, bd= 3, relief= GROOVE)
    frame1.pack()
    frame2.pack(fill= BOTH, padx= 3, pady= 3)
    frame3.pack(fill= BOTH, padx= 3, pady= 3)

    def frame3_widgets(str_to_process):
        #INITIALIZATION
        inFrame1 = Frame(frame3)
        inFrame1.pack(fill= X)
        inFrame1_1 = Frame(inFrame1)
        inFrame1_1.pack(side= LEFT, fill= BOTH)
        inFrame2 = Frame(inFrame1)
        inFrame3 = Frame(inFrame1)
        inFrame4 = Frame(inFrame1)
        inFrame2.pack(fill= BOTH)
        inFrame3.pack(fill= BOTH)
        inFrame4.pack(fill= BOTH)

        #PROCESSING DATA
        string = xtract_letters(str_to_process)
        num_list = getNumList(string)
        num_val = getNumVal(num_list)
        num_base = getBaseNum(num_val)

        #OUTPUT
        Label(inFrame1_1, text= "Result: ", relief= GROOVE)\
              .pack(fill=X, padx= 3, pady= 3)
        Label(inFrame2, text= string, state= ACTIVE)\
              .pack(fill= X,padx= 3, pady= 3)
        inFrame3_1 = Frame(inFrame3)
        inFrame3_1.pack()
        inFrame3_2 = Frame(inFrame3)
        inFrame3_2.pack()
        Label(inFrame1_1, text= "Numeric Value: ",
              relief= GROOVE).pack(padx= 3, pady= 3, fill= X)
        Label(inFrame3_1, text= num_val,
              state= ACTIVE).pack(side= LEFT, padx= 3, pady= 3)
        Label(inFrame1_1, text= "Base Number: ",
              relief= GROOVE).pack(padx= 3, pady= 3, fill= X)
        Label(inFrame3_2, text= num_base).\
              pack(padx= 3, pady= 3, fill= X)
        def ok_pressed():
            inFrame1.destroy()
        Button(inFrame4, text= "OK", command= ok_pressed
                ).pack(padx= 3, pady= 3, fill= X)

    #USER INPUT
    def frame2_widgets():
        def pressed():
            frame3_widgets(entry.get())

        inFrame1 = Frame(frame2)
        inFrame2 = Frame(frame2)
        inFrame1.pack()
        inFrame2.pack(fill= BOTH)

        Label(inFrame1, text= "Statement of Intent: ")\
              .pack(side= LEFT, padx= 3, pady= 3)
        entry = Entry(inFrame1)
        entry.pack()
        Button(inFrame2, text= "PROCESS!",
                command= pressed).pack(fill=X, padx= 3, pady= 3)

    frame2_widgets()
    root.mainloop()

main()
