# write a python script to create a class rectangle with datamember 
# length and width and method area and parimeter which can compute 
# area and parimeter of the rectangle

class rectangle:
    def __init__(self,length,width) -> None:
        self.length=length
        self.width=width
    
    def area(self):
        return self.width*self.length
    
    def perimeter(self):
        return (self.width+self.length)*2
    
r=rectangle(54,23)
print(r.area())
print(r.perimeter())
