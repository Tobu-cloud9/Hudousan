# -*- coding: utf-8 -*-
import scrapy
from ..items import HudousanItem

class HudousanSpiderSpider(scrapy.Spider):
    name = 'hudousan_spider'
    allowed_domains = ['tancyu-f.com']
    start_urls = ['https://tancyu-f.com/rent/']
    item = HudousanItem()

    def parse(self, response):
        # 不動産のURLをそれぞれ取得
        for url in response.css('div.category__detail a::attr("href")').extract():
            self.item['link'] = url

        # 次ページのURLを取得する
        next_page = response.css('div.nav_pager a::attr("href")')[-1].extract()
        print(next_page)
        if next_page is not None:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)