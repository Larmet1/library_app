import tkinter as tk
from library.catalog import add_entry_gui
from library.sort import get_sorted_authors, get_sorted_books
from library.file_ops import load_library

# --- Основне вікно ---
root = tk.Tk()
root.title("Бібліотека")
root.geometry("700x500")
root.configure(bg="#2b2b2b")

# --- Текстове поле з темною темою (тільки для читання) ---
text_area_frame = tk.Frame(root, bg="#2b2b2b")
text_area_frame.pack(expand=True, fill="both", padx=10, pady=10)

text_area = tk.Text(
    text_area_frame,
    bg="#2b2b2b",
    fg="#ffffff",
    insertbackground="white",
    state="disabled",  # тільки для читання
)
text_area.pack(expand=True, fill="both")

scrollbar = tk.Scrollbar(text_area_frame, command=text_area.yview)
scrollbar.pack(side="right", fill="y")
text_area.configure(yscrollcommand=scrollbar.set)

# --- Функція для оновлення Text ---
def update_text_area(content):
    text_area.config(state="normal")  # тимчасово дозволяємо редагування
    text_area.delete("1.0", "end")
    text_area.insert("1.0", content)
    text_area.config(state="disabled")  # блокуємо для користувача

# --- Функції для кнопок ---
def show_catalog():
    library = load_library()
    if not library:
        update_text_area("Каталог порожній")
        return

    output = ""
    for author, books in library.items():
        output += f"{author}:\n"
        for book in books:
            output += f"   - {book}\n"
        output += "\n"
    update_text_area(output)

def add_book():
    add_entry_gui(root)
    show_catalog()

def sort_author():
    output = ""
    for author in get_sorted_authors():
        output += f"{author}:\n"
        for book in load_library()[author]:
            output += f"   - {book}\n"
        output += "\n"
    update_text_area(output)

def sort_book():
    output = ""
    for book, author in get_sorted_books():
        output += f"{book} — {author}\n"
    update_text_area(output)

# --- Кнопки ---
btn_frame = tk.Frame(root, bg="#2b2b2b")
btn_frame.pack(pady=5)

btn_catalog = tk.Button(btn_frame, text="Перегляд каталога", command=show_catalog, bg="#444", fg="white", width=20)
btn_catalog.grid(row=0, column=0, padx=5)

btn_add = tk.Button(btn_frame, text="Додати книги", command=add_book, bg="#444", fg="white", width=20)
btn_add.grid(row=0, column=1, padx=5)

btn_sort_author = tk.Button(btn_frame, text="Сортування за автором", command=sort_author, bg="#444", fg="white", width=20)
btn_sort_author.grid(row=0, column=2, padx=5)

btn_sort_book = tk.Button(btn_frame, text="Сортування за твором", command=sort_book, bg="#444", fg="white", width=20)
btn_sort_book.grid(row=0, column=3, padx=5)

btn_exit = tk.Button(btn_frame, text="Вихід", command=root.quit, bg="#444", fg="white", width=20)
btn_exit.grid(row=0, column=4, padx=5)

root.mainloop()
