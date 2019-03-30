from newspaper import Article
import os


def crawl():
    path = os.path.join(os.getcwd(), 'data_test')
    list_url =[
        'https://dantri.com.vn/the-gioi/nhom-chuyen-gia-my-tai-khoi-dong-uy-ban-thoi-chien-tranh-lanh-doi-pho-trung-quoc-20190326150158070.htm',
        'https://vnexpress.net/the-gioi/trieu-tien-neu-ten-nhung-nguoi-can-tro-hoi-nghi-voi-my-tai-ha-noi-3900163.html',
        'https://vnexpress.net/kinh-doanh/nhieu-cay-xang-ha-noi-dung-ban-ron-95-3900207.html'
    ]
    i = 0
    for url in list_url:
        i += 1
        article = Article(url)
        article.download()
        article.parse()
        os.chdir(path)
        file_name = 'test{0}.txt'.format(i)
        with open(file_name, "w+", encoding="utf-8") as w:
            w.write(article.text)
    print(" carawling success!!!")

