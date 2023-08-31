import sqlite3 #this line imports the library sqlite3 
import uuid
from appjar import gui
app=gui("ordering system","400x200")
listOfLabels=[]
ChosenItems=[]
numItems=len(ChosenItems)
customerID=[]
FirstReviewOrderVisit=["NotComplete"]

NumPurchasesList=[0]#Global list that stores the users number of past purchases at the store


con=sqlite3.connect('SystemDB-Ilyas.db') #this line creates the database file
cur=con.cursor() #this line creates a cursor inside the file so that changes can be needed if necessary

def createDB(): #this function creates all 4 tables inside of the database.... if it doesnt exist already.
    cur.execute('''CREATE TABLE if not exists "tble_Product" (
            "ProductID"	INTEGER NOT NULL,
            "name"	TEXT NOT NULL,
            "cost"	INTEGER NOT NULL,
            PRIMARY KEY("ProductID")
    );
    ''')
    con.commit()

    cur.execute('''CREATE TABLE if not exists "tble_Order" (
            "Order ID"	TEXT,
            "total cost"	INTEGER,
            "CustomerID"	TEXT,
            PRIMARY KEY("Order ID")
    );
    ''')
    con.commit()

    cur.execute('''CREATE TABLE if not exists "tble_Customer" (
            "CustomerID"	INTEGER NOT NULL UNIQUE,
            "username"	TEXT NOT NULL,
            "Password"	TEXT NOT NULL,
            "email address"	TEXT,
            "NumPurchases"      INTEGER,
            PRIMARY KEY("CustomerID")
    );
    ''')
    con.commit()

    cur.execute('''CREATE TABLE if not exists "tbl_link_order" (
            "Order ID"	TEXT,
            "ProductID"	TEXT,
            "quantity"	INTEGER,
            FOREIGN KEY("Order ID") REFERENCES "tble_Order"("Order Id"),
            FOREIGN KEY("ProductID") REFERENCES "tble_Product"("ProductID")
    );
    ''')
    con.commit()
"""


def addingToProductsTable():
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[1,"Iphone Case" ,20,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[2,"Airpods",80,""])  
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[3,"Speaker",30,""])     
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[4,"HDMI wire",25,""]) 
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[5,"Radio Box",30,""])   
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[6,"Keyboard",15,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[7,"Printer",45,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[8,"Android Charger",20,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[9,"Android Adapter",25,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[10,"Airpods Case",45,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[11,"Chair",15,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[12,"Stool",10,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[13,"Cupholder",15,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[14,"Pillows",20,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[15,"Minitare Cupboard",40,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[16,"Suitcase",30,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[17,"Back Pack",15,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[18,"Hand Carier Bag",35,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[19,"Mat",35,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[20,"Purse",20,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[21,"Hand Cream",10,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[22,"Face Cream",15,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[23,"Hair Conditioner",30,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[24,"Shampoo",20,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[25,"Hair Comb",15,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[26,"Face Masks",25,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[27,"Mens Perfume",45,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[28,"Womens Perfume",45,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[29,"Purse",20,""])
    cur.execute("INSERT INTO tble_Product VALUES (?,?,?,?)",[30,"Afro Comb",10,""])
    con.commit()
createDB()
addingToProductsTable()

"""

"""

def AddingUsers():
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[1,"BukayoSaka","BukayoSaka1","BukayoSaka@gmail.com"])
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[2,"MartinOdegaard","MartinOdegaard1","MartinOdegaard@gmail.com"])  
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[3,"GabrielJesus","GabrielJesus1","GabrielJesus@gmail.com"])     
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[4,"GabrielMartinelli","GabrielMartinelli1","GabrielMartinelli@gmail.com"]) 
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[5,"GranitXhaka","GranitXhaka1","GranitXhaka@gmail.com"])   
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[6,"ThomasPartey","ThomasPartey1","ThomasPartey@gmail.com"])
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[7,"Zinchenko","Zinchenko1","Zinchenko@gmail.com"])
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[8,"WilliamSaliba","WilliamSaliba1","WilliamSaliba@gmail.com"])
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[9,"AarronRamsdale","AarronRamsdale1","AarronRamsdale@gmail.com"])
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[10,"SmithRowe","SmithRowe1","SmithRowe@gmail.com"])
    cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?)",[11,"MrIlyas","IlyasHussein","IlyasHussein@gmail.com"])
    con.commit()
AddingUsers()    
"""


