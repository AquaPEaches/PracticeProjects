

def quacks(obj):
    obj.quack()


class Duck: 
    
    def __init__(self, name):
        self.name = name
    def quack(self):
        print('Quack!')
class Car: 
  
    def __init__(self, model):
        self.model = model
    
    def quack(self):
        print('I can quack, too!')