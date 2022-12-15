import converter
from ecommerce.shipping import calc_shipping

#We can also import a specific function
from converter import lbs_to_kgs
from utils import find_max

#########################################      Modules
#instead of having these functions here, we can make a "converter" module and then import the functions
# def lbs_to_kgs(weight):
#     return weight * 0.45


# def kgs_to_lbs(weight):
#     return weight / 0.45

print(converter.lbs_to_kgs(190))
lbs_to_kgs(100)

#Exercise test
print(find_max([1, 2, 3, 4, 60, 2, 1, 54, 5]))

calc_shipping()


#########################################      Packages 