def Continue(*args):
    app.showSubWindow("Login")
    app.hide("ordering system")

def Guest(*args):
    app.hideSubWindow("Login")
    app.showSubWindow("GuestAccount")

def Back(*args):
    app.hideSubWindow("GuestAccount")
    app.showSubWindow("Login")

def BackToLogin(*args):
    app.hideSubWindow("Create Account")
    app.showSubWindow("Login")
    if len(customerID)>=1:
        customerID.pop()
    

def Confirm(*args):
    CreateEntryUsername=(app.getEntry("Create Username"))#saves the entered username in the CreateEntryUsername variable 
    CreateEntryPassword=(app.getEntry("Create Password"))#saves the entered password in the CreateEntryPassword variable
    CreateEntryEmailAddress=(app.getEntry("Email Address"))#saves the entered email address in the CreateEntryEmailAddress varaible
    Valid=CreateAccountValidation(CreateEntryUsername,CreateEntryPassword,CreateEntryEmailAddress)# passes the details into the validation function
    if Valid==False:
        app.warningBox("Incorrect username/password/email address length","Username must be greater than 5 characters, password must be greater than 8 and email address must include @ and .com and account must not currently exist", parent=None)
        #if it has not upheld the rules of validation show an error
        print(Valid)
    elif Valid==True:
        print(Valid)
        app.infoBox("New Account message","Congratulations for creating a new account "+CreateEntryUsername+". Customers that have more than 50 purchases at the store will be eligible for a discount", parent=None)
        app.hideSubWindow("Create Account")
        app.showSubWindow("Main")
        LastId=cur.execute("SELECT MAX(CustomerID) FROM tble_Customer")#get the last customer Id in table
        LastId=cur.fetchone()
        customerID.append(LastId[0]+1)
        cur.execute("INSERT INTO tble_Customer VALUES (?,?,?,?,?)",[LastId[0]+1,CreateEntryUsername,CreateEntryPassword,CreateEntryEmailAddress,1])#insert values
        con.commit()


def ConfirmAsGuest(*args):
    app.infoBox("GuestAccount","Welcome,Guest", parent=None)
    app.hideSubWindow("GuestAccount")
    app.showSubWindow("Main")
    customerID.append("Guest")
    

def Quit(*args):
    app.hideSubWindow("Main")
    app.showSubWindow("Login")
    ChosenItems.clear()
    NumPurchasesList.clear()
    NumPurchasesList.append(0)
    customerID.clear()
    app.setLabel("LbMainMenu","Main Menu")
    print(customerID)
    print(NumPurchasesList)
    print(ChosenItems)
    
    
