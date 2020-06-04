groupby
~~~~~~~

Функция groupby

.. code:: python

    itertools.groupby(iterable, key=None)

Пример использования:

.. code:: python

    from pprint import pprint
    from dataclasses import dataclass
    import operator

    @dataclass(frozen=True)
    class Book:
        title: str
        author: str


    In [75]: books
    Out[75]:
    [Book(title='1984', author='George Orwell'),
     Book(title='The Martian Chronicles', author='Ray Bradbury'),
     Book(title='The Hobbit', author='J.R.R. Tolkien'),
     Book(title='Animal Farm', author='George Orwell'),
     Book(title='Fahrenheit 451', author='Ray Bradbury'),
     Book(title='The Lord of the Rings (1-3)', author='J.R.R. Tolkien'),
     Book(title='Harry Potter and the Sorcerer’s Stone', author='J.K. Rowling'),
     Book(title='To Kill a Mockingbird', author='Harper Lee')]


    In [76]: list(groupby(books, operator.attrgetter('author')))
    Out[76]:
    [('George Orwell', <itertools._grouper at 0xb473f3ec>),
     ('Ray Bradbury', <itertools._grouper at 0xb473f12c>),
     ('J.R.R. Tolkien', <itertools._grouper at 0xb473f98c>),
     ('George Orwell', <itertools._grouper at 0xb473f7cc>),
     ('Ray Bradbury', <itertools._grouper at 0xb473f40c>),
     ('J.R.R. Tolkien', <itertools._grouper at 0xb473f74c>),
     ('J.K. Rowling', <itertools._grouper at 0xb473ffcc>),
     ('Harper Lee', <itertools._grouper at 0xb473fbec>)]


    In [81]: for key, item in groupby(books, operator.attrgetter('author')):
        ...:     print(key.ljust(20), list(item))
        ...:
    George Orwell        [Book(title='1984', author='George Orwell')]
    Ray Bradbury         [Book(title='The Martian Chronicles', author='Ray Bradbury')]
    J.R.R. Tolkien       [Book(title='The Hobbit', author='J.R.R. Tolkien')]
    George Orwell        [Book(title='Animal Farm', author='George Orwell')]
    Ray Bradbury         [Book(title='Fahrenheit 451', author='Ray Bradbury')]
    J.R.R. Tolkien       [Book(title='The Lord of the Rings (1-3)', author='J.R.R. Tolkien')]
    J.K. Rowling         [Book(title='Harry Potter and the Sorcerer’s Stone', author='J.K. Rowling')]
    Harper Lee           [Book(title='To Kill a Mockingbird', author='Harper Lee')]


    In [83]: sorted_books = sorted(books, key=operator.attrgetter('author'))

    In [84]: sorted_books
    Out[84]:
    [Book(title='1984', author='George Orwell'),
     Book(title='Animal Farm', author='George Orwell'),
     Book(title='To Kill a Mockingbird', author='Harper Lee'),
     Book(title='Harry Potter and the Sorcerer’s Stone', author='J.K. Rowling'),
     Book(title='The Hobbit', author='J.R.R. Tolkien'),
     Book(title='The Lord of the Rings (1-3)', author='J.R.R. Tolkien'),
     Book(title='The Martian Chronicles', author='Ray Bradbury'),
     Book(title='Fahrenheit 451', author='Ray Bradbury')]

    In [85]: for key, item in groupby(sorted_books, operator.attrgetter('author')):
        ...:     print(key.ljust(20), list(item))
        ...:
    George Orwell        [Book(title='1984', author='George Orwell'), Book(title='Animal Farm', author='George Orwell')]
    Harper Lee           [Book(title='To Kill a Mockingbird', author='Harper Lee')]
    J.K. Rowling         [Book(title='Harry Potter and the Sorcerer’s Stone', author='J.K. Rowling')]
    J.R.R. Tolkien       [Book(title='The Hobbit', author='J.R.R. Tolkien'), Book(title='The Lord of the Rings (1-3)', author='J.R.R. Tolkien')]
    Ray Bradbury         [Book(title='The Martian Chronicles', author='Ray Bradbury'), Book(title='Fahrenheit 451', author='Ray Bradbury')]

    In [86]: books_by_author = {}

    In [87]: for key, item in groupby(sorted_books, operator.attrgetter('author')):
        ...:     books_by_author[key] = list(item)
        ...:

    In [90]: pprint(books_by_author)
    {'George Orwell': [Book(title='1984', author='George Orwell'),
                       Book(title='Animal Farm', author='George Orwell')],
     'Harper Lee': [Book(title='To Kill a Mockingbird', author='Harper Lee')],
     'J.K. Rowling': [Book(title='Harry Potter and the Sorcerer’s Stone', author='J.K. Rowling')],
     'J.R.R. Tolkien': [Book(title='The Hobbit', author='J.R.R. Tolkien'),
                        Book(title='The Lord of the Rings (1-3)', author='J.R.R. Tolkien')],
     'Ray Bradbury': [Book(title='The Martian Chronicles', author='Ray Bradbury'),
                      Book(title='Fahrenheit 451', author='Ray Bradbury')]}

