import scrapy


class MmaSpider(scrapy.Spider):
    name = "mma"

    def scrap_page(self, page):
        url = 'https://work.mma.go.kr/caisBYIS/search/byjjecgeomsaek.do'
        params = {
            "eopjong_gbcd": "1",
            "pageIndex": str(page),
            "pageUnit": "1000",
        }

        return scrapy.FormRequest(method='POST', url=url, formdata=params, callback=self.parse)

    def start_requests(self):
        yield self.scrap_page(1)

    def parse(self, response: scrapy.http.Response):
        rows = response.xpath('//table[@class="brd_list_n"]/tbody/tr')

        for row in rows:
            result = {
                '산학연계여부': row.xpath('td[1]/text()').get(),
                '지방청': row.xpath('td[2]/text()').get(),
                '채용유무': row.xpath('td[3]/text()').get(),
            }
            link = row.xpath('th/a/@href').get()
            yield response.follow(link, self.parse_content, meta=result)

        page_info = response.xpath('//div[@class="topics"]').get()

        current_page = int(page_info.split('(')[1].split('/')[0])
        total_page = int(page_info.split('/')[1].split(' ')[0])

        if current_page < total_page:
            yield self.scrap_page(current_page + 1)

    def parse_content(self, response: scrapy.http.Response):
        url = response.url
        company_code = int(url.split("byjjeopche_cd=")[1].split("&")[0])

        td = response.xpath('//table[1]/tbody/tr/td')

        result = {
            '업체코드': company_code,
            '업체명': td[0].xpath('text()').get(),
            '주소': td[1].xpath('text()').get(),
            '전화번호': td[2].xpath('text()').get(),
            '팩스번호': td[3].xpath('text()').get(),
            '업종': td[4].xpath('text()').get(),
            '주생산물': td[5].xpath('text()').get(),
            '기업규모': td[6].xpath('text()').get(),
            '연구분야': td[7].xpath('text()').get(),
            '현역배정인원': int(td[8].xpath('text()').get().replace("명", "")),
            '보충역배정인원': int(td[9].xpath('text()').get().replace("명", "")),
            '현역편입인원': int(td[10].xpath('text()').get().replace("명", "")),
            '보충역편입인원': int(td[11].xpath('text()').get().replace("명", "")),
            '현역복무인원': int(td[12].xpath('text()').get().replace("명", "")),
            '보충역복무인원': int(td[13].xpath('text()').get().replace("명", "")),
            '산학연계여부': response.meta['산학연계여부'],
            '지방청': response.meta['지방청'],
            '채용유무': response.meta['채용유무'],
        }

        yield result
