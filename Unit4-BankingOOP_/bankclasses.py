from datetime import datetime
import connect
class Customer:
    ''' Customer Class to initialize the customer '''
    cursorC = connect.sql_conn.cursor()
    def __init__(self,cid,name,addr, dob,cr_score):
        self.cid = cid
        self.name = name
        self.addr = addr
        self.dob = dob
        self.cr_score = cr_score
        #sql= 'Insert into dbo.customer values ({},{},{},{},{})'.format(cid,name,addr, dob,cr_score)
        sql= 'Insert into dbo.customer values (?,?,?,?,?)'
        Customer.cursorC.execute(sql,(cid,name,addr, dob,cr_score))
        connect.sql_conn.commit()
        print('Customer Created:'+self.cid)
    @classmethod
	''' create instances based on user input'''
    def from_input(cls):
        return cls(cid=input('cid'),name=input('cust_name:'),addr=input('address:'),dob=input('dob:'),cr_score=input('cr_score:'))
    def __repr__(self):
        return 'Customer {} created '.format(self.name)

class Employee:
    ''' Employee Class to initialize the employee '''
    cursorE = connect.sql_conn.cursor()
    def __init__(self,eid,ename,doj, spcl=None):
        self.eid = eid
        self.ename = ename
        self.doj = doj
        self.spcl = spcl #spcl = CC,Loan
        sql= 'Insert into dbo.employee values (?,?,?,?)'
        Employee.cursorE.execute(sql,(eid,ename,doj, str(spcl)))
        connect.sql_conn.commit()
        print('Employee Created:'+self.eid)
    @classmethod
	''' create instances based on user input'''
    def from_input(cls):
        return cls(eid=input('eid:'),ename=input('emp_name:'),doj=input('dt of joining:'),spcl=input('specialization(CC,Loan):'))
    def __repr__(self):
        return 'Employee {} created '.format(self.ename)

savings_rate=.01
current_rate=1.5
class BankAct:
    ''' BankAct Class to initialize the BankAct '''
    cursorA = connect.sql_conn.cursor()
    cursorA.execute('select aid from [Springboard].[dbo].[bank_account]')
    acct_list=cursorA.fetchall() #class variable to store accounts list of the customer
    cursorA.execute('select cid from [Springboard].[dbo].[customer]')
    cust_list=cursorA.fetchall()
    cursorA.execute('select eid from [Springboard].[dbo].[employee]')
    emp_list=cursorA.fetchall()
    def __init__(self,aid,cid,eid,type,bal=0):
        #Employee.__init__(self,eid)
        #Customer.__init__(self,cid)
        self.cid=cid
        self.eid=eid
        self.bal=bal
        self.ibal =bal
        self.aid=aid
        self.type=type
        self.acct_list.append(aid)
        self.createDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print('Account Created:'+self.aid)
        sql= 'Insert into dbo.bank_account(aid,cid,eid,type,bal,createDate) values (?,?,?,?,?,?)'
        BankAct.cursorA.execute(sql,(aid,cid,eid,type,bal,self.createDate))
        connect.sql_conn.commit()
    @classmethod
	''' create instances based on user input'''
    def from_input(cls):
        cursorA = connect.sql_conn.cursor()
        cursorA.execute('select aid from [Springboard].[dbo].[bank_account]')
        acct_list=[i[0] for i in cursorA.fetchall()] #class variable to store accounts list of the customer
        cursorA.execute('select cid from [Springboard].[dbo].[customer]')
        cust_list=[i[0] for i in cursorA.fetchall()]
        cursorA.execute('select eid from [Springboard].[dbo].[employee]')
        emp_list=[i[0] for i in cursorA.fetchall()]
        print(cust_list,emp_list)
        cid=int(input('cid:'))
        eid=int(input('eid:'))
        if (cid in cust_list) and (eid in emp_list):
            return cls(aid=input('aid:'),cid=cid,eid=eid,type=input('type of acct(CA,SA):'),bal=input('Balance:'))
        else:
            print('enter valid info')
    @staticmethod
    def withdraw(w_ano,w_amt):
        cursorA = connect.sql_conn.cursor()
        cursorA.execute('select bal from [Springboard].[dbo].[bank_account] where aid = ?',w_ano)
        bal = cursorA.fetchone()
        bal = float(bal[0])
        if float(w_amt)<=bal:#if bal is greater than equal to w_amt
            bal -=float(w_amt)
            print('New balance in account:'+w_ano + 'is ' +str(bal))
            sql= 'update dbo.bank_account set bal= ? where aid=?'
            BankAct.cursorA.execute(sql,(bal,w_ano))
            connect.sql_conn.commit()
        else:
            print('Insufficient Funds')
    @staticmethod
    def deposit(d_ano,d_amt):
        #if a_no exists for that customer??
        #if bal is greater than equal to w_amt
        cursorA = connect.sql_conn.cursor()
        cursorA.execute('select bal from [Springboard].[dbo].[bank_account] where aid = ?',d_ano)
        bal = cursorA.fetchone()
        bal = float(bal[0])
        print(bal)
        bal +=d_amt
        print('New balance in account:'+d_ano + ' is ' +str(bal))
        sql= 'update dbo.bank_account set bal= ? where aid=?'
        BankAct.cursorA.execute(sql,(bal,d_ano))
        connect.sql_conn.commit()
    @staticmethod
    def accountInfo(a_no):
        cursorA = connect.sql_conn.cursor()
        cursorA.execute('select type,bal, createDate,cid from [Springboard].[dbo].[bank_account] where aid = ?',a_no)
        type,bal, createDate,cid  = cursorA.fetchone()
        print('============\nAccount# ' , a_no, '\nAccountCurrentBalance: ', bal,
        '\nAccount Created on: '+str(createDate)+'\nCustomer# '+str(cid)+'\nAccountType# '+type+'\n============')
    
    @classmethod#class method as alternate constructor
	''' create instances based on user input'''
    def from_file(cls,line_str):
                aid,cid,eid,type,bal=line_str.split(',')
                return cls(aid,int(cid),int(eid),type,int(bal))

    @classmethod#class method to change interest rates
    def change_rate(cls,typ,new_rate):
        if typ == 'savings':
            cls.savings_rate=new_rate
        else:
            cls.current_rate = new_rate

    def apply_intrest(self,acct):
        if acct in self.acct_list:
            if self.type == 'savings':
                self.bal*=(savings_rate+1)
                
            else:
                self.bal*=current_rate
        else:
            print ('account doesnt exist')
        print('new balance :' +str(self.bal))

    def __add__(self,other):
        print (self.bal+other.bal)

