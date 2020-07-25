# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class ArticlesVkScrapyPipeline:
    articles = []
    FILENAME = "vk_article.csv"
    def process_item(self, item, spider):
        self.articles.append(item)
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        res = [ItemAdapter.asdict(item) for item in self.articles]
        with open(self.FILENAME, 'w',  encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(res[0].keys()))
            writer.writeheader()
            for i in res:
                writer.writerow(i)