def reviewOrder(*args):
    numItems=len(ChosenItems)
    if FirstReviewOrderVisit[0]=="Completed":
        app.openSubWindow("ReviewOrder")
        app.setBg("#E2F0D9")
        app.setSize(500, 400)
        app.addLabel("LblNumItems",str(numItems) + " unique items in basket",2,0)
        app.getLabelWidget("LblNumItems").config(font="Times 12 underline")
        app.setSticky("W")
        app.addButton("BackToMain",BackToMain,40,0)
        app.setSticky("Ne")
        app.addButton("EmptyBasket",EmptyBasket,0,4)
        app.setSticky("e")
        app.addButton("ConfirmOrder",ConfirmOrder,40,4)
        app.addLabel("lbReviewOrder","Review Order",0,1)
        app.getLabelWidget("lbReviewOrder").config(font="Times 15 underline")
        app.addButton("Check Current Price",currentprice,40,2)
        app.addLabel("lbPrice"," current price:?",3,0)
        app.stopSubWindow()
            
    app.hideSubWindow("Main")
    app.showSubWindow("ReviewOrder")
        
    app.setLabel("LblNumItems",str(numItems) + " unique items in basket")
        
        
    app.openSubWindow("ReviewOrder")
    for item in ChosenItems:
        if item[2]==0:
            ChosenItems.remove(item)
    xCord1=4
    yCord1=0
    for eachItem in ChosenItems:
        
        app.addLabel(eachItem[0],eachItem[0],xCord1,yCord1)
            
        app.addSpinBoxRange(eachItem[0], 0 ,30 , xCord1,yCord1+1)
             
        app.setSpinBox(eachItem[0],eachItem[2], callFunction=True)
             
        xCord1=xCord1+1
        
        #iterates through list of chosen items and adds a label and spinbox for each item
        
    totalPrice=[[]]
    for eachitem in ChosenItems:
        eachitem[2]=int(app.getSpinBox(eachitem[0]))
        totalPrice.append([eachitem[1],eachitem[2]])
    totalPrice.remove(totalPrice[0])
   
    CurrentPrice=SumList(totalPrice)
    app.setLabel("lbPrice"," current price:"+"£"+str(CurrentPrice))
        
    app.stopSubWindow()

    FirstReviewOrderVisit[0]=("Completed")
    
    print(ChosenItems)

    for item in ChosenItems:
        if item[2]>12:
            item[2]=12
    

def currentprice():
    ####
    totalPrice=[[]]
    for eachitem in ChosenItems:
        eachitem[2]=int(app.getSpinBox(eachitem[0]))
        totalPrice.append([eachitem[1],eachitem[2]])
    totalPrice.remove(totalPrice[0])
    ####these lines of code stores the price and quantity of each item together inside a 2d array totalPrice
    CurrentPrice=SumList(totalPrice)
    #stores the price generated from the function SumList in the variable CurrentPrice 
    app.openSubWindow("ReviewOrder")
    app.setLabel("lbPrice"," current price:"+"£"+str(CurrentPrice))
    #updates the label on the review order page with the updated current price
    app.stopSubWindow()



def BackToMain(*args):
    if len(ChosenItems)>=1:
        for item in ChosenItems:
            item[2]=int(app.getSpinBox(item[0]))
            print(app.getSpinBox(item[0]))
            #updates the quantity of each item in the list with the inputted quantity from the user
                #removes items that have a quanitiy of 0 from list
        i=0
        k=0
        while i<len(ChosenItems):
            if ChosenItems[i][2]==0:
                ChosenItems.pop(k)
            else:
                k=k+1
                i=i+1
    #removes items that have a quanitiy of 0 from list
    
    app.hideSubWindow("ReviewOrder")
    app.emptySubWindow("ReviewOrder")
    #deletes all widgets on the review order page

    count=0
    for item in ChosenItems:
        count=count+item[2]
    app.setLabel("LbMainMenu","Main Menu        "+str(count)+" items")
    if len(ChosenItems)==0:
        app.setLabel("LbMainMenu","Main Menu        "+str(0)+" items")
    app.showSubWindow("Main")




def ConfirmOrder(*args):
    totalPrice=[[]]
    for eachitem in ChosenItems:
        eachitem[2]=int(app.getSpinBox(eachitem[0]))
        totalPrice.append([eachitem[1],eachitem[2]])
    totalPrice.remove(totalPrice[0])
    FinalPrice=SumList(totalPrice)
    #########Final price is calculated
    
    if NumPurchasesList[0]>50:
        if FinalPrice>50:
            FinalPrice=FinalPrice-(FinalPrice*0.3)
    #########the discount is applied
        
    if len(customerID)!=0:
        cur.execute("UPDATE tble_Customer SET NumPurchases=? WHERE CustomerID=?",[NumPurchasesList[0]+1,customerID[0]])
        con.commit()
    #########number of puchases is incremented
    if FinalPrice==0:
        app.warningBox("Final price is 0","the price of your order is currently £0. Please select an item", parent=None)
    else:
        app.hideSubWindow("ReviewOrder")
        app.openSubWindow("FinalOrderPage")
        app.setLabel("FinalPrice","Final Price:  £"+ str(FinalPrice))
        Unique=str(uuid.uuid4())[0:4]#unique order ID generated
        app.setLabel("UniqueOrderId","Your order ID is:  "+ Unique)
        app.setLabel("LbMessageEnd","Thank you for shopping")

        app.showSubWindow("FinalOrderPage")
        
        for x in ChosenItems:
            cur.execute("SELECT ProductID FROM tble_Product WHERE name=?",[x[0]])
            ProdID=cur.fetchone()
            cur.execute("INSERT INTO tbl_link_order VALUES (?,?,?)",[Unique,ProdID[0],x[2]])
            con.commit()
            
        cur.execute("INSERT INTO tble_Order VALUES (?,?,?)",[Unique,FinalPrice,customerID[0]])#insert values
        con.commit()
        app.stopSubWindow()
    print(customerID)


