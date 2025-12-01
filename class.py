import random

class Letter:
    def sell(self):
        methods = ['e-mail', 'carrier pigeon', 'dog', 'pot', 'telekinesis', 'ukrainian postal service', 'mobile phone', 'Morse code', 'clerk']
        self._time_connect = random.randint(1,10000)
        self._method = random.choice(methods)
        self.__sms = 'Denn du bist was du isst'
        self.name()

    def connect(self):    
        raise NotImplementedError('Need to redefine')
    
class Recipient:
    def name(self):
        recipients = ['mexican', 'alien', 'Trump', 'aunt', 'parrot', 'Ziliboba', 'John Carter', 'me']
        self.recipient_name = random.choice(recipients)


class Option1(Letter, Recipient):
    def connect(self):
        print(f'Sending a letter by {self._method}. The leters will arrive in {self._time_connect} minutes. Recipient is {self.recipient_name}.')

class Option2(Letter, Recipient):
    def connect(self):
        print(f'Sending a letter by {self._method}. The leters will arrive in {self._time_connect} minutes. Recipient is {self.recipient_name}.')

class Option3(Letter, Recipient):
    def connect(self):
        print(f'Sending a letter by {self._method}. The leters will arrive in {self._time_connect} minutes. Recipient is {self.recipient_name}.')

def process_connect(method: Letter):
    method.sell()
    method.connect()


process_connect(Option1())
process_connect(Option2())
process_connect(Option3())