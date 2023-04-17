import pickle

def write():
    p=open("hello.txt","wb")
    print('$'*52,end=' ')
    print('CUSTOMERS',end=" ")
    print('$'*52,end='')
    print()

    k="yes"
    while k=="yes":
        num=int(input("Enter the serial number: "))
        name=input("Enter the name of customer: ")
        date=(input("Enter the date of shopping: "))
        t=[num,name,date]
        pickle.dump(t,p)
        k=input("Do u want to store more record(yes/no): ")
    p.close()

def write1():
    p=open("hello1.txt","wb")
    print('\n'*2)
    print('$'*52,end=' ')
    print('ITEMS',end=" ")
    print('$'*52,end='')
    print()
    k='yes'
    while k=="yes":
        num=int(input('For entering items, enter their serial number again please:'))
        y=int(input("Enter the number of items:"))
        for i in range (y):
            item=input('Enter the item:')
            def total():
                p=open("hello1.txt","wb")
                n=0
                for i in range(y):
                    price=int(input('Enter the price of items serially:'))
                    n+=price
                print("Your bill is a total amount of Rs.",n)
                t=[item,price]
                pickle.dump(t,p)
        total()
        k=input("Do u want to add items of any more customers?(yes/no)")
        p.close()

                    
def read():
    p=open("hello.txt","rb")
    while True:
        try:
            k=pickle.load(p)
            print("Name:",k[1],"Date:",k[2])
        except EOFError:
            p.close()
            break

def read1():
    p=open("hello1.txt","rb")
    while True:
        try:
            k=pickle.load(p)
            print("ITEM:",k[0],"PRICE:",k[1])
        except EOFError:
            p.close()
            break

        
def search():
    p=open("hello.txt","rb")
    r=int(input("Enter the serial number of the customer whose details you want to see:"))
    count=0
    while True:
        try:
            k=pickle.load(p)
            if k[0]==r:
                print("Name:",k[1])
                print("Date:",k[2])
                count=1
        except EOFError:
            p.close()
            break
    if(count==0):
        print("Record not found")

def append():
    p=open("hello.txt","ab")
    print('IF ANY MORE CUSTOMERS, PLEASE FEED THE DETAILS HERE:')
    k="yes"
    while k=="yes":
        num1=int(input("Enter the serial number: "))
        name1=input("Enter the name of the customer:")
        date1=(input("Enter the date:"))
        t=[num1,name1,date1]
        pickle.dump(t,p)
        k=input("Do u want to add more record(yes/no)")
    p.close()

def append1():
    p=open('hello1.txt','ab')
    k='yes'
    while k=="yes":
        num=int(input('For entering items of the left customers, enter their serial number again please:'))
        y=int(input("Enter the number of items:"))
        for i in range (y):
            item=input('Enter the item:')
            def total():
                p=open('hello1.txt','ab')
                n=0
                for i in range(y):
                    price=int(input('Enter the price of items serially:'))
                    n+=price
            print("Your bill is a total amount of Rs.",n)
            t=[item,price]
            pickle.dump(t,p)
        total()
        k=input("Do u want to add items of any more customers?(yes/no)")
        p.close()

def review():
    p=open('hello.txt','ab')
    s=input("Did you like our product?")
    t=input('How was our page?')
    u=int(input('Rate us out of 5?'))
    print("WE REALLY APPRECIATE YOUR FEEDBACK:)")
    p.close()
    
        
        
    
#Main Program

while True:
    print("$"*50, end=" ")
    print("||SUPERMARKET MANAGEMENT||",end=' ')
    print("$"*50, end=" ")
    print()
    print('''WELCOME TO MAIN MENU OF OUR PAGE

    1. ADD NEW CUSTOMERS
    2. ADD THE ITEMS PURCHASED BY THE CUSTOMERS AND GET THE BILL
    3. ADD NEW CUSTOMERS, IF ANY
    4. ADD THE ITEMS PURCHASED BY THE NEW CUSTOMERS AND GET THE BILL
    5. VIEW THE DETAILS OF THE CUSTOMERS
    6. VIEW THE ITEMS PURCHASED WITH PRICES
    7. SEARCH THE INFORMATION OF ANY CUSTOMER
    8. REVIEW OUR PRODUCTS AnD SERVICES
    9. EXIT''')

    try:
        c=int(input("ENTER YOUR CHOICE(1-8):"))
        if c==1:
            write()
        elif c==2:
            write1()
            total()
        elif c==3:
            append()
        elif c==4:
            append1()
        elif c==5:
            read()
        elif c==6:
            read1()
        elif c==7:
            search()
        elif c==8:
            review()
        elif c==9:
            break
        else:
            print(" PLEASE ENTER CORRECT CHOICE(1-8): ")
    except NameError:
        print("Input correct choice...(1-8)")