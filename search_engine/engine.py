
import requests
from bs4 import BeautifulSoup
from locators.page_locators import PageLocators
from parsers.product_parser import ProductParser

class Engine:
    """
    ================================================================
    Developend by PRIZ Development team
    it's designed to web scrap for sanalmarket.
    it delivers products from www.sanalmarket.com.tr

    find_products_from_all_categories : Search all products from web site by categories.
    1. Open the web page(sanalmarket)
    2. Find the categories
    3. Open categories page
    4. Find coumt of pages
    5. Opemn propducts pages
    6. Scrap them
    ================================================================
    """
    def __init__(self):
        self.products = []

    def __repr__(self):
        pass

    def __str__(self):
        return

    def find_product_list(self,page):
        pagecontent = requests.get(page).content
        simple_soup = BeautifulSoup(pagecontent, "html.parser")
        selector = PageLocators.PRODUCTSELECTOR
        list_id_products = simple_soup.select(selector)
        # print(list_id_products)
        # selector = 'input'
        # list_contents = [e for e in list_id_products]
        # print(list_contents)
        for e in list_id_products:
            x = ProductParser(e)
            print(x)
            self.products.append(x.getProduct)
            print(f'ürün : {self.products}')

    def find_pages(self,link):
        pagecontent = requests.get(link).content
        simple_soup = BeautifulSoup(pagecontent, "html.parser")
        selector = PageLocators.SEARCHENGINESELECTOR
        pages = simple_soup.select(selector)
        page_list = list(set([e.select_one('a').attrs['href'] for e in pages]))

        for page in page_list:
            print(f' ürün page  = https://www.sanalmarket.com.tr/arama{page}')
            self.find_product_list(f'https://www.sanalmarket.com.tr/arama{page}')

    def find_products_from_all_categories(self):
        pagecontent = requests.get('https://www.sanalmarket.com.tr/').content
        simple_soup = BeautifulSoup(pagecontent, "html.parser")
        selector = PageLocators.SEARCHALLPRODUCTSBYCATEGORIESSELECTOR
        pages = [e.select_one('a').attrs['href'] for e in simple_soup.select(selector)]
        # print(pages)
        for page in pages:
            print(f' category page  = https://www.sanalmarket.com.tr{page}')
            # find_product_list(f'https://www.sanalmarket.com.tr/{page}')
            self.find_pages_from_categories(f'https://www.sanalmarket.com.tr{page}')

    def find_pages_from_categories(self,link):
        pagecontent = requests.get(link).content
        simple_soup = BeautifulSoup(pagecontent, "html.parser")
        selector = 'div.row div.text-center nav.page-nav ul.pagination li'  # PageLocators.SEARCHENGINESELECTOR
        pages = simple_soup.select(selector)
        # print(f'pages : {pages}')
        page_list = list(set([e.select_one('a').attrs['data-page'] for e in pages]))
        print(page_list)

        for page in page_list:
            print(f' ürün page  = {link}?sayfa={page}')
            self.find_product_list(f'{link}?sayfa={page}')
