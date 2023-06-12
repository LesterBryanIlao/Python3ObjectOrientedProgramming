class EvenOnly(list):
	def append(self, integer):
		if not isinstance(integer, int):
			raise TypeError("Only integers can be added")
		if integer % 2:
			raise ValueError("Only even numbers can be added")
		super().append(integer)


def funny_division(divider):
	try:
		if divider == 13:
			raise ValueError("13 is an unlucky number")
		return 100 / divider
	except (ZeroDivisionError):
		return "Zero is not a good idea!"
	except (TypeError):
		return "Enter a number please!"


def funny_division3(divider):
	try:
		if divider == 13:
			raise ValueError("13 is an unlucky number")
		return 100 / divider
	except ZeroDivisionError:
		return "Enter a number other than zero"
	except TypeError:
		return "Enter a numerical value"
	except ValueError:
		print("No, No, not 13!")
		raise


# print(funny_division3(13))  # evenlist = EvenOnly()  # evenlist.append(2)  # try:
# 	evenlist.append(11)
# except ValueError as e:
# 	print(f"Error: {e}")
# print(evenlist)

import random

some_exceptions = [ValueError, TypeError, IndexError, None]
try:
	choice = random.choice(some_exceptions)
	print("raising {}".format(choice))
	if choice:
		raise choice("An error")
except ValueError:
	print("Caught a ValueError")
except TypeError:
	print("Caught a TypeError")
except Exception as e:
	print("Caught some other error: %s" % (e.__class__.__name__))
else:
	print("This code called if there is no exception")
finally:
	print("This cleanup code is always called")
