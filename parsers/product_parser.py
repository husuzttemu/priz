from locators.page_locators import PageLocators

class ProductParser:
    '''
    parse edilmiş satırlar ile initilize edilir...
    '''

    def __init__(self,parent):
        self.product = {}
        self.parent = parent
        self.setProduct()


    def __repr__(self):
        return f' repr id={self.productBarcode} name={self.productName} price={self.productPrice}'

    def __str__(self):
        return f' str id={self.productBarcode} name={self.productName} price={self.productPrice}'

    def setProduct(self):
        self.product['barcode']=self.productBarcode
        self.product['name']=self.productName
        self.product['price']=self.productPrice

    @property
    def getProduct(self):
        return self.product


    @property
    def productBarcode(self):
        text = self.parent.select_one(PageLocators.BARCODE)
        barcode = text.attrs['value']
        return barcode

    @property
    def productName(self):
        text = self.parent.select_one(PageLocators.PRODUCTATTR)
        name = text.attrs['data-product-name']
        return name

    @property
    def productPrice(self):
        text = self.parent.select_one(PageLocators.PRODUCTATTR)
        price = text.attrs['data-price']
        return price

    @property
    def productUnit(self):
        text = self.parent.select_one(PageLocators.PRODUCTATTR)
        unit = text.attrs['data-unit']
        return unit

    @property
    def productCode(self):
        text = self.parent.select_one(PageLocators.PRODUCTMONITOR)
        code = text.attrs['data-monitor-id']
        return code

    @property
    def productMonitorName(self):
        text = self.parent.select_one(PageLocators.PRODUCTMONITOR)
        name = text.attrs['data-monitor-name']
        return name

    @property
    def productCategoryName(self):
        text = self.parent.select_one(PageLocators.PRODUCTMONITOR)
        categoryName = text.attrs['data-monitor-category']
        return categoryName

    @property
    def productPromotionPrice(self):
        text = self.parent.select_one(PageLocators.PROMOTIONPRICE)
        promotionPrice = text.string.strip()
        return promotionPrice






