from Chapter3.contactlist import ContactList


class Contact:
	all_contacts = ContactList()

	def __init__(self, name, email):
		self.name = name
		self.email = email
		Contact.all_contacts.append(self)
