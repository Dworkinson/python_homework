from orm.book import Book


if __name__ == '__main__':
    # Create book
    book = Book()
    book.author = 'caiman'
    book.title = 'JAVA'
    book.save()

    # select book
    book = Book(1)
    print(book.id)
    print(book.title)
    print(book.author)

    # update book
    book.author = 'anonymous'
    book.save()

    print(book.id)
    print(book.title)
    print(book.author)
