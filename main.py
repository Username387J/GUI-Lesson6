#Do winner_label and title_label kinda stuff
from tkinter import *
import random
import tkinter.font as font
root=Tk()
root.geometry("700x300")
root.title("Rock Paper Scissors Game")

playerscore=0
computerscore=0
options=[('rock',0),('paper',1),('scissors',2)]

def computerwins():
    global playerscore,computerscore
    computerscore+=1
    winner_label.config(text="Computer Won")
    computer_scorelabel.config(text='Computer Score: '+str(computerscore))
    player_scorelabel.config(text="Player Score"+str(playerscore))

def playerwins():
    global playerscore, computerscore
    playerscore+=1
    winner_label.config(text="Player Won")
    player_scorelabel.config(text="Player Score"+str(playerscore))
    computer_scorelabel.config(text="Computer Score"+str(computerscore))

def tie():
    global playerscore,computerscore
    winner_label.config(text="Its a Tie!")
    player_scorelabel.config(text="Player Score"+str(playerscore))
    computer_scorelabel.config(text="Computer Score"+str(computerscore))

def getcomputerchoice():
    return random.choice(options)

def getplayerchoice(playerinput):
    global playerscore,computerscore
    computerinput=getcomputerchoice()
    computer_choicelabel.config(text="Computer Selected: "+ computerinput[0])
    player_choicelabel.config(text="Player Selected: "+playerinput[0])
    
    if playerinput == computerinput:
        tie()
    
    if (playerinput[1] == 0):
        if (computerinput[1] == 1):
            computerwins()
        elif (computerinput[1] == 2):
            playerwins()

    elif (playerinput[1] == 1):
        if (computerinput[1] == 0):
            playerwins()
        elif (computerinput[1] == 2):
            computerwins()

    elif (playerinput[1] == 2):
        if (computerinput[1] == 1):
           playerwins()
        elif (computerinput[1] == 0):
            computerwins() 



title_label=Label(root,text="Rock Paper Scissors Game",font=font.Font(size=20),fg='grey')
title_label.pack()

winner_label=Label(root,text="Let's Start The Game...",font=font.Font(size=16),fg="green")
winner_label.pack()

frame=Frame(root)
frame.pack()

app_font=font.Font(size=12)

player_options = Label(frame,text = "Your Options: ",font=app_font, fg='grey')
player_options.grid(row=0,column=0,pady=8)

rock_button= Button(frame,text="Rock",bg="red",fg="black",command=lambda: getplayerchoice(options[0]))
rock_button.grid(row=1,column=1,padx=8,pady=5)

paper_button = Button(frame,text="Paper",bg="green",fg="black",command=lambda: getplayerchoice(options[1]))
paper_button.grid(row=1,column=2,padx=8,pady=5)

scissors_button = Button(frame,text="Scissors",bg="white",fg="black",command=lambda: getplayerchoice(options[2]))
scissors_button.grid(row=1,column=3,padx=8,pady=5)

score_label=Label(frame,text="Score: ",fg="grey")
score_label.grid(row=2,column=0)

player_choicelabel=Label(frame,text="You Selected: ----",font=app_font)
player_choicelabel.grid(row=3,column=1)

player_scorelabel=Label(frame,text="Your Score: -",font=app_font)
player_scorelabel.grid(row=3,column=2)

computer_choicelabel=Label(frame,text="Computer Selected: ---",font=app_font)
computer_choicelabel.grid(row=4,column=1)

computer_scorelabel=Label(frame,text="Computer Score: -",font=app_font)
computer_scorelabel.grid(row=4,column=2)


root.mainloop()
