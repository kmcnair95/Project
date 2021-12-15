#Project - Buisness Taxes
#Kelton McNair
#12/14/21
#M08 Project

#imports 

from tkinter import *  # library import

# below is the basic information class
class Information():
    def __init__(self, name, address, telephone,ssn):  # the attributes constructor and below are the attributes
        self.name = name
        self.address = address
        self.telephone = telephone
        self.ssn = ssn

# below are the setter functions for the attributes

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setTelephone(self, telephone):
        self.telephone = telephone

    def setSSN(self, ssn):
        self.ssn = ssn


#below are the getter functions for the attributes

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getTelephone(self):
        return self.telephone

    def getSSN(self):
        return self.ssn



# below is the basic information class
class profitLoss():
    def __init__(self, gross, expenses): # the attributes constructor and below are the attributes
        self.gross = gross
        self.expenses = expenses
        #self.pOL


# below are the setter functions for the attributes
    def setGross(self, gross):
        self.gross = gross

    def setExpenses(self, expenses):
        self.expenses = expenses

   # def setPOL(self, pOL):
       # self.pOL = pOL
#below are the getter functions for the attributes

    def getGross(self):
        return self.gross

    def getExpenses(self):
        return self.expenses

    #def getPOL(self):
       # return self.pOL


class Taxes(profitLoss):
    def __init__(self, gross, expenses,  stateTax, fedTax, selfTax, stateP, fedP): # the attributes constructor and below are the attributes
        profitLoss.__init__(self, gross, expenses)
        self.stateTax = stateTax
        self.fedTax = fedTax
        self.selfTax = selfTax
# below are the setter functions for the attributes
    def setStateTax(self, stateTax):
        self.stateTax = stateTax

    def setFedTax(self, fedTax):
        self.fedTax = fedTax

    def setSelfTax(self, selfTax):
        self.selfTax = selfTax

    def setStateP(self, stateP):
        self.stateP = stateP

    def setFedP(self, fedP):
        self.fedP = fedP
#below are the getter functions for the attributes
    def getStateTax(self):
        return self.stateTax

    def getFedTax(fedTax):
        return self.fedTax

    def getSelfTax(self):
        return self.selfTax

    def getStateP(self):
        return self.stateP

    def getFedP(self):
        return self.fedP



#below I declare the variables that I am goting to use to create the class objects
name = ""
address = ""
telephone = 0
ssn = 0
gross = 0
expenses = 0
#pOL = 0
stateTax = 0
fedTax = 0
selfTax = 0
stateP = 0
fedP = 0
#below are the two class object creations
CustomerInformation = Information(name, address, telephone, ssn)
CustomerTaxes = Taxes(gross, expenses, stateTax, fedTax, selfTax, stateP, fedP)

print(
    "This program will help teach and guide you in preparing 1099/ Small Buisness Taxes for Entrepenuers"
)


root = Tk()  # assighning tk as root

root.title("Self Employment Tax Helper")  #title of the application

root.geometry("900x400")  # setting the dimensions of the window size

#the below functions are used to assign a user input value to each of the class object attributes
def grossIncome():
    g = entry.get()
    CustomerTaxes.setGross(g)
    print("You entered", CustomerTaxes.getGross(), "$ as your gross income")

#the below functions are used to assign a user input value to each of the class object attributes
def buisnessExpenses():
    e = entry.get()
    CustomerTaxes.setExpenses(e)
    print("You entered", CustomerTaxes.getExpenses(), "$ as your tax deductable buisness expenses")

#the below functions are used to assign a user input value to each of the class object attributes
def stateTaxPaid():
    sp = entry.get()
    CustomerTaxes.setStateP(sp)
    print("You entered", CustomerTaxes.getStateP(), "$ as the amount of state taxes you have already paid")

#the below functions are used to assign a user input value to each of the class object attributes
def fedTaxPaid():
    fp = entry.get()
    CustomerTaxes.setFedP(fp)
    print("You entered", CustomerTaxes.getFedP(), "$ as the amount of federal taxes you have already paid")
    
#the below functions are used to assign a user input value to each of the class object attributes
def namer():
    ne = entry.get()
    CustomerInformation.setName(ne)
    print("You entered", CustomerInformation.getName(), "as your full legal name")

#the below functions are used to assign a user input value to each of the class object attributes
def add():
    ad = entry.get()
    CustomerInformation.setAddress(ad)
    print("You entered", CustomerInformation.getAddress(), "as your address")

#the below functions are used to assign a user input value to each of the class object attributes
def phone():
    ph = entry.get()
    CustomerInformation.setTelephone(ph)
    print("You entered", CustomerInformation.getTelephone(), "as your telephone number")

#the below functions are used to assign a user input value to each of the class object attributes
def social():
    sc = entry.get()
    CustomerInformation.setSSN(sc)
    print("You entered", CustomerInformation.getSSN(), "as your Social Security number") 




# this function calculates all fo the applicable tax information and displays it by printing the class objects as a compelte package
def finish():
  print("Didn't finish")











