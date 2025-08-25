# --- Основна програма ---
from library.catalog import view_catalog, add_entry
from library.sort import sort_by_author, sort_by_book

def main():
    while True:
        print("\nПрограма Бібліотека\n\n\tМеню")
        print("1 - Перегляд каталога")
        print("2 - Внести зміни")
        print("3 - Сортування за автором")
        print("4 - Сортування за твором")
        print("0 - Вихід")
        choice = input("\nВаш вибір: ")
        
        if choice == "1":
            view_catalog()
        elif choice == "2":
            add_entry()
        elif choice == "3":
            sort_by_author()
        elif choice == "4":
            sort_by_book()
        elif choice == "0":
            print("Вихід...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
        
        
if __name__ == '__main__':
    main()
        
        