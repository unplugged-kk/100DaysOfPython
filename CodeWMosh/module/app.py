import sys
from ecommerce.shopping.sales import calc_shipping, calc_tax
import ecommerce.shopping.sales

ecommerce.shopping.sales.calc_shipping()
ecommerce.shopping.sales.calc_tax()

calc_tax()
calc_shipping()
print(sys.path)
