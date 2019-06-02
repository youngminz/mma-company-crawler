import unicodedata
import pymysql

class NormalizeString:
    def process_item(self, item, spider):

        for key, value in item.items():
            if isinstance(value, str):
                item[key] = unicodedata.normalize('NFC', unicodedata.normalize('NFKD', value)).strip()

        return item


class SaveToMySQL:
    def __init__(self):
        self.conn = pymysql.connect(
            user='root',
            passwd='password',
            db='mma',
            host='localhost',
            charset="utf8mb4",
            use_unicode=True
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """
            INSERT INTO company(업체코드, 업체명, 주소, 전화번호, 팩스번호, 업종, 주생산물, 기업규모, 연구분야, 현역배정인원, 보충역배정인원, 현역편입인원, 보충역편입인원, 현역복무인원, 보충역복무인원, 산학연계여부, 지방청, 채용유무) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                item["업체코드"],
                item["업체명"],
                item["주소"],
                item["전화번호"],
                item["팩스번호"],
                item["업종"],
                item["주생산물"],
                item["기업규모"],
                item["연구분야"],
                item["현역배정인원"],
                item["보충역배정인원"],
                item["현역편입인원"],
                item["보충역편입인원"],
                item["현역복무인원"],
                item["보충역복무인원"],
                item["산학연계여부"],
                item["지방청"],
                item["채용유무"],
            )
        )
        self.conn.commit()
