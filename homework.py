from tkinter import*
import tkinter.font as font
root = Tk()
root.geometry("530x220")
root.title("Speed Calculator")

def change():
    time = timeentry.get()
    distance = distanceentry.get()

    # Validate both inputs
    if time.replace(".", "", 1).isdigit() and distance.replace(".", "", 1).isdigit():
        noticelabel.grid_forget()
        speed = round((float(distance) / float(time)), 3)
        outputlabel.config(text="The speed in total is " + str(speed))
    else:
        noticelabel.grid(row=2, column=0)


titlelabel = Label(root, text="speed calc ", font=font.Font(size=20))
titlelabel.pack()

frame = Frame(root)
frame.pack(pady=20)

timelabel = Label(frame, text="Enter time taken here: ")
timelabel.grid(row=1, column=0)

distancelabel = Label(frame, text="Enter distance : ")
distancelabel.grid(row=1, column=1)

timeentry = Entry(frame, width=20)
timeentry.grid(row=2, column=0)

distanceentry = Entry(frame, width=20)
distanceentry.grid(row=2, column=1)

noticelabel = Label(frame, text="Please enter a number")

outputlabel = Label(frame)
outputlabel.grid(row=3, column=0)

converterbutton = Button(frame, text="Convert", command=change)
converterbutton.grid(row=4, column=0)

root.mainloop()
