## goodreads-book-info-scraper

A Python-based scraper that extracts genres, book lists, and detailed book information from Goodreads using browser automation.

This project was built as a learning exercise to understand browser-based scraping, page traversal, and structuring a multi-file Python project.

---

## What this project does

The program walks through Goodreads step by step, similar to how a real user would browse the site.

It allows the user to:
- Choose a book genre
- Read the genre description
- View a list of popular books in that genre
- Select a specific book
- Extract detailed information about the selected book
- Save the extracted data to a CSV file

All scraping is done using a real browser session via Playwright.

---------------------------------------------------------------------------------------------------------------

## How it works (high level)

1. A browser session is started using Playwright.
2. The Goodreads homepage is loaded.
3. Available genres are extracted and displayed.
4. The user selects a genre.
5. The genre description and link to the book list are extracted.
6. A list of books from that genre is displayed.
7. The user selects a book.
8. Detailed book information is extracted.
9. The data is saved to a CSV file.
10. The browser session is closed.

---------------------------------------------------------------------------------------------------------------

## Project structure
```
goodreads-book-info-scraper/
├── src/
│ ├── browser.py # Browser lifecycle and page loading
│ ├── homepage.py # Extracts available genres from the homepage
│ ├── genreDesc.py # Extracts genre descriptions and related links
│ ├── genre.py # Genre-related helpers
│ ├── bookList.py # Extracts lists of books from a genre page
│ ├── bookListDesc.py # Extracts detailed book information
│ ├── BookListDesc2.py # Extracts book genres from a book page
│
├── main.py # Entry point and user interaction flow
├── .gitignore
├── README.md
```
---------------------------------------------------------------------------------------------------------------

## File explanations
## `main.py`
This is the main entry point of the program.

It is responsible for:
- Starting and stopping the browser
- Coordinating the scraping flow
- Handling user input
- Calling the appropriate extraction functions
- Writing extracted data to a CSV file

---------------------------------------------------------------------------------------------------------------

## `src/browser.py`
Handles browser automation.

This file:
- Starts the Playwright browser
- Creates and manages browser contexts
- Loads pages
- Closes all browser resources cleanly

---------------------------------------------------------------------------------------------------------------

## `src/homepage.py`
Extracts available book genres from the Goodreads homepage.

It returns:
- Genre names
- Links to genre pages

---------------------------------------------------------------------------------------------------------------

## `src/genreDesc.py`
Extracts information from a genre page.

This includes:
- A short genre description
- A link to a page containing a list of books in that genre

---------------------------------------------------------------------------------------------------------------

## `src/bookList.py`
Extracts a list of books from a genre’s book list page.

Each book entry includes:
- Book title
- Link to the book’s detail page

Duplicate entries are filtered out.

---------------------------------------------------------------------------------------------------------------

## `src/bookListDesc.py`
Extracts detailed information about a selected book.

This includes:
- Book title
- Contributor / author
- Rating
- Total number of ratings
- Genres associated with the book

The extracted data is returned as a dictionary for easy CSV writing.

---------------------------------------------------------------------------------------------------------------

## `src/BookListDesc2.py`
Contains helper logic for extracting genre tags from a book’s detail page.

This file is used by `bookListDesc.py`.

---------------------------------------------------------------------------------------------------------------


## Installation / Process

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/goodreads-book-info-scraper.git
cd goodreads-book-info-scraper
```

---------------------------------------------------------------------------------------------------------------

2. Install dependencies:
```
pip install playwright
playwright install
```

---------------------------------------------------------------------------------------------------------------

3. Run the program:
```
python main.py
```

---------------------------------------------------------------------------------------------------------------
## You will be prompted to:

• Select a genre
• Select a book
• Automatically generate a CSV file with book details

The scraping process follows a guided, interactive flow.
---------------------------------------------------------------------------------------------------------------

## Output:
• Book information is saved to a CSV file.
• Each run overwrites the previous output unless modified.
• The CSV contains structured, labeled fields for each extracted value.

---------------------------------------------------------------------------------------------------------------

## Notes and limitations:
• This project uses synchronous browser automation.
• It is not optimized for speed or large-scale scraping.
• Goodreads page structure may change over time, which could require selector updates.
• This project is intended for educational purposes only.

---------------------------------------------------------------------------------------------------------------
## License:
This project is provided for educational use.
