import math
class Circle:
    r = None
    def get_area(self,radius):
        self.r=radius
        area = math.pi*(self.r**2)
        return round(area,2)

    def get_perimeter(self,radius):
        self.r=radius
        perimeter = 2*math.pi*self.r
        return round(perimeter,2)

if __name__=="__main__":
    circle=Circle()
    print(circle.get_area(float(input("输入想要计算面积的半径"))))
    print(circle.get_perimeter(float(input("请输入想要求周长的半径"))))