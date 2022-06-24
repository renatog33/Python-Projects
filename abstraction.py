from abc import ABC, abstractmethod
class motorcycle(ABC): #abstract class
    def invoice(self, amount): #regular method- invoice for motorcyle purchase
        print("Your invoice will total: ",amount)

    @abstractmethod
    def payment(self, amount):
        pass

class StoreCredit(motorcycle): #child class
    #defined how to implement the payment functionfrom its invoice class for a refund/credit
    def payment(self, amount):
        print('Your purchase amount of {} will be applied as a store credit.'.format(amount))

obj = StoreCredit()
obj.invoice("$2,500")
obj.payment("$2,500")
