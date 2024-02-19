import mysql.connector as sql
connector = sql.connect(host='127.0.0.1',user='root',password='',database = "ayo_db")
myCursor = connector.cursor()
# myCursor.execute("CREATE DATABASE ayo_db")

# myCursor.execute("SHOW DATABASES")
# for base in myCursor:
#     print(base)

# myCursor.execute("CREATE TABLE customer_table(id INT(4) AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(50), email VARCHAR(50) UNIQUE KEY, account_number VARCHAR(10) UNIQUE KEY, account_balance FLOAT(50), username VARCHAR(15) UNIQUE KEY, password INT(4))")

# myCursor.execute("ALTER TABLE customer_table ADD date_joined DATETIME DEFAULT current_timestamp")

# myCursor.execute("SHOW TABLE")
# for bt in myCursor:
#     print(bt)

# myCursor.execute("DROP TABLE staff_table")

import pwinput as pw       
import random as rd
import time
import re

sleep = time.sleep(2)
def dashboard():
    print("""
          Welcome to Ayomide Bank App\n
          1.Signup
          2.Login
          3.Exit
    """)
    user = int(input("Option: ").strip())
    if user == 1:
        signup()
        sleep
        dashboard()
    elif user == 2:
        login()
        sleep
        dashboard()
    elif user == 3:
        sleep
        exit()
    else:
        sleep
        print("Incorrect number,Try again!!")
        dashboard()

def check_for_email(Email):
    pattern = r"^\w+@\w+\.\w+$"
    matches = re.match(pattern,Email)
    if matches:
        print("Valid email")
        account_no = rd.randint(9000000000,9099999999)
        account_bal = 0
        username = input("Username: ").strip()
        password = pw.pwinput(mask="-")
        info = "INSERT INTO customer_table(fullname, email, account_number, account_balance, username, password) VALUES(%s,%s,%s,%s,%s,%s)"
        val = (fullname,email,account_no,account_bal,username,password)
        myCursor.execute(info,val)
        connector.commit()
        print(f"{myCursor.rowcount} account inserted successfully and your account number is {account_no}")
    else:
        not_match()


def not_match():
        print(f"Invalid email")
        print('''
         1.sign up
         00.Exit
        ''')
        user = int(input(("Option:")))
        if user==1:
           signup()
        elif user==00:
            exit()

def signup():
    global fullname
    global email
    fullname = input("Enter your fullname: ").strip()
    email = input("Email: ").strip()
    check_for_email(email)

def login(): 
    global detail
    global customer
    global bal
    global inp_username
    global inp_password
    inp_username = input("Username: ").strip()
    inp_password =  pw.pwinput(mask="-")
    query = ("SELECT fullname, account_number, account_balance FROM customer_table WHERE username = %s AND password = %s")
    val = (inp_username,inp_password)
    myCursor.execute(query,val)
    detail= myCursor.fetchone()
    customer = detail[0]
    bal = detail[2]

    if detail:
        print("Access granted")
        landing_page()
    else:
        print("Invalid login details.Try again! ")
        login()

def  landing_page():
    pass
    print(f"""
        Name: {customer}
        Available balance: ${bal} 

        1.Deposit            2.Withdraw
        3.Transfer           4.Buy Airtime 
        5.Buy Data           6.Check balance
        7.Exit
  
       """)
    user = int(input("Option: ").strip())
    if user== 1:
        deposit()
    elif user == 2:
        withdraw()
    elif user == 3:
        transfer()
    elif user == 4:
        airtime()
    elif user == 5:
        data()
    elif user == 6:
        amount()
    elif user == 7:
        exit()
    else:
        print("Enter the correct number")
        landing_page()

