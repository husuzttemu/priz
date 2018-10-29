#import libraries
import requests
from bs4 import  BeautifulSoup

from locators import page_locators

#print(pagecontent)




#print(simple_soup)


def parse_products(e):
    #xyz = BeautifulSoup(text, "html.parser")
    text = e.select_one("input.product_id")
    id = text.attrs['value']
    text = e.select_one("form.basket-process")
    name = text.attrs['data-product-name']
    price = text.attrs['data-price']
    unit = text.attrs['data-unit']
    print(f'id={id} name={name} price={price}')



def find_product_list(page):
    pagecontent = requests.get(page).content
    simple_soup = BeautifulSoup(pagecontent, "html.parser")
    selector = 'div.product-card'
    list_id_products = simple_soup.select(selector)
    #print(list_id_products)
    #selector = 'input'
    #list_contents = [e for e in list_id_products]
    #print(list_contents)
    for e in list_id_products:
        parse_products(e)

def find_pages(link):
    pagecontent = requests.get(link).content
    simple_soup = BeautifulSoup(pagecontent, "html.parser")
    selector = 'div.row div.text-center nav.page-nav ul.pagination li'
    pages = simple_soup.select(selector)

    page_list = list(set([e.select_one('a').attrs['href'] for e in pages]))
    print(page_list)

    for page in page_list:
        print(f' ürün page  = https://www.sanalmarket.com.tr/arama{page}')
        find_product_list(f'https://www.sanalmarket.com.tr/arama{page}')

#Ana sayfadan ürün kategorilerini parse ederek gideceği sayfaları bulur.
def find_categories():
    pagecontent = requests.get('https://www.sanalmarket.com.tr/').content
    simple_soup = BeautifulSoup(pagecontent, "html.parser")
    selector = 'div.menu-under-links div.row  ul.category-list li.category-list-item'
    pages = [e.select_one('a').attrs['href'] for e in simple_soup.select(selector)]
    #print(pages)
    for page in pages:
        print(f' category page  = https://www.sanalmarket.com.tr/{page}')
        #find_product_list(f'https://www.sanalmarket.com.tr/{page}')
        find_pages(f'https://www.sanalmarket.com.tr/{page}')

    #page_list = list(set([e.select_one('a').attrs['href'] for e in pages]))
    #print(page_list)





#print(page_locators.PageLocators.CONTAINER)
#print(simple_soup.find('div.container'))

#find_product_list()
find_pages('https://www.sanalmarket.com.tr/arama?q=seker')
#find_categories()




