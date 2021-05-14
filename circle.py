# 9주차 2차시
# 비교 연산자 오버로딩
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def __gt__(self, another):
        return self.radius > another.radius

    def __lt__(self, another):
        return self.radius > another.radius

    def __str__(self):
        return f'Circle with radius {self.radius}'

if __name__ == '__main__':
    c1 = Circle(4)
    c2 = Circle(5)

    print(c1 > c2)
    # c1, c2이 갖고 있는 메소드를 호출하여 연산한다
    
