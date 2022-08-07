from cgitb import text
from tkinter import *
from tkinter.tix import *
root = Tk()
root.geometry("500x300")


def getvals():
    print("Accepted")


# Heading
Label(root, text="Python Registration Form",
      font="arail 15 bold").grid(row=0, column=3)

# Field Name
Name = Label(root, text="Name")
Phone = Label(root, text="Phone")
Gender = Label(root, text="Gender")
Emergency = Label(root, text="Emergency")
Paymentmode = Label(root, text="Payment Mode")

# Packing Field
Name.grid(row=1, column=2)
Phone.grid(row=2, column=2)
Gender.grid(row=3, column=2)
Emergency.grid(row=4, column=2)
Paymentmode.grid(row=5, column=2)

# Variable for storing data
namevalue = StringVar
Phonevalue = StringVar
Gendervalue = StringVar
Emergencyvalue = StringVar
Paymentmodevalue = StringVar
checkvalue = IntVar

# Creating Entery Field
Nameentry = Entry(root, textvariable=namevalue)
Phoneentry = Entry(root, textvariable=Phonevalue)
Genderentry = Entry(root, textvariable=Gendervalue)
Emergencyentry = Entry(root, textvariable=Emergencyvalue)
Paymentmodeenrty = Entry(root, textvariable=Emergencyvalue)

# Packing Entry Field
Nameentry.grid(row=1, column=3)
Phoneentry.grid(row=2, column=3)
Genderentry.grid(row=3, column=3)
Emergencyentry.grid(row=4, column=3)
Paymentmodeenrty.grid(row=5, column=3)

# Creating Check Box

Checkbtn = Checkbutton(text="Remeber Me!?", variable=checkvalue)
Checkbtn.grid(row=6, column=3)

# Submit button

Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()
