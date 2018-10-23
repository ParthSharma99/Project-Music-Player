#Q1----------------------------------------------------------------------------
'''
class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calculate(self,x):
        y = self.a*(x**2) + self.b*x + self.c
        print (y)

    def roots(self):
        d = self.b**2 - 4*self.a*self.c

        if d<0:
            print ("No roots")

        elif d>0:
            r1 = (-self.b + (d)**(1/2))/2*self.a
            r2 = (-self.b - (d)**(1/2))/2*self.a
            print ("Roots are: ",r1," and ",r2)

        elif d==0:
            r = -self.b/2*self.a
            print ("Only one root that is: ",r)

l = Quadratic(1,-2,1)
l.calculate(2)
l.roots()

m =Quadratic(2,2,4)
m.calculate(2)
m.roots()

#Q2----------------------------------------------------------------------------

class Numeric:
    def __init__(self):
        self.n = 1

    def getData(self):
        try:
            self.n = input("Enter number: ")
        except ValueError:
           print("That's not an integer!")

    def count(self):
        l = len(str(self.n))
        print ("Count of digits in n is : ",l)

    def show(self):
        l = len(str(self.n))
        temp = self.n
        temp1 =[]
        for i in range(l):
            temp2 = temp%10
            temp = int((temp-temp2)/10)
            temp2 = temp2*(10**i)
            temp1.append(str(temp2))

        temp3=str(self.n) + ' = '
        for i in range(1,l+1):
            if i!=l:
                temp3 += temp1[-i]+' + '
            elif i==l:
                temp3 += temp1[-i]

        return temp3
    def reverse(self):
        tr = len(str(self.n))
        n_tr=[]
        for i in range(tr):
            n_tr += str(self.n)[i]
        n_tr.reverse()
        n_tr2=''
        for i in range(tr):
            n_tr2 += n_tr[i]
        return int(n_tr2)

    def hasdigit(self,x):

        lis = str(self.n)
        for i in lis:
            print (i)
            if x==i:
                count=1
        if count==1:
            temp =True
        return temp

main = Numeric()
main.getData()
main.count()
print (main.show())
print (main.reverse())
print (main.hasdigit(2))

#Q3----------------------------------------------------------------------------

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def set_location(self,a,b):
        self.x = a
        self.y =b

    def distance_from_original(self):
        dist = (self.x**2 + self.y**2)**(0.5)
        return dist
    def distance_between(self,point):
        a,b = point
        dist = ((self.x-a)**2 + (self.y-b)**2)**(0.5)
        return dist
    def __str__(self):
        n = 0
        if self.x>0 and self.y>0:
            n=1

        elif self.x<0 and self.y>0:
            n=2
        elif self.x<0 and self.y<0:
            n=3
        elif self.x>0 and self.y<0:
            n=4

        return "A point A(",self.x,self.y,") lies in quadrant ",n
main = Point()
main.set_location(3,4)
print (main.distance_from_original())
print (main.distance_between((2,3)))

#Q4----------------------------------------------------------------------------
class Mylist:
    def __init__(self):
        self.num=[]

    def getlist(self):
        val = True
        while val:
            val = int(input("Enter value: "))
            if val==0:

                break
            self.num.append(val)

    def printlist(self):
        print (self.num)
    def is_member(self,x):
        if x in self.num:
            return True

    def maxmin_in_list(self):
        m1 = max(self.num)
        m2 = min(self.num)
        return m1-m2
    def closest_to(self,v):
        self.num.sort()
        print (self.num)
        l =len(self.num)
        i=0
        while i<l:
            if self.num[i]==v:
                i='go'
                break
            elif self.num[i]<v:
                i+=1
            elif self.num[i]>v:
                break
        if i=='go':
            return v

        elif ( v -self.num[i-1]) < (self.num[i] - v ):
            return self.num[i-1]

        elif (v-self.num[i-1]) > (self.num[i]-v):
            return self.num[i]
main = Mylist()
main.getlist()
print (main.is_member(2))
print (main.maxmin_in_list())
print (main.closest_to(4))

#Q5---------------------------------------------------------------------------
class PerfectNo:
    def __init__(self,num):
        self.factor = []
        self.n =num

    def Genfactors(self):
        self.factor.append(1)
        for i in range(2,self.n):
            if self.n%i==0:
                self.factor.append(i)

    def IsPerfectNo(self):
        s = 0
        for i in self.factor:
            s+=i
        if s==self.n:
            return True
        else:
            return False

    def IsPrimeNo(self):
        if self.n!=1:
            if len(self.factor)==1:
                return True
            else:
                return False
        else:
            return "Neither Prime nor composite"
    def __str__(self):
        if IsPrimeNo:
            if IsPerfectNo:
                print (self.n),' = ',self.factor,' is a Perfect number and a prime number.'
            else:
                print (self.n),' = ',self.factor,' is not a Perfect number but a prime number.'
        else:
            if IsPerfectNo:
                print (self.n),' = ',self.factor,' is a Perfect number and not a prime number.'
            else:
                print (self.n),' = ',self.factor,' is not a Perfect number and not a prime number.'

main = PerfectNo(28)
main.Genfactors()
print (main.IsPerfectNo(),'   ',main.IsPrimeNo())
'''
#Q6---------------------------------------------------------------------------


class Matrix:
    def __init__(self,X,Y):
        temp=[]
        for i in range(X):
            for j in range(Y):
                temp1 = []
                a = int(input("Enter Number: "))
                temp1.append(a)
            temp.append(temp1)
        self.row = X
        self.column = Y
        self.mat = temp

    def display(self):
        for i in range(self.row):
            print (self.mat[i])

    def Diasgsum(self):
        if self.row==self.column:
            s1=0
            s2=0
            for i in range(self.row):
                for j in range(self.column):
                    if i==j:
                        s1+=self.mat[]



















