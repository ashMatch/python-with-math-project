class AreaMath:
    def __init__(self, base, high, bigger_base = 0, radius = 0, PI = 3.14):
        self.base = base
        self.high = high
        self.radius =radius
        self.bigger_base = bigger_base
    
    def triangle_math(self):
        print("A = BasexAltura/2²")
        area =self.base*self.high/2
        return "A = %.1f" %(area)
    
    def rectangle_math(self):
        area =self.base*self.high
        return "A = %.1f" %(area)
    
    def square_math(self):
        area =self.base*self.high
        return "A = %.1f" %(area)
    
    def circle_math(self):
        area =self.base*self.high
        return "A = %.1f" %(area)