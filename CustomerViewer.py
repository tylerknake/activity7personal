# NAME: Tyler Knake
# DATE: 12/5/2021
# COURSE: ISQA 3900 Web Application Development

import csv
from Customer import Customer

filename = 'customers.csv'
customers = []

# Goes through csv and puts customer objects in global list
def getCusts(csvFile):
    try:
        with open(csvFile, mode='r') as file:
            custCsv = csv.reader(file)
            next(custCsv)

            for line in custCsv:
                if line:
                    tempCust = Customer(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
                    customers.append(tempCust)
    except :
        print("%s could not be opened! Check file and try again!" %filename)
        exit(-1)

# Prints out the list of customer ids followed by names
def cust_names():
    print("ALL CUSTOMERS")
    print("-" * 25)
    for customer in customers:
        print("%s : %s"%(customer.cust_ID(), customer.cust_name()))

# Finds the customer when given the id or number
def getCustByNum(num):
    for cust in customers:
        thisNum = cust.cust_ID()
        if thisNum == num:
            return(cust)
            break
    return None

# main function
# Calls all other functions
def main():
    getCusts(filename)
    cust_names()
    print()
    print('Enter Customer ID: ')
    loopFlag1 = 1
    while loopFlag1 == 1:
        numIn = input()
        print()
        if not numIn.isnumeric():
            print("Please enter valid number: ", end = " ")
            continue
        cust = getCustByNum(numIn)
        if cust == None:
            print("Customer %s does not exist\n" %numIn)
        else:
            print(cust)
            print()
        while 1==1:
            ansIn = input('Would you like to continue? y/n: ')
            print()
            if ansIn == 'n':
                loopFlag1 = 0
                break
            elif ansIn == 'y':
                print('Enter Customer ID: ', end = " ")
                break
            else:
                continue

if __name__=="__main__":
    main()

# Run Program
main()