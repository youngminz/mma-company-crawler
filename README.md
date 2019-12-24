# 병무청 산업지원 병역일터 크롤러

## 왜 만들었나요?

- 우리 회사에 비해 다른 업체들은 보충역을 얼마나 뽑는지 궁금해졌습니다.
- 병무청 사이트에서 통계를 볼 수 있는 방법이 없었습니다.
- `scrapy` 처음으로 써 봤습니다.

## 어떻게 사용하나요?

- python 3.6 이상을 설치하세요.
- `pip install requirements.txt`
- mysql에 데이터베이스를 저장하려면 테이블을 만들어야 합니다.
```mysql
CREATE TABLE `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `업체코드` int(11) NOT NULL,
  `업체명` varchar(45) DEFAULT NULL,
  `주소` varchar(512) DEFAULT NULL,
  `전화번호` varchar(45) DEFAULT NULL,
  `팩스번호` varchar(45) DEFAULT NULL,
  `업종` varchar(45) DEFAULT NULL,
  `주생산물` varchar(45) DEFAULT NULL,
  `기업규모` varchar(45) DEFAULT NULL,
  `연구분야` varchar(45) DEFAULT NULL,
  `보충역배정인원` int(11) DEFAULT NULL,
  `보충역편입인원` int(11) DEFAULT NULL,
  `보충역복무인원` int(11) DEFAULT NULL,
  `현역배정인원` int(11) DEFAULT NULL,
  `현역편입인원` int(11) DEFAULT NULL,
  `현역복무인원` int(11) DEFAULT NULL,
  `산학연계여부` varchar(45) DEFAULT NULL,
  `지방청` varchar(45) DEFAULT NULL,
  `채용유무` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `업체코드_UNIQUE` (`업체코드`)
) ENGINE=InnoDB AUTO_INCREMENT=8586 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```
- `mma/pipelines.py`의 `SaveToMySQL` 에 들어가는 데이터베이스 연결 파라미터를 적절히 수정하세요.
- MySQL에 저장하는 기능을 끄고 싶으면 `mma/settings.py` 에서 `ITEM_PIPELINES` 를 수정하시면 됩니다.
- `scrapy crawl mma` 으로 크롤링을 시작하세요.

## 피플펀드는 2019년, 현역과 보충역을 얼마나 신규 편입시켰나요?

```mysql
SELECT 업체명,
       현역배정인원,
       현역편입인원,
       현역복무인원,
       보충역편입인원,
       보충역복무인원
FROM   company
WHERE  지방청 = '서울'
       AND 업종 = '정보처리'
ORDER  BY 보충역편입인원 DESC; 
```

- 2019년 11월 20일 기준, 피플펀드는 신규 현역을 3명 (현역 재배정 TO 2명), 신규 보충역을 3명 편입시켰습니다.
- 전체 업체 목록은 [stats_20191120.csv](stats_20191120.csv) 파일을 참고하세요.

## 채용

[피플펀드는 산업기능요원 현역/보충역의 신규/전직 채용하고 있습니다!](https://github.com/peoplefund-tech/careers/blob/master/README.md)