def SumList(listsOfNums):
    if len(listsOfNums)==0:
        return 0
    else:
        return (listsOfNums[0][0]*listsOfNums[0][1])+SumList(listsOfNums[1:])





def End(*args):
    app.openSubWindow("ReviewOrder")
    app.stopSubWindow()
    app.hideSubWindow("FinalOrderPage")
    ChosenItems.clear()
    NumPurchasesList.clear()
    NumPurchasesList.append(0)
    print(ChosenItems)
    app.emptySubWindow("ReviewOrder")
    app.setLabel("LbMainMenu","Main Menu")
    app.show()

def EmptyBasket(*args):
    ChosenItems.clear()#removes all items from the basket of goods
    app.emptySubWindow("ReviewOrder")#this line empties the container review order
    #########
   
    numItems=len(ChosenItems)
    stringNumItems=str(numItems)
    app.openSubWindow("ReviewOrder")
    app.setBg("#E2F0D9")
    app.setSize(500, 400)
    app.addLabel("LblNumItems",str(numItems) + " unique items in basket",2,0).config("underline")
    app.getLabelWidget("LblNumItems").config(font="Times 12 underline")
    app.setSticky("W")
    app.addButton("BackToMain",BackToMain,40,0)
    app.setSticky("Ne")
    app.addButton("EmptyBasket",EmptyBasket,0,4)
    app.setSticky("e")
    app.addButton("ConfirmOrder",ConfirmOrder,40,4)
    app.addLabel("lbReviewOrder","Review Order",0,0)
    app.getLabelWidget("lbReviewOrder").config(font="Times 15 underline")
    app.addButton("Check Current Price",currentprice,40,2)
    app.addLabel("lbPrice"," current price:?",3,0)
    app.stopSubWindow()
    ##########these lines of code repopulate the review order page with the basic founational widgets
    app.setLabel("LblNumItems",str(numItems) + " unique items in basket")
    app.openSubWindow("ReviewOrder")
    
    app.setLabel("lbPrice"," current price:"+"£"+str(0))#updates the current price on the review order page to 0

    print(ChosenItems)
    app.stopSubWindow()


def firstPage(*args):
    app.emptySubWindow("Main")
    cur.execute("Select name,cost from tble_Product LIMIT 0,10")
    results=cur.fetchall()
    Products=results
    Products=Products[0:10]
    ###########################
    app.openSubWindow("Main")
    app.setBg("#E2F0D9")
    app.setSize(750, 600)
    app.setFont(9)
    app.addButton("<Page1",firstPage,20,0,0)
    app.addButton("Page2", SecondPage,20,4,0)
    app.addButton("Page3>",LastPage,20,6,0)
    app.setSticky("Ne")
    app.addButton("review order",reviewOrder,0,6,0)
    app.setSticky("w")
    app.addLabel("lbMessage10","please choose your items:",1,0,0)
    app.getLabelWidget("lbMessage10").config(font="Times 12 underline")
    app.setSticky("Nw")
    app.addButton("Quit",Quit,0,0,0)
    app.setSticky("N")
    app.addLabel("LbMainMenu","Main Menu",0,4,0)
    app.getLabelWidget("LbMainMenu").config(font="Times 15")
    ########################this section repopulates the main menu with the basic foundation
    xCord=4
    yCord=0
    AddtoBasket="add to Basket"
    extraNum='0'
    ############################
    for x in range(len(Products)):
        app.addLabel(Products[x][0]+str(x),Products[x][0],xCord,yCord,0)
        app.addLabel(str(Products[x][1])+str(x),("£",+Products[x][1]),xCord,yCord+4,0)
        app.addNamedButton("Add to basket",extraNum,ItemBtn,xCord,yCord+6,0)
        
        listOfLabels[x]=([Products[x][0],Products[x][1],extraNum])
        extraNum=extraNum+str(1)
        xCord=xCord+1
    print(listOfLabels)
    count=0
    i=0
    while i <len(ChosenItems):
        count=count+ChosenItems[i][2]
        i=i+1
    app.setLabel("LbMainMenu","Main Menu        "+str(count)+" items")
    app.stopSubWindow()
    ####this secion of the code iterates through the list of products and displays the products onto the page accordingly


