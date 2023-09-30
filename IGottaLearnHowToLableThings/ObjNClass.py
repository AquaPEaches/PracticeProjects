
class Dog(object):
    def __init__(self, name):
        self.name = name
    
    
    def speak(self):
        print(f'Hi i am {self.name}')


tim = Dog('Tim')
fred = Dog('Fred')