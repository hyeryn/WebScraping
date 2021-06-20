import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    #html가져오기
    result = requests.get(URL)
    #데이터 탐색 및 추출
    soup = BeautifulSoup(result.text,"html.parser")
    #해당 태그 내용만 추출 1 div찾아서 class명이 pagination인 것만 찾아 2 링크(a)찾기
    pagination = soup.find("div",{"class":"pagination"})
    links = pagination.find_all("a")
    pages = []
    #3 각 links에서 span만 가져와(마지막은 잘라줘)
    for link in links[:-1]:
        #pages.append(page.find("span").string)
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    #각페이지 request
    #for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
    for result in results:
        jobtitle = result.find("h2",{"class":"title"}) #.find("a")["title"]
        print(jobtitle.find("a").string)
    return jobs