def extract_desc(page):
  description = page.query_selector("div.mediumText.reviewText span[id^='freeText']")
  moreBooks = page.query_selector("a.actionLink[href^='/shelf/show/']")
  text = ""
  booksListURL = ""

  if description:
    temp = description.inner_html()
    text = temp.split("<br>")[0].strip()
  
  if moreBooks:
    booksListURL = moreBooks.get_attribute("href")

  return (text,booksListURL)