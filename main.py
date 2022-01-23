import requests
from bs4 import BeautifulSoup

res = requests.get('https://mandala.library.virginia.edu/terms/1/overview/nojs')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find_all('span'))
letter = soup.select('ajax-id-')
ti_letter = soup.select('.bo')
#
#


def create_custom_tib(letter, ti_letter):
    en_tib_letter = []
    for idx, item in enumerate(letter):
        letter_en = letter[idx].getText()
        en_tib_letter.append(letter_en)
    return en_tib_letter


print(create_custom_tib(letter, ti_letter))






