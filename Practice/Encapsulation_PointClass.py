#2차원 평면상의 점(point)을 표현하는 클래스 Point를 정의하라.
import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    def move(self, x, y):
        self.__x = x
        self.__y = y
    def reset(self):
        self.__x = 0.0
        self.__y = 0.0
    def distance(self, pt):
        x2 = math.pow(self.__x - pt.x, 2)
        y2 = math.pow(self.__y - pt.y, 2)
        return math.sqrt(x2+y2)

def main():
    p1 = Point()
    p2 = Point(1.0, 1.0)
    d = p1.distance(p2)
    print(f'distance between p1:({p1.x}, {p1.y}) and p2:({p2.x}, {p2.y}) ‐ {d:.4f}')
    p1.move(2.0, 3.0)
    p2.reset()
    d = p1.distance(p2)
    print(f'distance between p1:({p1.x}, {p1.y}) and p2:({p2.x}, {p2.y}) ‐ {d:.4f}')
    
main()