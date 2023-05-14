from bs4 import *
import requests
from prettytable import PrettyTable
import sys


name = input("Enter the name of the Person to gather information: ")
#name="Salman Khan"

try:
    url = "https://en.wikipedia.org/wiki/"+name.replace(' ','_')

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    name = soup.select_one(".fn")
    age = soup.select_one(".bday")
    place = soup.select_one(".birthplace")
    # occ = soup.select_one(".hlist")
    # occ1= soup.find_all('div','hlist')

    occ3 = soup.find('div', 'hlist')
    ul_menu = occ3.find('ul')
    menu_items = ul_menu.find_all('li')

    o = ""
    for c in menu_items:
        o += c.get_text() + ' . '

    print()
    photo = soup.select_one(".image")

    l = "https:"
    for p in photo:
        l += p['src']

    table = PrettyTable()

    table.field_names = ["Title", "Avilable Information"]

    table.add_row(["Name", name.get_text()])
    table.add_row(["Birth Date", age.get_text()])
    table.add_row(["Birth Place", place.get_text()])
    table.add_row(["Occupation", o])
    table.add_row(["Photo", l])
    table.add_row(["For More Information", url])

    table.align = 'l'
    print(table)

except:
    print("\n\n  Sorry Information Is Not Public \n")
    sys.exit(1)


