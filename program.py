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
html_doc = get_html_doc()
soup = BeautifulSoup(html_doc, 'lxml')
breeds = [breed for breed in get_breeds_from(soup)]

@app.route('/breeds')
def get_breeds():
    return {'breeds': [{'id':index, 'value': value} for index, value in enumerate(breeds)]}

@app.route('/breeds/<int:breed_id>')
def get_breed(breed_id):
    try:
        return {'breed': {'id': breed_id, 'value': breeds[breed_id]}}
    except:
        return {'message': 'not found'}, 404


if __name__ == '__main__':
    
    html_doc = get_html_doc()
    soup = BeautifulSoup(html_doc, 'lxml')
    breeds = [breed for breed in get_breeds_from(soup)]
    print(breeds)




                    
