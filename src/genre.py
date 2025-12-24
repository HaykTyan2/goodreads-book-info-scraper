def extract_books(page):
    #a.BookTitle short for a[class="bookTitle"]
    books = page.query_selector_all('a[class="bookTitle"]')
    return [(b.inner_text().strip(), b.get_attribute("href")) for b in books]
