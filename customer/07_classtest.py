# class Cookie:
#     pass

# a=Cookie()
# b=Cookie()

# print(a)
# print(id(a))
# print(type(a))


# print(b)
# print(id(b))
# print(type(b))

class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second



    def setdata(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        result= self.first + self.second
        return result
    
    def sub(self):
        result= self.first - self.second
        return result
    
    def nnum(self):
        result= self.first % self.second
        return result
    
 
        

# a=FourCal()
# a.setdata(2,3)
# print(a.add())

class flower(FourCal):
    def div(self)

b=flower(4,0)
b.add()




