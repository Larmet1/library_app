from .file_ops import load_library, save_library
from tkinter import simpledialog

def add_entry_gui(root):
    author = simpledialog.askstring("Додати книгу", "Введіть автора:", parent=root)
    if not author:
        return

    books = []
    while True:
        book = simpledialog.askstring(
            "Додати книгу",
            "Введіть назву книги (або залиште порожнім для завершення):",
            parent=root
        )
        if not book:
            break
        books.append(book)

    library = load_library()
    if author in library:
        if isinstance(library[author], list):
            library[author].extend(books)
        else:
            library[author] = [library[author]] + books
    else:
        library[author] = books

    save_library(library)
