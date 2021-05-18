class MenuItem:
    # 음식 메뉴를 나타내는 클래스
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return "{} 케이크 가격: {}".format(self.name,self.price)

# 메뉴 인스턴스 생성
carrot = MenuItem("당근", 6500)
strawberry = MenuItem("딸기 생크림", 5400)
cheese = MenuItem("뉴욕 치즈", 5700)

# 메뉴 인스턴스 출력
print(carrot)
print(strawberry)
print(cheese)