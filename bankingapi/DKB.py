from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bankingapi.parser.parserDKB import DKBParser
from bankingapi.exceptions.ItemNotFoundError import ItemNotFoundError
import time


class Api:
    browser = None

    def __init__(self):
        pass

    def init_api(self, credentials):
        """
        Opens up selenium geckodriver with page "https://www.dkb.de/banking" and enters credentials for logging in
        """
        self.browser = webdriver.Firefox()
        self.browser.get("https://www.dkb.de/banking")
        username, password = credentials
        username_field = self.browser.find_element_by_id("loginInputSelector")
        username_field.send_keys(username + Keys.TAB + password)
        time.sleep(0.5)
        self.browser.find_element_by_id("buttonlogin").click()

    def close_browser(self):
        """
        Closes browser and exits running state of API
        """
        return self.browser.close()

    def fetch_balance(self):
        """
        Returns:
            string
            Balance in plain string formatted with "," for cent amounts
        """
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
        """Fetch all transactions
        Returns:
            Array with all pages. Each Page-array contains tuple structured like following: (date, description, amount)
        Examples:
            for transaction_page in fetch_all_transactions():
                for transaction in transaction_page:
                    print(transaction) # returns tuple with date, description and amount
        """
        links = self.browser.find_elements_by_tag_name("a")
        time.sleep(0.5)
        for link in links:
            try:
                if link.text == "Umsätze":
                    link.click()
                    break
            except:
                pass
                raise ItemNotFoundError(
                    "Link with text 'Umsätze' could not be found")
        return DKBParser().parse_table(self.browser)


Api()
