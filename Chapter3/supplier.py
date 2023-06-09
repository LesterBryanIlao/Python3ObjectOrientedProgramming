from Chapter3.contact import Contact


class Supplier(Contact):
    def order(self, order):
        # If this were a real system we would send
        print(f"'{order}' order to '{self.name}'")
