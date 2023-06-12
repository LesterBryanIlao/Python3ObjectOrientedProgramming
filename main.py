from Chapter2.menu import Menu
from Chapter2.note import Note
from Chapter2.notebook import Notebook

nb1 = Notebook()
nb1.new_note("hello world1", "tag1")
nb1.new_note("hello world2", "tag2")
nb1.new_note("hello world3", "tag3")
menu = Menu(nb1)
menu.run()


def product(*args):
	if len(args) == 0:
		raise TypeError('At least one argument required')
	result = 1
	for arg in args:
		result *= arg
	return result