def SecondPage(*args):
    app.emptySubWindow("Main")
    cur.execute("Select name,cost from tble_Product LIMIT 10 OFFSET 10")
    results=cur.fetchall()
    Products=results
    Products=Products[0:20]
    ###########################
    app.openSubWindow("Main")
    app.setBg("#E2F0D9")
    app.setSize(750, 600)
    app.setFont(9)
    app.addButton("<Page1",firstPage,20,0,0)
    app.addButton("Page2", SecondPage,20,4,0)
    app.addButton("Page3>",LastPage,20,6,0)
    app.setSticky("Ne")
    app.addButton("review order",reviewOrder,0,6,0)
    app.setSticky("w")
    app.addLabel("lbMessage10","please choose your items:",1,0,0)
    app.getLabelWidget("lbMessage10").config(font="Times 12 underline")
    app.setSticky("Nw")
    app.addButton("Quit",Quit,0,0,0)
    app.setSticky("N")
    app.addLabel("LbMainMenu","Main Menu",0,4,0)
    app.getLabelWidget("LbMainMenu").config(font="Times 15")
    ########################this section repopulates the main menu with the basic foundation
    xCord=4
    yCord=0
    AddtoBasket="add to Basket"
    extraNum='01111111111'
    ############################
    for x in range(len(Products)):
        app.addLabel(Products[x][0]+str(x),Products[x][0],xCord,yCord,0)
        app.addLabel(str(Products[x][1])+str(x),("£",+Products[x][1]),xCord,yCord+4,0)
        app.addNamedButton("Add to basket",extraNum,ItemBtn,xCord,yCord+6,0)
        listOfLabels[x]=([Products[x][0],Products[x][1],extraNum])
        extraNum=extraNum+str(1)
        xCord=xCord+1
    print(listOfLabels)
    count=0
    i=0
    while i <len(ChosenItems):
        count=count+ChosenItems[i][2]
        i=i+1
    app.setLabel("LbMainMenu","Main Menu        "+str(count)+" items")
    app.stopSubWindow()
    ####this secion of the code iterates through the list of products and displays the products onto the page accordingly



