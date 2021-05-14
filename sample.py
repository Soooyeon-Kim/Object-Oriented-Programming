# 9주차 2차시
# 산술 연산자 오버로딩
class SampleClass:
    def __init__ (self, value):
        self.value =value

    def __add__(self, another):
        result = self.value + another.value
        return SampleClass(result)

    def __str__(self):
        return f'value is: {self.value}'

if __name__== '__main__':
    obj1 = SampleClass(10)
    obj2 = SampleClass(20)
    obj3 = obj1 + obj2
    print(obj3)

