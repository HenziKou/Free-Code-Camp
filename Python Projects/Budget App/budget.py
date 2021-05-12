from typing import List


class Category():

	def __init__(self, name: str):
		self.name = name
		self.ledger = []

	def __str__(self):
		# Using formatted strings: align center, 30 char min, '*' as filler char
		title = f"{self.name:*^30}" + "\n"
		items = ""
		total = "Total: " + str(self.getBalance())

		for item in self.ledger:
			# Formatted strings: right align, 7 char min, 2 rounded decimal places
			# --------------------------------------------------------------
			#																|
			items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
		
		return title + items + total

	def deposit(self, amount: int, description = "") -> None:
		"""
		A deposit method that accepts an amount and description. If no description is given,
		it should default to an empty string. The method should append an object to the ledger
		list in the form of {"amount": amount, "description": description}.
		"""
		self.ledger.append( {"amount": amount, "description": description} )
		return None

	def withdraw(self, amount: int, description = "") -> bool:
		"""
		A withdraw method that is similar to the deposit method, but the amount passed in
		should be stored in the ledger as a negative number. If there are not enough funds,
		nothing should be added to the ledger. This method should return True if the
		withdrawal took place, and False otherwise.
		"""
		if (self.checkFunds(amount)):
			self.ledger.append( {"amount": (-1 * amount), "description": description} )
			return True
		return False

	def getBalance(self) -> float:
		"""
		A get_balance method that returns the current balance of the budget category based
		on the deposits and withdrawals that have occurred.
		"""
		balance = 0
		for item in self.ledger:
			balance += item["amount"]
		return balance

	def transfer(self, amount: int, budget) -> bool:
		"""
		A transfer method that accepts an amount and another budget category as arguments.
		The method should add a withdrawal with the amount and the description "Transfer to
		[Destination Budget Category]". The method should then add a deposit to the other
		budget category with the amount and the description "Transfer from [Source Budget
		Category]". If there are not enough funds, nothing should be added to either ledgers.
		This method should return True if the transfer took place, and False otherwise.
		"""
		transfer_to = "Transfer to" + budget.name
		transfer_from = "Transfer from" + self.name
		if (self.checkFunds(amount)):
			self.withdraw(amount, transfer_to)
			budget.deposit(amount, transfer_from)
			return True
		return False

	def checkFunds(self, amount: int) -> bool:
		"""
		A check_funds method that accepts an amount as an argument. It returns False if the
		amount is greater than the balance of the budget category and returns True otherwise.
		This method should be used by both the withdraw method and transfer method.
		"""
		if (amount > self.getBalance()):
			return False
		return True

	def getWithdrawals(self) -> float:
		"""
		A helper function for createSpendChart(). Returns the withdraw total.
		"""
		total = 0
		for item in self.ledger:
			if ( item["amount"] < 0 ):
				total += item["amount"]
		return total



def truncate(n: float) -> float:
	"""
	Helper function for getTotal(). Returns the rounded value.
	"""
	multiplier = 10
	return int(n * multiplier) / multiplier

def getTotal(categories: list) -> List[float]:
	"""
	Helper function for createSpendChart(). Returns the total percent spent, rounded down to
	the nearest tenth.
	"""
	total = 0
	breakdown = []

	for category in categories:
		# Calculate total amount withdrawn
		total += category.getWithdrawals()
		breakdown.append(category.getWithdrawals())

	rounded = list( map( lambda x: truncate(x / total), breakdown ) )
	return rounded

def createSpendChart(categories: list) -> str:
	result = "Percentage spent by category\n"
	i = 100
	percentages = getTotal(categories)

	while (i >= 0):
		# Formatting appropriate bars to their respective percentages
		spaces = " "
		for percent in percentages:
			if (percent * 100 >= i):
				spaces += "o  "
			else:
				spaces += "   "

		result += str(i).rjust(3) + "|" + spaces + "\n"
		i -= 10

	line = "-" + ( "---" * len(categories) )
	names = []
	x_axis = ""

	for category in categories:
		names.append(category.name)

	longest = max(names, key = len)

	for j in range( len(longest) ):
		# Print formatting the category name in a vertical line
		nameStr = "     "
		for name in names:
			if j >= len(name):
				nameStr += "   "
			else:
				nameStr += name[j] + "  "

		# Case handling for extra newline character at the last print line
		if ( j != len(longest) - 1 ):
			nameStr += "\n"
		x_axis += nameStr

	result += line.rjust( len(line) + 4 ) + "\n" + x_axis
	return result

