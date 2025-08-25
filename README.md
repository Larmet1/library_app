# Library App

A simple **Python library management application** with a **dark-themed Tkinter GUI**. This app allows you to view, add, and sort books by author or title.

---

## Features

- View the full library catalog
- Add new books to existing or new authors
- Sort books by **author** or **title**
- Dark-themed GUI for comfortable reading
- Read-only catalog display to prevent accidental editing

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/library_app.git
cd library_app
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> Tkinter is included with Python, so no need to install it separately.

---

## Usage

Run the main GUI application:

```bash
python main.py
```

- **Buttons:**

  - _View Catalog_ — displays all books
  - _Add Books_ — add a new book or author
  - _Sort by Author_ — sorts library by authors
  - _Sort by Book_ — sorts all books alphabetically
  - _Exit_ — close the application

---

## File Structure

```
library_app/
│
├── main.py          # Main GUI program
├── library/
│   ├── __init__.py
│   ├── file_ops.py  # Load/save JSON
│   ├── catalog.py   # Add books GUI functions
│   └── sort.py      # Sorting functions
└── library.json     # Library data (ignored by Git)
```

---

## Notes

- The library data is stored in `library.json`.
- The text area in the GUI is **read-only**; you cannot modify books directly.
- `.gitignore` prevents local files like virtual environments, JSON, and build files from being uploaded to GitHub.

---

## Optional: Create an EXE

```bash
pyinstaller --onefile --noconsole main.py
```

This will generate a single executable in the `dist/` folder without showing the console window.

---