def deposit():
    sleep
    print("""
    1. 1000          2. 5000
    3. 10000         4. 50000
    5. Other         6. Exit
     """)
    user = int(input("Option: ").strip())
    global new_bal
    if user == 1:
        new_bal = bal + 1000
        query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
        val = (new_bal,inp_username,inp_password)
        myCursor.execute(query,val)
        transaction = ("UPDATE transaction_table SET account_balance = %s AND amount = %s WHERE transaction_id = %s")
        val2=(new_bal,1000,1)
        myCursor.execute(transaction,val2)
        connector.commit()
        print(f"Deposited ${1000}. Current balance: ${new_bal}")
    elif user == 2:
        new_bal = bal + 5000
        query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
        val = (new_bal,inp_username,inp_password)
        myCursor.execute(query,val)
        connector.commit()
        print(f"Deposited ${5000}. Current balance: ${new_bal}")
    elif user == 3:
        new_bal = bal + 10000
        query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
        val = (new_bal,inp_username,inp_password)
        myCursor.execute(query,val)
        connector.commit()
        print(f"Deposited ${10000}. Current balance: ${new_bal}")
    elif user == 4:
        new_bal = bal + 50000
        query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
        val = (new_bal,inp_username,inp_password)
        myCursor.execute(query,val)
        connector.commit()
        print(f"Deposited ${50000}. Current balance: ${new_bal}")
    elif user == 5:
        depot = float(input("Amount: "))
        new_bal = bal + depot
        query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
        val = (new_bal,inp_username,inp_password)
        myCursor.execute(query,val)
        connector.commit()
        print(f"Deposited ${depot}. Current balance: ${new_bal}")
    elif user == 6:
        exit()
    else:
        print("Incorrect number,Try Again!!!")
        deposit()

def withdraw():
    sleep
    print("""
    1. 1000          2. 5000
    3. 10000         4. 50000
    5. Other         6. Exit
     """)
    user = int(input("Option: ").strip())
    if user == 1:
        if bal >= 1000:
            new_bal = bal - 1000
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"Withdrew ${1000}. Current balance: ${new_bal}")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 2:
        if bal >= 5000:
            new_bal = bal - 5000
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"Withdrew ${5000}. Current balance: ${new_bal}")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 3:
        if bal >= 10000:
            new_bal = bal - 10000
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"Withdrew ${10000}. Current balance: ${new_bal}")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 4:
        if bal >= 50000:
            new_bal = bal - 50000
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"Withdrew ${50000}. Current balance: ${new_bal}")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 5:
        if bal >= depot:
            depot = float(input("Amount: "))
            new_bal = bal - depot
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"Withdrew ${depot}. Current balance: ${new_bal}")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 6:
        exit()
    else:
        print("Incorrect number,Try Again!!!")
        withdraw()

def airtime():
    sleep
    print("""
    1. 100           2. 200
    3. 500           4. 1000
    5. Other         6. Exit
     """)
    user = int(input("Option: ").strip())
    if user == 1:
        if bal >= 100:
            new_bal = bal - 100
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"You have successfully buy $100 airtime")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 2:
        if bal >= 200:
            new_bal = bal - 200
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"You have successfully buy $200 airtime")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 3:
        if bal >= 500:
            new_bal = bal - 500
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"You have successfully buy $500 airtime")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 4:
        if bal >= 1000:
            new_bal = bal - 1000
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"You have successfully buy $1000 airtime")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 5:
        if bal >= depot:
            depot = float(input("Amount: "))
            new_bal = bal - depot
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            connector.commit()
            print(f"You have successfully buy ${depot} airtime")
        else:
            sleep
            print(f"Insufficient balance, your account balance is ${bal}")
    elif user == 6:
        exit()
    else:
        print("Incorrect number,Try Again!!!")
        airtime() 

def amount():
    print(f"Your available balance is ${bal}")
    sleep
    landing_page()

