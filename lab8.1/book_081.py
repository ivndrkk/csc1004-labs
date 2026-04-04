class Book:
    def set_attributes(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = int(pages)
        self.isAvailable = True
    def print_attributes(self):
        print(f'{self.author}. {self.title}. {self.pages} pp.')
        if self.isAvailable:
            print("Currently available")
        else:
            print("Currently on loan")
    def borrow_book(self):
        if self.isAvailable:
            self.isAvailable = False
    def return_book(self):
        if not self.isAvailable:
            self.isAvailable = True