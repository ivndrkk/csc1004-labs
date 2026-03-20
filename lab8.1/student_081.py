# Student class to model a student
class Student:
    def set_attributes(self, sid, name, modlist):
        self.sid = sid
        self.name = name
        self.modlist = list(modlist)

    def print_attributes(self):
        print(f"ID: {self.sid}")
        print(f"Name: {self.name}")
        print(f"Modules: {', '.join(self.modlist)}")

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)
