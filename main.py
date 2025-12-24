from src.browser import start_browser, stop_browser, get_page
from src.homepage import extract_genres
from src.genreDesc import extract_desc
from src.bookList import extract_bookList
from src.bookListDesc import extract_book_choice_desc
import os
import csv
BASE_URL = "https://www.goodreads.com"

folder = "data"
os.makedirs(folder, exist_ok=True)

filename = "output.csv"
full_path = os.path.join(folder, filename)

def main():
  start_browser(headless=True)

  #STEP 1: HOMEPAGE'S GENRES
  page = get_page(BASE_URL)
  genres = extract_genres(page)

  print("\nAvailable Genres:")
  for i , (genre,link) in enumerate(genres, start=1):
    print(f"{i}, {genre}")
  choice = int(input("\nPick a genre number: ")) - 1
  genre_url = BASE_URL + genres[choice][1]

  #STEP 2: GENRE PAGE'S DESCRIPTION
  page = get_page(genre_url)
  pagePackage = extract_desc(page)
  print("\n")
  print(pagePackage[0])
  
  #STEP 3: GENRE'S LIST OF TOP 100 BOOKS
  bookListURL = BASE_URL + pagePackage[1]
  page = get_page(bookListURL)
  bookList = extract_bookList(page)

  print("\n")
  print("Here is a list of all available books...")
  for i, (bookTitle, bookURL) in enumerate(bookList, start=1):
    print("\n")
    print(f"[{i}]: {bookTitle}")
  bookChoice = int(input("\nChoose a book number to learn more: ")) - 1

  #STEP 4: CHOSEN BOOK URL DESCRIPTION
  bookChoiceURL = BASE_URL + bookList[bookChoice][1]
  page = get_page(bookChoiceURL)
  data = extract_book_choice_desc(page)

  with open(full_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)

  stop_browser()

if __name__ == "__main__":
  main()