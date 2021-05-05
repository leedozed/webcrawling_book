import urllib.request
import bs4

url = "http://news.naver.com/"
html = urllib.request.urlopen(url) #urlopen: 특정 url을 호출

bs_obj = bs4.BeautifulSoup(html, "html.parser") #(변수, 파싱할 파서)

print(bs_obj)
