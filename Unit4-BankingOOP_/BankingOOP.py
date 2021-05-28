from datetime import datetime
import connect

#parent class
class Customer:
    ''' Customer Class to initialize the customer '''
    cursorC = sql_conn.cursor()
    def __init__(self,cid,name,addr, dob,cr_score):
        self.cid = cid
        self.name = name
        self.addr = addr
        self.dob = dob
        self.cr_score = cr_score
        #sql= 'Insert into dbo.customer values ({},{},{},{},{})'.format(cid,name,addr, dob,cr_score)
        sql= 'Insert into dbo.customer values (?,?,?,?,?)'
        Customer.cursorC.execute(sql,(cid,name,addr, dob,cr_score))
        sql_conn.commit()
    def __repr__(self):
        return 'Customer {} created '.format(self.name)   
        
    
#parent class
class Employee:
    ''' Employee Class to initialize the employee '''
    cursorE = sql_conn.cursor()
    def __init__(self,eid,ename,doj, spcl=None):
        self.eid = eid
        self.ename = ename
        self.doj = doj
        self.spcl = spcl #spcl = CC,Loan
        sql= 'Insert into dbo.employee values (?,?,?,?)'
        Employee.cursorE.execute(sql,(eid,ename,doj, str(spcl)))
        sql_conn.commit()
    def __repr__(self):
        return 'Employee {} created '.format(self.ename)

#child class
savings_rate=.01
current_rate=1.5
class BankAct(Customer,Employee):
    ''' BankAct Class to initialize the BankAct '''
    cursorA = sql_conn.cursor()
    acct_list=[] #class variable to store accounts list of the customer    
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
        sql= 'Insert into dbo.bank_account values (?,?,?,?,?,?)'
        BankAct.cursorA.execute(sql,(aid,cid,eid,type,bal,self.createDate))
        sql_conn.commit()
    def withdraw(self,w_amt):
        a_no=input('Enter accnt Number you would like to withdraw:'+str(w_amt)+' :')
        #if a_no exists for that customer??
        if a_no in self.acct_list:
            if w_amt<=self.bal:#if bal is greater than equal to w_amt
                self.bal -=w_amt
                print('New balance in account:'+self.aid + 'is ' +str(self.bal))
                sql= 'update dbo.bank_account set bal= ? where aid=?'
                BankAct.cursorA.execute(sql,(self.bal,self.aid))
                sql_conn.commit()
            else:
                print('Insufficient Funds')
        else:
            print(a_no + ' doesnt exist for customer '+str(self.cid))
    #@classmethod
    def deposit(self,d_amt):
        a_no=input('Enter accnt Number you would like to deposit '+str(d_amt)+' :')
        #if a_no exists for that customer??
        #if bal is greater than equal to w_amt
        if a_no in self.acct_list:
            self.bal +=d_amt
            print('New balance in account:'+self.aid + ' is ' +str(self.bal))
            sql= 'update dbo.bank_account set bal= ? where aid=?'
            BankAct.cursorA.execute(sql,(self.bal,self.aid))
            sql_conn.commit()
        else:
            print(a_no + ' doesnt exist for customer '+str(self.cid))
        
    
    def accountInfo(self):
        print('============\nAccount# ' , self.aid, '\nAccountCurrentBalance: ', self.bal,'\nAccountInitialBalance: ', self.ibal,
        '\nAccount Created on: '+str(self.createDate)+'\nCustomer# '+str(self.cid)+'\n============')
    
    @classmethod#class method as alternate constructor
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


    
#how to create instance for customer , Employee class?
#getter setter?
#use Exception
#@classmethod, instancemethod, static method
#logging
#DB Cnnections
#_sstr,_repr
#if __name__ == '__main__':
#readme File
#UML
#Unit Testing - https://medium.com/@gurupratap.matharu/object-oriented-programming-project-in-python-for-your-github-portfolio-d34feaf1332c


    
c1=Customer(1,'Sam','156 Rex Lane', '2-2-1984',750)
c2=Customer(2,'Mike','120 Buck Lane', '2-2-1984',600)
c3=Customer(3,'Jen','10 Lincoln Dr', '2-2-1984',500)
c4=Customer(4,'Tucker','80 Main st', '2-2-1984',800)
c5=Customer(5,'Lindsey','99 River Dr', '2-2-1984',900)
e1=Employee(1,'John','1-5-2019',['Loan'])
e2=Employee(2,'Rahul','7-5-2018',['cc','loan'])
e3=Employee(3,'Cheryl','11-15-2019',['cc'])
e4=Employee(4,'Mary','4-1-2021')
#print statements
a1=BankAct('a1',1,2,'savings')
#a2=BankAct('a2',1,3,'current')
#print(a1.eid)# how can I print the account's customer's attibute(dob)
#print(a1.accountInfo())
#a1.withdraw(500)
a1.deposit(500)
#a2.deposit(700)
#print(c1)
#print(a1+a2)
print(a1.accountInfo())
#a1.apply_intrest('a1')
#BankAct.change_rate('savings',.02)
#a1.apply_intrest('a1')

with open(r"C:\Users\samy8\Desktop\Work Lab\SpringBoard\python\acct.csv",'r') as f:
            for line in f:
                BankAct.from_file(line)

#a3.deposit(700)

#how do I access objects variables  

