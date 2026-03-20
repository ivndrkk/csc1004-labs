# Book class to model a library book
class Book:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.pages = 0
        self.on_loan = False

    @classmethod
    def set_attributes(cls, instance, title, author, pages):
        instance.title = title
        instance.author = author
        instance.pages = pages
        instance.on_loan = False

    @classmethod
    def print_attributes(cls, instance):
        print(f"{instance.author}. {instance.title}. {instance.pages} pp.")
        if instance.on_loan:
            print("Currently on loan")
        else:
            print("Currently available")

    @classmethod
    def borrow_book(cls, instance):
        instance.on_loan = True

    @classmethod
    def return_book(cls, instance):
        instance.on_loan = False
