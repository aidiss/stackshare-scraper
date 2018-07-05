StackShare Scraper
===================

Scraper www.stackshare.com
Only for educational purposes.
Use at own risk, it might violate StackShare policies.

# Dependencies
Install: 
* [Scrapy](http://doc.scrapy.org)

# Usage - Have fun!
```shell
cd stackshare-scraper/
```

Scrape and save data in JSON lines format:
```shell
scrapy crawl main -o output/result.json
```

For JSON format use:
```shell
scrapy crawl main -o output/result.json -t json
```
