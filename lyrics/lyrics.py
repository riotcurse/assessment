from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

#get page
#search through page for lyrics text
#return lyrics text as string

def SimpleGet(url):
    try:
        with closing(get(url,stream=True)) as resp:
            if isGoodResponse(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}',format(url,str(e)))
        return None

def isGoodResponse(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def logError(e):
    print(e)

#given bs4 html object, recursively search for target class
def getLyrics(html,identifier=''):
    soup = BeautifulSoup(html)
    lyrics = soup.select(identifier)
    return lyrics[0].get_text()
    
