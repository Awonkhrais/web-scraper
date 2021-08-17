import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    result = soup.find_all("span" ,text='citation needed')
    return len(result)


def get_citations_needed_report(url):
    arr = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    result=soup.find_all('p')
    # return result
    for i in result:
        citations=i.find_all('a',title='Wikipedia:Citation needed')
        for citation in citations:
            arr.append(i.text)

    return(arr)
    # return ('\n').join(arr)




if __name__ == "__main__":
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
