from selenium import webdriver
from datetime import datetime
from time import sleep


class DKBParser:

    def __init__(self):
        pass

    def parse_table(self, browser: webdriver.Firefox):
        # step 1 - changing start and end of statistics
        # getting todays date
        today = datetime.now()
        day = str("{:02d}".format(today.day))
        month = str("{:02d}".format(today.month))

        today_string = str(day) + "." + \
            str(month) + "." + str(today.year)
        three_years_ago_string = str(
            day) + "." + str(month) + "." + str(today.year - 3)

        from_date = browser.find_element_by_id(
            "id-1615473160_transactionDate")
        from_date.clear()
        from_date.send_keys(three_years_ago_string)
        to_date = browser.find_element_by_id(
            "id-1615473160_toTransactionDate")
        to_date.clear()
        to_date.send_keys(today_string)

        browser.find_element_by_id("searchbutton").click()

        while len(browser.find_elements_by_class_name("mainRow")) < 1:
            continue

        transactions = []

        transactions.append(self.get_transactions(browser))
        while True:
            try:
                browser.find_element_by_class_name("butNext0").click()
                transactions.append(self.get_transactions(browser))
                sleep(3)
            except:
                print("Can't find next arrow")
                break
        return transactions

    def get_transactions(self, browser: webdriver.Firefox):
        transactions = []
        items = browser.find_elements_by_class_name("mainRow")
        for item in items:
            description = item.find_element_by_class_name(
                "transactionText").text.replace("\n", " ")
            date = item.find_element_by_class_name(
                "transactionDate").text.split("\n")[0]
            amount = item.find_element_by_class_name(
                "alignRight").text
            transactions.append((date, description, amount))
        return transactions
