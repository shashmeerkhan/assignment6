class Book:
    totle_books=2
    @classmethod
    def increment_book_count(cls):
        cls.totle_books+=1
b1=Book()
print(b1.totle_books)