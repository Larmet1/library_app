from .file_ops import load_library
import locale

locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

def get_sorted_authors():
    library = load_library()
    return sorted(library.keys(), key=locale.strxfrm)

def get_sorted_books():
    library = load_library()
    books_list = []
    for author, books in library.items():
        if isinstance(books, list):
            for book in books:
                books_list.append((book, author))
        else:
            books_list.append((books, author))
    books_list.sort(key=lambda x: locale.strxfrm(x[0]))
    return books_list