def LastPage(*args):
    app.emptySubWindow("Main")
    cur.execute("Select name,cost from tble_Product LIMIT 10 OFFSET 20")
    results=cur.fetchall()
    Products=results
    Products=Products[0:30]
    ###########################
    app.openSubWindow("Main")
    app.setBg("#E2F0D9")
    app.setSize(750, 600)
    app.setFont(9)
    app.addButton("<Page1",firstPage,20,0,0)
    app.addButton("Page2", SecondPage,20,4,0)
    app.addButton("Page3>",LastPage,20,6,0)
    app.setSticky("Ne")
    app.addButton("review order",reviewOrder,0,6,0)
    app.setSticky("w")
    app.addLabel("lbMessage10","please choose your items:",1,0,0)
    app.getLabelWidget("lbMessage10").config(font="Times 12 underline")
    app.setSticky("Nw")
    app.addButton("Quit",Quit,0,0,0)
    app.setSticky("N")
    app.addLabel("LbMainMenu","Main Menu",0,4,0)
    app.getLabelWidget("LbMainMenu").config(font="Times 15")
    ########################this section repopulates the main menu with the basic foundation
    xCord=4
    yCord=0
    AddtoBasket="add to Basket"
    extraNum='011111111111111111111'
    ############################
    for x in range(len(Products)):
        app.addLabel(Products[x][0]+str(x),Products[x][0],xCord,yCord,0)
        app.addLabel(str(Products[x][1])+str(x),("£",+Products[x][1]),xCord,yCord+4,0)
        app.addNamedButton("Add to basket",extraNum,ItemBtn,xCord,yCord+6,0)
        
        listOfLabels[x]=([Products[x][0],Products[x][1],extraNum])
        extraNum=extraNum+str(1)
        xCord=xCord+1
    print(listOfLabels)
    count=0
    i=0
    while i <len(ChosenItems):
        count=count+ChosenItems[i][2]
        i=i+1
    app.setLabel("LbMainMenu","Main Menu        "+str(count)+" items")
    app.stopSubWindow()
    ####this secion of the code iterates through the list of products and displays the products onto the page accordingly


def OutputItems():
    cur.execute("Select name,cost from tble_Product LIMIT 0,10")
    results=cur.fetchall()
    return results

def confirmLogin(*args):
    EntryUsername=(app.getEntry("Username"))
    #stores the entered username in the variable EntryUsername
    EntryPassword=(app.getEntry("Password"))
    #stores the entered password in the variable EntryPassword
    Valid=LoginValidation(EntryUsername,EntryPassword)#this line passes the inputted entries through the the validation function 
    print(Valid)
    if Valid==False:
        app.warningBox("Incorrect username/password length","Username must be greater than 5 characters and password must be greater than 8", parent=None)
        #this line prompts the user re enter their details if the output from the validation functions comes out as false 
    elif Valid==True:
        cur.execute("SELECT Password,CustomerID FROM tble_Customer WHERE Username=?",[EntryUsername]) 
        result=cur.fetchone()
        #these lines search the table for the entered username and password and store the results in the variable result
        print(result)
        if result==None:
            app.warningBox("InvalidEntry"," either username or password is incorrect", parent=None)
            #if the entered username or password does not exist the table an error will occur prompting the user to renter their details
        elif result[0]==EntryPassword:
            cur.execute("SELECT NumPurchases FROM tble_Customer WHERE Username=?",[EntryUsername])
            NumberOfPurchases=cur.fetchone()
            NumPurchasesList[0]=(NumberOfPurchases[0])
            if NumPurchasesList[0]>=51:
                DistanceFromDiscount=NumPurchasesList[0]
            else:
                DistanceFromDiscount=51-NumPurchasesList[0]
            if DistanceFromDiscount>50:
                app.infoBox("DiscountHasApplied","Welcome "+EntryUsername+". Your eligible for a discount, make a purchase above £100 and you can have 30% off!",parent=None)
            elif DistanceFromDiscount==1:
                app.infoBox("DiscountHasNotApplied","Welcome "+EntryUsername+"!. You are only "+str(DistanceFromDiscount)+" purchase away from being able to use a 30% discount",parent=None)
            else:
                app.infoBox("DiscountHasNotApplied2","Welcome "+EntryUsername+"!. After "+str(DistanceFromDiscount)+" more purchases you will be eligible for a 30% discount",parent=None)
                
            print(NumberOfPurchases[0])
            customerID.append(result[1])
            app.hideSubWindow("Login")
            app.showSubWindow("Main")
        else:
            app.warningBox("Invalid username or password"," either username or password is incorrect", parent=None)
            #if the password entered does match the password stored in the database of that username the user is allowed to procced to the main menu

    
def LoginValidation(EnteredUsername,EnteredPassword):
    valid=False
    #This line sets the variable valid to false 
    if len(EnteredUsername)<5:
        #the first condition set will check to see whether the username entered is less than 5 characters
        valid=False
        #if condition has been met then Valid will remain as false
    elif len(EnteredPassword)<8:
        #the second condition will check to see whether the password entered is less than 8 characters
        valid=False
        #if condition has been met then Valid will remain as false
    else:
        valid=True
        #if both of these conditions have not been met then Valid will set to true
    return valid
    
