from tkinter import*
def attacked():
    wn = Tk()
    buttonA = Button(wn, text='roll(d20)', command=roll20)
    buttonB = Button(wn, text='roll(d12)', command=roll12)
    buttonC = Button(wn, text='roll(d10)', command=roll10)
    buttonD = Button(wn, text='roll(d8)', command=roll8)
    buttonE = Button(wn, text='roll(d6)', command=roll6)
    buttonF = Button(wn, text='roll(d4)', command=roll4)
    buttonG = Button(wn, text='roll(d100)', command=roll100)
    buttonG.pack()
    buttonA.pack()
    buttonB.pack()
    buttonC.pack()
    buttonD.pack()
    buttonE.pack()
    buttonF.pack()
    




#all dnd dices
from random import randint
def roll20():
    print(str(randint(1,20)))
    
    
    


def roll12():
    print(str(randint(1,12)))


def roll10():
    print(str(randint(1,10)))
    
def roll8():
    print(str(randint(1,8)))

def roll6():
    print(str(randint(1,6)))

def roll4():
    print(str(randint(1,4)))

def roll100():
    print(str(randint(1,100)))
    
attacked()      
