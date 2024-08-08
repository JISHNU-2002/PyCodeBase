class BankAccount:
	def __init__(self, balance): # constructor
		self.__balance = balance

	def deposit(self, amount):   # mutator 
		self.__balance += amount

	def getBalance(self):        # accessor
		return self.__balance

account = BankAccount(1000)
# print(account._BankAccount__balance) : Output: 1000
account.deposit(2000)
print(account.getBalance()) # 3000