def data():
    sleep
    print("""
    1. Daily          2. Weekly
    3. Monthly        4. 2-Months
    5. Yearly         6. Exit
      """)
    user = int(input("Option: ").strip())
    if user == 1:
        time.sleep(1)
        print("""
          1.100mb ($100)           2.1gb ($350)
          3.3gb  ($800)            4.Cancel
            """)
        user2 = int(input("Option: ").strip())
        if user2 == 1:
            if bal >= 100:
                new_bal = bal - 100
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 2:
            if bal >= 350:
                new_bal = bal - 350
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 3:
            if bal >= 800:
                new_bal = bal - 800
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 4:
            exit()
        else:
            data()
    elif user == 2:
        time.sleep(1)
        print("""
          1.1gb ($500)              2.5gb ($1500)
          3.7gb  ($2000)            4.Cancel
            """)
        user2 = int(input("Option: ").strip())
        if user2 == 1:
            if bal >= 500:
                new_bal = bal - 500
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 2:
            if bal >= 1500:
                new_bal = bal - 1500
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 3:
            if bal >= 2000:
                new_bal = bal - 2000
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 4:
            exit()
        else:
            data()
    elif user == 3:
        time.sleep(1)
        print("""
          1.3gb ($1500)              2.6gb ($3000)
          3.20gb  ($5500)            4.Cancel
            """)
        user2 = int(input("Option: ").strip())
        if user2 == 1:
            if bal >= 1500:
                new_bal = bal - 1500
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 2:
            if bal >= 3000:
                new_bal = bal - 3000
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 3:
            if bal >= 5500:
                new_bal = bal - 5500
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 4:
            exit()
        else:
            data()
    elif user == 4:
        time.sleep(1)
        print("""
          1.100gb ($20000)             2.160gb ($30000)
          3.200gb  ($50000)            4.Cancel
            """)
        user2 = int(input("Option: ").strip())
        if user2 == 1:
            if bal >= 20000:
                new_bal = bal - 20000
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 2:
            if bal >= 30000:
                new_bal = bal - 30000
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 3:
            if bal >= 50000:
                new_bal = bal - 50000
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 4:
            exit()
        else:
            data()
    elif user == 5:
        time.sleep(1)
        print("""
          1. 1TB    ($100000)              2. 2.5TB ($250000)
          3. 4.5TB  ($450000)            4.Cancel
            """)
        user2 = int(input("Option: ").strip())
        if user2 == 1:
            if bal >= 100000:
                new_bal = bal - 100000
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 2:
            if bal >= 250000:
                new_bal = bal - 250000
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 3:
            if bal >=450000:
                new_bal = bal - 450000
                query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password = %s")
                val = (new_bal,inp_username,inp_password)
                myCursor.execute(query,val)
                connector.commit()
                print(f"Your balance is ${new_bal}")
            else:
                time.sleep(1)
                print(f"Insufficient balance, your account balance is ${bal}")
        elif user2 == 4:
            exit()
        else:
            data()

def transfer():
    time.sleep(1)
    print("""
     1. To Ayomide Bankapp
     2. Exit
""")
    user = int(input("Option: ").strip())
    if user == 1:
        query = ("SELECT account_balance FROM customer_table WHERE username = %s AND password = %s")
        val = (inp_username,inp_password)
        myCursor.execute(query,val)
        detail= myCursor.fetchone()
        bal = detail[0]
        trans = float(input("Enter the amount you want to transfer: ").strip())
        if bal < trans:
            print("Insufficient balance")
        else:
            customer_username = input("Username: ").strip()
            customer_acct_no = input("Account number: ").strip()
            query = ("SELECT account_balance FROM customer_table WHERE username = %s AND account_number = %s")
            val = (customer_username,customer_acct_no)
            myCursor.execute(query,val)
            customer_detail= myCursor.fetchone()
            customer_bal = customer_detail[0]
            New_bal = customer_bal + trans
            new_bal=bal-trans
            print("Transfer successful")
            query = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND password =%s")
            val = (new_bal,inp_username,inp_password)
            myCursor.execute(query,val)
            query_cus = ("UPDATE customer_table SET account_balance = %s WHERE username = %s AND account_number =%s")
            val_cus = (New_bal,customer_username,customer_acct_no)
            myCursor.execute(query_cus,val_cus)
            connector.commit()
            print(f"Transferred ${trans}. Current balance: ${new_bal}")

            
dashboard()
            
# myCursor.execute("CREATE TABLE Transaction_table(transaction_id INT(4) AUTO_INCREMENT PRIMARY KEY, amount FLOAT(50), account_balance FLOAT(50), date_joined DATETIME DEFAULT current_timestamp )")