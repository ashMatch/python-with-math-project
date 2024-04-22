class AreaMath:

    def __init__(self, base = 0, high = 0, bigger_base = 0, radius = 0, PI = 3.14):
        self.base = base
        self.high = high
        self.bigger_base = bigger_base
        self.radius =radius
        self.PI = PI
    
    def triangle_math(self):
        area =self.base*self.high/2
        return "A = %.1f" %(area)
    
    def rectangle_math(self):
        area =self.base*self.high
        return "A = %.1f" %(area)
    
    def square_math(self):
        area =self.base*self.base
        return "A = %.1f" %(area)
    
    def circle_math(self):
        area = self.PI*self.radius**2
        return "A = %.1f" %(area)
    
    def trapezoid_math(self):
        area = (self.base+self.bigger_base/2)*self.high
        return "A = %.1f" % (area)