class Author:
    all = []
    pass
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []
    pass
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def authors(self):
        return[contract.author for contract in self.contracts()]
    
    def contracts(self):
        return[contract for contract in Contract.all if contract.book == self]


class Contract:
    pass
    all = []
    def __init__(self,author:Author, book:Book, date:str, royalties:int):
        pass

        self.author: Author = author
        self.book: Book = book
        self.royalties:int = royalties
        self.date:str = date
        Contract.all.append(self)

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance (value, str):
            raise TypeError ('Date must be a string')
        self._date= value
    
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, value):
        if not isinstance (value, int):
            raise TypeError ('Royalties must be an integer')
        self._royalties= value
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not isinstance (value, Author):
            raise TypeError ('Author must be an instance of Author class')
        self._author = value

    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if not isinstance (value, Book):
            raise TypeError ('Book must be an instance of Book class')
        self._book = value


    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]