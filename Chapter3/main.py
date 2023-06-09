from Chapter3.contact import Contact
from Chapter3.supplier import Supplier

c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
print(c.name, c.email, s.name, s.email)

print(c.all_contacts)
