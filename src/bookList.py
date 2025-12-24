def extract_bookList(page) -> list[tuple[str,str]]:
  bookList = []
  seen = set()

  mainTitle = page.query_selector_all("div.mainContentFloat a.bookTitle[href^='/book/show/']")

  for book in mainTitle:
     pair = (book.inner_text().strip(), book.get_attribute("href").strip())
     if pair not in seen:
        seen.add(pair)
        bookList.append(pair)
  return bookList