#the below functions are used to create multiple pages/different windows for each attribute input, they do this by editing the previous pages and changing the label names as well as the functions called with the button presses
def nextTab():
    firstLabel.config(text="Enter Your Total Buisness Deductions")
    firstButton.config(text="Enter", command=buisnessExpenses)
    oneNext.config(text="Next", command=nextTab3)
    back.config(text="Back", command=firstTab)
    

#the below functions are used to create multiple pages/different windows for each attribute input
def nextTab3():
    firstLabel.config(text="Enter Any State Taxes Already Paid")
    firstButton.config(text="Enter", command=stateTaxPaid)
    oneNext.config(text="Next", command=nextTab4)
    back.config(text="Back", command=nextTab)

#the below functions are used to create multiple pages/different windows for each attribute input
def nextTab4():
    firstLabel.config(text="Enter Any Federal Taxes Already Paid")
    firstButton.config(text="Enter", command=fedTaxPaid)
    oneNext.config(text="Next", command=nextTab5)
    back.config(text="Back", command=nextTab3)

#the below functions are used to create multiple pages/different windows for each attribute input
def nextTab5():
    firstLabel.config(text="Enter your Full Legal Name")
    firstButton.config(text="Enter", command=namer)
    oneNext.config(text="Next", command=nextTab6)
    back.config(text="Back", command=nextTab4)

#the below functions are used to create multiple pages/different windows for each attribute input
def nextTab6():
    firstLabel.config(text="Enter your Full Address")
    firstButton.config(text="Enter", command=add)
    oneNext.config(text="Next", command=nextTab7)
    back.config(text="Back", command=nextTab5)

#the below functions are used to create multiple pages/different windows for each attribute input
def nextTab7():
    firstLabel.config(text="Enter your Telephone Number")
    firstButton.config(text="Enter", command=phone)
    oneNext.config(text="Next", command=nextTab8)
    back.config(text="Back", command=nextTab6)

#the below functions are used to create multiple pages/different windows for each attribute input
def nextTab8():
    firstLabel.config(text="Enter your Full Social Security Number")
    firstButton.config(text="Enter", command=social)
    oneNext.config(text="Next", command=lastTab)
    back.config(text="Back", command=nextTab7)

#This last tab function is used to change the name of the label, destroy the inputs and buttons, and direct the user to the console
def lastTab():
  firstLabel.config(text="Your Tax Printout will appear in the Console")
  oneNext.config(text="Press When Finished", command=openWindow)
  entry.destroy() 
  firstButton.destroy()


#this function is used to return to the first window/tab created
def firstTab():
  #I am unsure how to add the back functionality to return to the first tab, when I try to destroy the existing labels like below, I am getting an error
  #firstButton.destroy()
  #oneNext.destroy()
  #entry.destroy() 
  #firstLabel.destroy()
  #secondLabel.destroy()
  #thirdLabel.destroy() 
    
    #The below variable is used to name and create the first label, on the first page of the gui
  firstLabel = Label(root, text="Enter Your Gross Income")
  firstLabel.pack(side=TOP)

  #this label is used as a disclaimer
  secondLabel = Label(root, text="This program is not to be used to actual Tax Preperation, it is just a guide to help you learn about self employment tax preperation")
  secondLabel.pack(side=BOTTOM)
  #this label is used as a disclaimer
  thirdLabel = Label(root, text="This program was created by Kelton McNair")
  thirdLabel.pack(side=BOTTOM)

  #The below variable is used to name and create the first button on the first page of the gui
  firstButton = Button(root, text="Enter", command=grossIncome)
  firstButton.pack()
  #The below variable is used to name and create the next button, on the first page of the gui
  oneNext = Button(root, text="Next", command=nextTab)
  oneNext.pack()


  #back button created below
  back = Button(root, text="Back")
  back.pack()

  #the below variable creates the entry feild
  entry = Entry(root)
  entry.pack()


#this function below creates a new window to display results
def openWindow():
   new= Toplevel(root)
   new.geometry("900x400")
   new.title("Results")
   Button(new,text="Press to display Results",command=finish).pack()








#The below variable is used to name and create the first label, on the first page of the gui
firstLabel = Label(root, text="Enter Your Gross Income")
firstLabel.pack(side=TOP)

#this label is used as a disclaimer
secondLabel = Label(root, text="This program is not to be used to actual Tax Preperation, it is just a guide to help you learn about self employment tax preperation")
secondLabel.pack(side=BOTTOM)
#this label is used as a disclaimer
thirdLabel = Label(root, text="This program was created by Kelton McNair")
thirdLabel.pack(side=BOTTOM)

#The below variable is used to name and create the first button on the first page of the gui
firstButton = Button(root, text="Enter", command=grossIncome)
firstButton.pack()
#The below variable is used to name and create the next button, on the first page of the gui
oneNext = Button(root, text="Next", command=nextTab)
oneNext.pack()


#back button created below
back = Button(root, text="Back")
back.pack()

#the below variable creates the entry feild
entry = Entry(root)
entry.pack()


