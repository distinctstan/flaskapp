import xmltodict
from pkg import app

@app.route('/xml/')
def xml():
    with open('productxml.txt') as xml:
        result = xmltodict.parse(xml.read())
        print(result)
    return f'{str(result['product']['prodname']['#text'])}'
