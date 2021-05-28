#connect
#import all classes
#print a welcome message and ask what you want to do - 
	#cust login - options:create new acct(S,C), check balance, deposit or withdraw, Loans or Credit card 
	#emp login - create new emps, cust
#
#

import bankclasses
t = input('Welcome to our Bank! \nDo you want to create a new Employee(E), a new Customer(C) or a new account(NA) or work on an existing account(EA) or additional services(S)?')
if t == 'E':
	bankclasses.Employee.from_input()
if t == 'C':
	bankclasses.Customer.from_input()
if t == 'NA':
	bankclasses.BankAct.from_input()
	
if t == 'EA':
	a = input('Enter Account ID: ')
	t1= input('Please select from below services - \n1)Check Balance\n2)Deposit Fund\n3)Withdraw fund\n')
	if t1 == '1':
		bankclasses.BankAct.accountInfo(a)
	if t1 == '2':
		d=float(input('deposit_amt'))
		bankclasses.BankAct.deposit(a,d)
	if t1 == '3':
		w=input('withdraw_amt')
		bankclasses.BankAct.withdraw(a,w)
if t == 'S':
	s=input('Do you want to open a loan account(LA) or credit card account(CCA)?')
	if s == 'LA':
		bankclasses.LoanAccount.from_input()
	if s == 'CCA':
		bankclasses.CreditAccount.from_input()

