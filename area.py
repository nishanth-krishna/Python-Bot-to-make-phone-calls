class Area():
    def __init__(self,h=0,w=0,r=0):
        self.h = h
        self.w = w
        self.r = r

    
    def __str__(self):
        if self.r == 0 and self.h != 0 and self.w != 0:
            b = self.h * self.w
            return "area of the quadrilateral is : {}".format(b)
        elif self.h == 0 and self.w == 0 and self.r != 0:
            c = 3.14 * self.r * self.r 
            return "area of circle is : {}".format(c)


d = Area(0,0,5)
print(d)
