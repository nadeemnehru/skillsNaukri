import scrapy

class skillsSpider(scrapy.Spider):
	name = "skillsNaukriBot"

	start_urls = ["https://www.naukri.com/top-skill-jobs"]

	def parse(self, response):
		pages = response.xpath('//div[@class="multiColumn colCount_four"]/a/@href').extract()
		for page in pages:
			yield scrapy.Request(page, callback=self.parsePage)

	def parsePage(self, response):
		skills = []
		skills.extend(response.xpath('//span[@class="skill"]/text()').extract())
		yield {'Skill': skills}
		nextPage = response.xpath('//div[@class="pagination"]/a/@href').extract_first()

		if nextPage is not None:
			yield response.follow(url=nextPage, callback=self.parsePage)
