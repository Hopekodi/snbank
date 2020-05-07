
import json
import random
import os
import sys
details={}

details['staff']=[]

details['staff'].append( {
    'username':'promise',
    'password':'1234',
    'email':'pro@gmail.com',
    'fullname':'promise orevaoghene'
})
details['staff'].append( {
    'username':'hopey',
    'password':'1234',
    'email':'okelue@gmail.com',
    'fullname':'Okelue Hope'
})
username=[]
password=[]
with open('staff.txt','w') as output:
    json.dump(details, output)

with open('staff.txt') as json_file:
    data= json.load(json_file)
    for x in data['staff']:
        username.append(x['username'])
        password.append(x['password'])
    option = input("1. Staff Login\n2. Exit\n")

    if (option == "1"):
        while (True):
            user = input("Username: ")
            psw = input("Password: ")

            if (user in username and psw in password):
                session=[user,psw]
                open('session.txt','w')
                while(True):
                    option2 = input("1. Create New Bank Account\n2. Check Account Details\n3. Logout\n")

                    if(option2=="1"):
                        accountName = input("Account name: ")
                        balance = input("Opening Balance: ")
                        accountType = input("Account Type: ")
                        accountEmail = input("Account email: ")
                        accountNo = random.randint(0000000000,9999999999)

                        data = {}

                        data['account'] = []

                        data['account'].append({
                            'accountName': accountName,
                            'balance': balance,
                            'accountType': accountType,
                            'accountEmail': accountEmail,
                            'accountNo':accountNo
                        })
                        print("Account Created: "+ str(accountNo))
                        with open('customer.txt', 'w') as output:
                            json.dump(data, output)
                        continue


                    elif(option2=="2"):
                        with open('customer.txt') as json_file:
                            data = json.load(json_file)
                            accno=input("Enter Account Number: ")
                            for y in data['account']:
                                accN =y['accountNo']
                            if(int(accno)==accN):
                                for x in data['account']:
                                    print("accountName: "+x['accountName'])
                                    print("balance: " + x['balance'])
                                    print("Type: " + x['accountType'])
                                    print("Email: " + x['accountEmail'])
                                    print("Account No: " + str(x['accountNo'])+"\n")
                            else:
                                print("Account No does not exists\n")
                        continue
                    elif(option2 == "3"):
                        print("Logged Out")
                        os.remove("session.txt")
                        break
                    else:
                        continue
            else:
                print("Wrong Username or Password")
                continue


    elif(option=="2"):
        print("Application Closing")
        sys.exit()
    else:
        sys.exit()
