import requests
from bs4 import BeautifulSoup
from .pages import PAGES
from .parsers import PARSERS

def name_value(name,page=1):
    page_get= requests.get(PAGES['page'+str(page)]+name)
    soup = BeautifulSoup(page_get.text,'html.parser')
    result =PARSERS['page'+str(page)](soup)
    
    if not result and page==len(PAGES):
        return 'no se encontro el significado del nombre '+name

    if result == None:
        return name_value(name,page+1)
  
    return result
    
