#import libraries

from search_engine.engine import Engine

from pymongo import MongoClient 1n14 1111111111

from locators import page_locators

#print(pagecontent)


#print(simple_soup)

'''
def parse_products(e):
    #xyz = BeautifulSoup(text, "html.parser")
    text = e.select_one("input.product_id")
    id = text.attrs['value']
    text = e.select_one("form.basket-process")
    name = text.attrs['data-product-name']
    price = text.attrs['data-price']
    unit = text.attrs['data-unit']
    print(f'id={id} name={name} price={price}')
'''




#Ana sayfadan ürün kategorilerini parse ederek gideceği sayfaları bulur.


    #page_list = list(set([e.select_one('a').attrs['href'] for e in pages]))
    #print(page_list)





#print(page_locators.PageLocators.CONTAINER)
#print(simple_soup.find('div.container'))

#find_product_list()
#find_pages('https://www.sanalmarket.com.tr/arama?q=komili')

myEngine = Engine()

print(myEngine.__doc__)
#myEngine.find_products_from_all_categories()
#myEngine.find_pages('https://www.sanalmarket.com.tr/arama?q=komili')




