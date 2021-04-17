class Employee():
    def __init__(self, name, age, sal):
        self.name,self.age,self.sal = name,age,sal
    def raise_sal(self,amt):
        self.sal=self.sal+amt
        return self.sal
class Manager(Employee):    
    def __init__(self, name, age, sal,Emps=None):
        Employee.__init__(self,name, age, sal)
        self.Emps = ['d1','t1','d2']
    def raise_sal(self,amt):
        #self.sal=self.sal+amt +100
        self.sal=Employee.raise_sal(self,amt)
        return self.sal

M1=Manager('sam',40,2000)
print(M1.Emps,M1.sal,M1.raise_sal(100))