def createAccountButton(*args):
    app.hideSubWindow("Login")
    app.showSubWindow("Create Account")

def CreateAccountValidation(EnteredUsername,EnteredPassword,EnteredEmailAddress):
    valid=False#the variable valid is set to false
    if len(EnteredUsername)<6:
        valid=False
        #if the condition was met valid is set to false
        return valid
    else:
        #if has not met the condition valid is set to true
        valid=True
    if len(EnteredPassword)<8:
        valid=False
        #if the condition was met valid is set to false
        return valid
    else:
        Valid=True
        #if has not met the condition valid is set to true
    if ".com" and "@" not in EnteredEmailAddress:
        valid=False
        #if the condition was met valid is set to false
        return valid
    else:
        valid=True
        #if has not met the condition valid is set to true
    cur.execute("SELECT 1 FROM tble_Customer WHERE username=?",[EnteredUsername])
    exists=cur.fetchone()
    if exists!=None:
        valid=False
    return valid
        

def ItemBtn(btn):
    i=0
    notfound=False
    for name,cost,Button in listOfLabels:
        if Button==btn:
            if len(ChosenItems)==0:
                ChosenItems.append([name,cost,1])
                notfound=True
                #the first condition checks if the lists empty and adds to it if it is
            while notfound==False and i<len(ChosenItems):
                if ChosenItems[i][0]==name:
                    ChosenItems[i][2]=ChosenItems[i][2]+1
                    notfound=True
                i=i+1
                #the second condition checks to see whether an item exists in the list of items
            
            if notfound==False:
                if (name,cost,1) not in ChosenItems:
                    ChosenItems.append([name,cost,1])
                    #finally if the list is not empty and the item does not currently exist in the list it is added
                    
    count=0
    i=0
    while i <len(ChosenItems):
        count=count+ChosenItems[i][2]
        i=i+1
    app.setLabel("LbMainMenu","Main Menu        "+str(count)+" items")
    
    


