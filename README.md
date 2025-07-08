# 📚 Books Scraper - Python Web Scraping Project

This project is a simple web scraper built with Python that extracts book data from [http://books.toscrape.com](http://books.toscrape.com), a website designed for practicing web scraping.

It collects the following information from the first page of books:

- 📘 Title
- 💰 Price (in GBP)
- ✅ Availability
- ⭐ Rating (1 to 5 stars)
- 🔗 Link to the product detail page

The data is exported to a `.csv` file named `books.csv`.

---

## 🔧 Technologies Used

- Python 3
- Requests
- BeautifulSoup (bs4)
- Pandas

---

## 🚀 How to Use

1. Download or clone this repository.

2. Install the required libraries:

```bash

pip install requests beautifulsoup4 pandas
