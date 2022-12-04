from Restaurant1 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):#如何继承父类，注意此处格式
        super().__init__(restaurant_name,cuisine_type)#注意继承格式
        self.name = restaurant_name#继承了父类的restaurant_name,cuisine_type
        self.type = cuisine_type
        self.flavour =['orange','lemon','watermolon']
    def show(self):
        for fla in self.flavour:
            print(fla)




ice_store1 = IceCreamStand('MIXUEBINGCHENG','guocha')
ice_store1.show()
