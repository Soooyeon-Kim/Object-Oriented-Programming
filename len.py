class Order:
    def __init__(self, cart, customer):
        self.cart =list(cart)
        self.customer = customer


    def __len__(self):
        return self.cart

if __name__== '__main_-':
    order = Order(['banana', 'apple', 'mango'],'Real Python'
                  print(len(order)))