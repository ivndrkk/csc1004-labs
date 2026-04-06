class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"{self.name} {self.phone} {self.email}"

class Contactlist:
    def __init__(self, d={}):
        self.d = d
    def add(self, contact):
        self.d[contact.name] = contact
    def remove(self,name):
        if name in self.d:
            del self.d[name]
    def get(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None
    def __str__(self):
        print("Contact list")
        print("------------")
        list_of_contacts = []
        for x in self.d:
            list_of_contacts.append(str(self.d[x]))
        list_of_contacts.sort()
        return "\n".join(list_of_contacts)