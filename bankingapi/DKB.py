from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .parser.parserDKB import DKBParser
import time


class Api:
    browser = None

    def __init__(self):
        pass

    def init_Api(self, credentials):
        self.browser = webdriver.Firefox()
        self.browser.get("https://www.dkb.de/banking")
        username, password = credentials
        username_field = self.browser.find_element_by_id("loginInputSelector")
        username_field.send_keys(username + Keys.TAB + password)
        time.sleep(0.5)
        self.browser.find_element_by_id("buttonlogin").click()

    def close_browser(self):
        return self.browser.close()

    def fetch_balance(self):
        amounts = self.browser.find_elements_by_class_name("amount")
        while 1:
            try:
                amounts = self.browser.find_elements_by_class_name(
                    "amount")
                if (amounts[-1].text != None):
                    break
            except:
                time.sleep(0.2)
                continue
        saldo_over_all = amounts[-1].text
        return saldo_over_all

    def fetch_all_transactions(self):
        links = self.browser.find_elements_by_tag_name("a")
        time.sleep(0.5)
        for link in links:
            try:
                if link.text == "Umsätze":
                    link.click()
            except:
                pass
        DKBParser().parse_table(self.browser)
        pass


Api()
