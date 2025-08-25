from .file_ops import load_library

def sort_by_author():
    library = load_library()
    for author in sorted(library.keys()):
        print(f"\n{author}:")
        for book in library[author]:
            print(f"   - {book}")


def sort_by_book():
    library = load_library()
    books = []
    for author, works in library.items():
        if isinstance(works, list):
            for book in works:
                books.append((book, author))
        else:
            books.append((works, author))

    for book, author in sorted(books, key=lambda x: x[0]):
        print(f"{book} — {author}")
         