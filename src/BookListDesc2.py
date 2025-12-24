#PART 2 FOR EXTRACTING GENRES

def extract_genres(page) -> list[tuple[str, str]]:
  genres = []

  genre_spans = page.query_selector_all("span.BookPageMetadataSection__genreButton")

  for span in genre_spans:
    genres.append(span.inner_text().strip())

  return genres
