import random
import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Redhat1!",
  database="Banking"
)
cur = con.cursor()

class MyBank:
    bank_data={}
    balance_data={}
    def __init__(self):
        pass
    def create_account(self,name,balance):
        self.name=name
        self.balance=balance
        #self.acc_no=int('4321'+str(random.randrange(1000,9999)))
        cur.execute("INSERT INTO Bank (name, balance) VALUES (%s,%s)",(self.name,self.balance))
        con.commit()
        print("Account created successfully")
        #print("Hi "+self.name)
        #print("Your accont number is " + str(self.acc_no))
        cur.execute("SELECT * FROM Bank ORDER BY id DESC LIMIT 1")
        last_row=cur.fetchall()
        for item in last_row:
            self.acc_no = int(item[0])
            self.name = item[1]
            self.balance = int(item[2])
        print("Hi "+self.name)
        print("Your accont number is "+str(self.acc_no))
        self.bank_data[self.acc_no]=self.name
        self.balance_data[self.acc_no]=self.balance
    def get_account(self,acc_no):
        self.acc_no=acc_no
        cur.execute("SELECT * FROM Bank WHERE id = (%s)",(self.acc_no,))
        items = cur.fetchall()
        for item in items:
            self.acc_no = item[0]
            name = item[1]
            balance = item[2]
        print("Hi "+name)
        return balance
    def Update_Transactions(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
        cur.execute("UPDATE Bank SET balance = %s WHERE id = %s",(self.balance,self.acc_no))
        con.commit()
        print("Transaction Successful")
        self.balance_data[self.acc_no]=self.balance

class Transaction(MyBank):
    def deposit(self,acc_no):
        balance = self.get_account(acc_no)
        print("Your Balance = "+str(balance))
        Deposit_amt = int(input(" Enter the amount to be deposited = "))
        balance += Deposit_amt
        self.Update_Transactions(acc_no,balance)
        print("Your Balance = "+str(balance))

    def withdraw(self,acc_no):
        balance = self.get_account(acc_no)
        print("Your Balance = "+str(balance))
        Withdraw_amt = int(input(" Enter the amount to withdraw = "))
        balance -= Withdraw_amt
        self.Update_Transactions(acc_no,balance)
        print("Your Balance = "+str(balance))

print("""                   MyBank               
              Welcome, Greetings of the Day!     
1)create Account                            2)Withdraw
3)Deposit                                   4)Exit""")


#with con:
#    cur.execute("CREATE TABLE 'Bank' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 'name' TEXT(20), 'balance' INT)")
#print("Table Created")
#with con:
#    cur.execute("INSERT INTO 'Bank' ('id', 'name', 'balance') VALUES (4321001,'Admin',5000)")
#print("Admin details inserted")

customer = MyBank()
trans = Transaction()
flag='y'
while(flag=='y'):
    option = int(input("Please enter your option = "))
    if option == 1:
        name =raw_input("Enter your name = ")
        balance = int(input("Enter you Initial deposit = "))
        customer.create_account(name,balance)
    elif option == 2:
        acc_no=int(input("Enter Account number = "))
        trans.withdraw(acc_no)
    elif option == 3:
        acc_no=int(input("Enter Account number = "))
        trans.deposit(acc_no)
    elif option == 4:
        print("You will be directed to home page")
    else:
        print("Invalid input")
    print(""" To use bank services . Enter 'y' - continue     'n' - exit""")
    flag =raw_input("Do you want to continue = ")
