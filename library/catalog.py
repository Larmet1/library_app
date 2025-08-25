from .file_ops import load_library, save_library


def view_catalog():
    library = load_library()
    if not library:
        print("Каталог порожній")
        return
    for author, books in library.items():
        print(f"\n{author}:")
        if isinstance(books, list):
            for book in books:
                print(f"   - {book}")
        else:
            print(f"   {books}")


def add_entry():
    library = load_library()
    
    while True:
        author = input('Введіть автора (або "вийти" щоб повернутись у меню): ').strip()
        if author.lower() == 'вийти':
            print("Повертаємося в головне меню")
            return  # вихід назад у меню

        books_input = input('Введіть книги через пробіл (або "вийти" щоб повернутись у меню): ').strip()
        if books_input.lower() == 'вийти':
            print("Повертаємося в головне меню")
            return  # вихід назад у меню

        # Розбиваємо введений рядок на список книг
        books = books_input.split()

        if author in library:
            if isinstance(library[author], list):
                library[author].extend(books)
            else:
                library[author] = [library[author]] + books
        else:
            library[author] = books

        save_library(library)
        print(f"Книги {books} додано успішно!")
            
