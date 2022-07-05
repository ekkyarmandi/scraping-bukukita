# Bukukita.com Scraping Project

[Bukukita.com](https://www.bukukita.com/katalogbuku.php) is one of the online bookstores in Indonesia. It has about 7k books in its database.

This project intended to collect all bukukita.com books data from its database and develop a Data Scraping script using Scrapy library. The scrapy will run through the pagination, collect all the links, and scrape the book details including the book title, author, publisher, ISBN, etc.

## How to run the script

You can clone this repo by typing command line below on your terminal. Make sure `git` have been installed on your computer.

```
git clone https://github.com/ekkyarmandi/scraping-bukukita.git`
```

Next change your directory into the cloned repo, then install all the dependencies by typing commmand line below

```
pip install -r requirements.txt
```

Last, you can run the script by executing

```
scrapy crawl buku
```

You also can specify the output by adding `-o` for output follow by the filename with extension (ie. `csv` or `json`)

```
scrapy crawl buku -o output.csv
```
