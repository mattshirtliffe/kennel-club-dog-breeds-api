import requests
from bs4 import BeautifulSoup
from flask import Flask, request


def get_html_doc():
    response = requests.get('https://www.thekennelclub.org.uk/services/public/breed/Default.aspx')
    return response.text

def get_breeds_from(soup):
    breed_div_id = 'MainContent_BreedListFront'
    for div in soup.find_all('div'):
        div_id = div.get('id')
        if div_id:
            if div_id == breed_div_id:
                for contents in div.contents:
                    try:
                        yield contents.a.text
                    except:
                        pass

app = Flask(__name__)

@app.route('/breeds')
def get_breeds():
    html_doc = get_html_doc()
    soup = BeautifulSoup(html_doc, 'lxml')
    breeds = [breed for breed in get_breeds_from(soup)]
    return {'breeds': breeds}
    

if __name__ == '__main__':
    
    html_doc = get_html_doc()
    soup = BeautifulSoup(html_doc, 'lxml')
    breeds = [breed for breed in get_breeds_from(soup)]
    print(breeds)




                    
