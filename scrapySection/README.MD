# Project Scrapy section 

Brief description of the project.

## Installation

install the libs in requirement.txt
pymongo==4.5.0
dnspython==2.4.2

Scrapy==2.11.0


## Usage
scrapy startproject scrapySection # for starting project
scrapy genspider -t crawl transcript subslikescript.com/movies # from creating project file
scrapy crawl transcript -o transcripts.csv # from crawl the site and saving the data in a csv file
scrapy crawl Quotes -o quotes.json # for data to crawl and save data in a json file



docker pull scrapinghub/splash # to install splash after starting docker
docker run -it -p 8050:8050 scrapinghub/splash


## Contributing

Guidelines on how to contribute to the project.

## links
 Targeted site scrapted
www.worldometers.info
https://subslikescript.com/movies
www.worldometers.info
https://quotes.toscrape.com/scroll

 to view sqlite db
https://inloop.github.io/sqlite-viewer/


