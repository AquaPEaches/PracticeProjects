#poly-mophism is changing a form into another form


class French:
    def say_hello(self):
        print("Bonjour")
        
class Chinese:
    def say_hello(self):
        print('Ni hou')

def intro(lang):
    #lang is assigned to say hello function
    lang.say_hello()

sarthak = French()
Jhon = Chinese()

intro(sarthak)
intro(Jhon)


