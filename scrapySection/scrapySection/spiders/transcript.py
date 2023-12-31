import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule



 # ========================= Scraping  with user-agent  =========================
class TranscriptsSpider(CrawlSpider):
    name = 'transcript'
    allowed_domains = ['subslikescript.com']
    # start_urls = ['https://subslikescript.com/movies_letter-X']

    # Setting an user-agent variable
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

    # Editing the user-agent in the request sent
    def start_requests(self):
        yield scrapy.Request(url='https://subslikescript.com/movies_letter-X', headers={
            'user-agent':self.user_agent
        })

    # Setting rules for the crawler
    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]")), process_request='set_user_agent'),
    )

    # Setting the user-agent
    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request
    
# for MongodbPipeline to work
    # def parse_item(self, response):
    #     # Getting the article box that contains the data we want (title, plot, etc)
    #     article = response.xpath("//article[@class='main-article']")

    #     # Extract the data we want and then yield it
    #     yield {
    #         'title': article.xpath("./h1/text()").get(),
    #         'plot': article.xpath("./p/text()").get(),
    #         'transcript': article.xpath("./div[@class='full-script']/text()").getall(),
    #         'url': response.url,
    #         'user-agent': response.request.headers['User-Agent'],
    #     }

# for SQLitPipeline to work
    def parse_item(self, response):
        # Getting the article box that contains the data we want (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")
        # .getall() will return a list, use .join() to turn the list into a string
        transcript_list = article.xpath("./div[@class='full-script']/text()").getall()
        transcript_string = ' '.join(transcript_list)

        # Extract the data we want and then yield it
        yield {
            'title':article.xpath("./h1/text()").get(),
            'plot':article.xpath("./p/text()").get(),
            'transcript':transcript_string,
            'url':response.url,
            # 'user-agent':response.request.headers['User-Agent'],
        }




"""

# ========================= Scraping a page =========================
class TranscriptSpider(CrawlSpider):
    name = "transcript"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com/movies/"]


    # Setting rules for the crawler
    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Getting the article box that contains the data we want (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")

        # Extract the data we want and then yield it
        yield {
            'title': article.xpath("./h1/text()").get(),
            'plot': article.xpath("./p/text()").get(),
            'transcript': article.xpath("./div[@class='full-script']/text()").getall(),
            'url': response.url,
        }



# ========================= Scraping pagination =========================

class TranscriptsSpider(CrawlSpider):
    name = 'transcripts'
    allowed_domains = ['subslikescript.com']
    start_urls = ['https://subslikescript.com/movies_letter-X']  # let's test scraping all the pages for the X letter

    # Setting rules for the crawler
    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]"))),
    )

    def parse_item(self, response):
        # Getting the article box that contains the data we want (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")

        # Extract the data we want and then yield it
        yield {
            'title':article.xpath("./h1/text()").get(),
            'plot':article.xpath("./p/text()").get(),
            # 'transcript':article.xpath("./div[@class='full-script']/text()").getall(),
            'url':response.url,
        }


"""