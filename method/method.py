import random

class ContactMethod:
    def sell(self):
        methods = ['электронной почты', 'почтового голубя', 'собаки', 'кастрюли', 'телекинеза', 'укропошты', 'мобильного телефона', 'старого телефона', 'рации']
        self.time_connect = random.randint(1,10000)
        self.method = random.choice(methods)

    def connect(self):    
        raise NotImplementedError('Нужно переопределить')

class Option1(ContactMethod):
    def connect(self):
        print(f'Связь с помощью {self.method} {self.time_connect} минут')

class Option2(ContactMethod):
    def connect(self):
        print(f'Связь с помощью {self.method} {self.time_connect} минут')

class Option3(ContactMethod):
    def connect(self):
        print(f'Связь с помощью {self.method} {self.time_connect} минут')

def process_connect(method: ContactMethod):
    method.sell()
    method.connect()


process_connect(Option1())
process_connect(Option2())
process_connect(Option3())