class CreditAccount(BankAct):
    def __init__(self,aid,cid,eid,type,bal,cc_int):
        BankAct.__init__(aid,cid,eid,type,bal)
        self.cc_int=cc_int
    @classmethod
	''' create instances based on user input'''
    def from_input(cls):
        cursorA = connect.sql_conn.cursor()
        cursorA.execute('select aid from [Springboard].[dbo].[bank_account]')
        acct_list=[i[0] for i in cursorA.fetchall()] #class variable to store accounts list of the customer
        cursorA.execute('select cid from [Springboard].[dbo].[customer]')
        cust_list=[i[0] for i in cursorA.fetchall()]
        cursorA.execute('select eid from [Springboard].[dbo].[employee]')
        emp_list=[i[0] for i in cursorA.fetchall()]
        print(cust_list,emp_list)
        cid=int(input('cid:'))
        eid=int(input('eid:'))
        if (cid in cust_list) and (eid in emp_list):
            return cls(aid=input('aid:'),cid=cid,eid=eid,type=input('type of acct(CCA):'),bal=input('Balance:'),int= input('interestRate'))
        else:
            print('enter valid info')
        
class LoanAccount(BankAct):
    def __init__(self,aid,cid,eid,type,bal,loan_int=.005,term=10):
        self.loan_int=loan_int
        self.term = term
        BankAct.__init__(aid,cid,eid,type,bal)

    @classmethod
	''' create instances based on user input'''
    def from_input(cls):
        cursorA = connect.sql_conn.cursor()
        cursorA.execute('select aid from [Springboard].[dbo].[bank_account]')
        acct_list=[i[0] for i in cursorA.fetchall()] #class variable to store accounts list of the customer
        cursorA.execute('select cid from [Springboard].[dbo].[customer]')
        cust_list=[i[0] for i in cursorA.fetchall()]
        cursorA.execute('select eid from [Springboard].[dbo].[employee]')
        emp_list=[i[0] for i in cursorA.fetchall()]
        print(cust_list,emp_list)
        cid=int(input('cid:'))
        eid=int(input('eid:'))
        if (cid in cust_list) and (eid in emp_list):
            return cls(aid=input('aid:'),cid=cid,eid=eid,type=input('type of acct(LA):'),bal=input('Balance:'),intr= input('loanRate:'),term=input('term:'))
        else:
            print('enter valid info')


