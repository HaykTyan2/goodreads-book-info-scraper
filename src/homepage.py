def extract_genres(page):
    #internally, page.query_selector_all() creates and 
    # returns a Python list of objects
    links = page.query_selector_all("a[href^='/genres/']")
    return [(l.inner_text().strip(), l.get_attribute("href")) for l in links]