def createInterFace():
    ###############welcome page############
    app.addLabel("lblWelcome1","Welcome to the retail corner",0,0,2)
    app.getLabelWidget("lblWelcome1").config(font="Times 15 underline")
    app.addButton("continue button",Continue,3,0,2)
    app.setBg("#E2F0D9")
    app.setSize(350, 300)
    ###############login##################
    app.startSubWindow("Login")
    app.setBg("#E2F0D9")
    app.setSize(500, 400)
    app.addLabel("lbLogin","Login",0,0,4)
    app.getLabelWidget("lbLogin").config(font="Times 15 underline")
    app.addLabel("lbWelcome2","Welcome to the retail corner!",1,0)
    app.addLabel("lbLoginMessage","please login:",2,0)
    
    app.addLabel("lbUsername","Username:",3,0)
    app.addEntry("Username",3,1)
    app.addLabel("lbPassword","Password:",4,0)
    app.addSecretEntry("Password",4,1)
    app.addButton("Submit",confirmLogin,5,1,1)
    app.addButton("Guest",Guest,5,0,0)
    app.addButton("Create Account",createAccountButton,5,2,3)
    app.stopSubWindow()
    ###############Guest Account##############
    app.startSubWindow("GuestAccount")
    app.setBg("#E2F0D9")
    app.setSize(450, 250)
    app.addButton("ConfirmAsGuest",ConfirmAsGuest,3,3)
    app.addLabel("lbGuest","Sign in as Guest",0,2)
    app.getLabelWidget("lbGuest").config(font="Times 15 underline")
    app.addLabel("lbWelcome3","Welcome to retail corner!",1,2)
    app.addButton("Back button",Back,3,1)
    
    app.stopSubWindow()
    ##############create Account#############
    app.startSubWindow("Create Account")
    app.setBg("#E2F0D9")
    app.setSize(500, 400)
    app.addLabel("lbCreateAccount","Create Account",0,0,3)
    app.getLabelWidget("lbCreateAccount").config(font="Times 15 underline")
    app.addLabel("lbWelcome4","welcome to retail corner!",1,0,0)
    app.addLabel("lbMessage","please create an account:",3,0)
    app.addLabel("labelUsername","Username:",4,0)
    app.addEntry("Create Username",4,1)
    app.addLabel("labelPassword","Password:",5,0)
    app.addSecretEntry("Create Password",5,1)
    app.addLabel("Email Address","Email address:",6,0)
    app.addEntry("Email Address",6,1)
    app.addButton("BackToLogin",BackToLogin,8,0)
    app.addButton("Confirm",Confirm,8,2,0)
    app.stopSubWindow()
    ###################Main###################
    app.startSubWindow("Main")
    app.setBg("#E2F0D9")
    app.setSize(750, 600)
    app.setFont(9)
    app.addButton("<Page1",firstPage,20,0,0)
    app.addButton("Page2", SecondPage,20,4,0)
    app.addButton("Page3>",LastPage,20,6,0)
    app.setSticky("Ne")
    app.addButton("review order",reviewOrder,0,6,0)
    app.setSticky("w")
    app.addLabel("lbMessage10","please choose your items:",1,0,0)
    app.getLabelWidget("lbMessage10").config(font="Times 12 underline")
    app.setSticky("Nw")
    app.addButton("Quit",Quit,0,0,0)
    app.setSticky("N")
    app.addLabel("LbMainMenu","Main Menu",0,4,0)
    app.getLabelWidget("LbMainMenu").config(font="Times 15 ")
    #app.addButton("Update content on review order",UpdateReviewOrder,14,0,0)
    Products=OutputItems()
    xCord=4
    yCord=0
    AddtoBasket="add to Basket"
    extraNum='0'
    
    for x in range(len(Products)):
        app.addLabel(Products[x][0]+str(x),Products[x][0],xCord,yCord,0)
        app.addLabel(str(Products[x][1])+str(x),("£",+Products[x][1]),xCord,yCord+4,0)
        app.addNamedButton("Add to basket",extraNum,ItemBtn,xCord,yCord+6,0)
        
        listOfLabels.append([Products[x][0],Products[x][1],extraNum])
        extraNum=extraNum+str(1)
        xCord=xCord+1
    print(listOfLabels)
        
    app.stopSubWindow()
    ################review order##############
    app.startSubWindow("ReviewOrder")
    app.setBg("#E2F0D9")
    app.setSize(500, 400)
    app.addLabel("LblNumItems",str(numItems) + " items in basket",2,0,0)
    app.getLabelWidget("LblNumItems").config(font="Times 12 underline")
    app.setSticky("W")
    app.addButton("BackToMain",BackToMain,40,0)
    app.setSticky("Ne")
    app.addButton("EmptyBasket",EmptyBasket,0,4)
    app.setSticky("e")
    app.addButton("ConfirmOrder",ConfirmOrder,40,4)
    app.addLabel("lbReviewOrder","Review Order",0,1)
    app.getLabelWidget("lbReviewOrder").config(font="Times 15 underline")
    app.addButton("Check Current Price",currentprice,40,2)
    app.addLabel("lbPrice"," current price:?",3,0)
    app.stopSubWindow()
     # talk about the scaling issue previously potentially
    ################Final Order Page##########
    app.startSubWindow("FinalOrderPage")
    app.setBg("#E2F0D9")
    app.setSize(500, 400)
    app.addButton("End",End,6,2,2)
    app.addLabel("lbFinalOrderPage","FinalOrderPage",0,2,2)
    app.getLabelWidget("lbFinalOrderPage").config(font="Times 15 underline")
    app.addLabel("FinalPrice","Final Price:  £",4,2,2)
    app.addLabel("UniqueOrderId","Your order ID is:  ",5,2,2)
    app.addLabel("LbMessageEnd","Thank you for shopping",1,2,2)
    
    app.stopSubWindow()
    app.go()
createInterFace()

