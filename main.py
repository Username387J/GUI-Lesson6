#Do winner_label and title_label kinda stuff
from tkinter import *
import random
import tkinter.font as font
root=Tk()
root.geometry("700x300")
root.title("Rock Paper Scissors Game")


title_label=Label(root,text="Rock Paper Scissors Game",font=font.Font(size=20),fg='grey')
title_label.pack()

winner_label=Label(root,text="Let's Start The Game...",font=font.Font(size=16),fg="green")
winner_label.pack()

frame=Frame(root)
frame.pack()

app_font=font.Font(size=12)

player_options = Label(frame,text = "Your Options: ",font=app_font, fg='grey')
player_options.grid(row=0,column=0,pady=8)

rock_button= Button(frame,text="Rock",bg="red",fg="black",command=None)
rock_button.grid(row=1,column=1,padx=8,pady=5)

paper_button = Button(frame,text="Paper",bg="green",fg="black",command=None)
paper_button.grid(row=1,column=2,padx=8,pady=5)

scissors_button = Button(frame,text="Scissors",bg="white",fg="black",command=None)
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
