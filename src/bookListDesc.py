from src.BookListDesc2 import extract_genres

def extract_book_choice_desc(page) -> dict:
    # Title
    bookTitle = page.query_selector("div.BookPageTitleSection__title h1.Text").inner_text().strip()
    print("BOOKTITLE" + bookTitle)

    # Contributor
    contributor = page.query_selector("div.ContributorLinksList span.ContributorLink__name").inner_text().strip()
    print("CONTRIBUTOR" + contributor)

    # Rating
    rating = page.query_selector("div.RatingStatistics__rating").inner_text().strip()
    print("RATING" + rating)

    # Ratings total
    ratingText = page.query_selector("span[data-testid='ratingsCount']").inner_text().strip()
    ratingTotal = ratingText.split()[0].strip()
    print("RATING TOTAL" + ratingTotal)

    # Genres
    genres = extract_genres(page)
    print("Genres:", ", ".join(genres))

    # Return structured data
    return {
        "Title": bookTitle,
        "Contributor": contributor,
        "Rating": rating,
        "RatingsTotal": ratingTotal,
        "Genres": ", ".join(genres)   # flatten list into a single string
    }

