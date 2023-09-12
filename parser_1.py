import time
# from seleniumbase import SB

# with SB(headed=True) as driver:
#   driver.open('https://mgroup-spb.ru/')
#   driver.click('#menu-item-1276')
#   driver.click("input#kmcf7-text-247bmepYdgA")
#   driver.type("input#kmcf7-text-247bmepYdgA", "Egor")
#   self.type("input#id_value", "2012")

# a[name*="partial_name"]
# id="kmcf7-text-247bmepYdgA"

""" test_fail.py """
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

# class MyTestClass(BaseCase):
#   def test_find_army_of_robots_on_xkcd_desert_island(self):
#     self.open("https://mgroup-spb.ru/")
#     self.click('#menu-item-1276')
#     self.click('span[class*="text-247"]')
#     self.type("input[name*='text-247']", "Egor")

class MyTestClass(BaseCase)
  def find_name_of_park(self):
    self.open("https://mgroup-spb.ru/")
    self.click('#menu-item-1276')