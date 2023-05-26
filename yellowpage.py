import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import argparse

parser = argparse.ArgumentParser(description='YellowPage Scraper')
parser.add_argument("url", help="URL to scrape")
url = parser.parse_args()
print(url.url)


class YellowPage:

    def __init__(self):
        self.url = url.url
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1500,1000")
        self.driver = webdriver.Chrome(options = self.options)
        print("init")


    def browser(self):
        self.driver.get(self.url)
        sleep(5)
        print('got url')


    def scrape(self):

        data = []

        while True:
            Title = self.driver.find_elements_by_xpath('//a[@class="listing__name--link listing__link jsListingName"]')
            Phone = self.driver.find_elements_by_xpath('//a[@class="mlr__item__cta jsMlrMenu"]')

            for title,phone in zip(Title,Phone):

                title_and_phone = []
                title_and_phone.append(title.text)

                phone_val = phone.get_attribute('data-phone')
                title_and_phone.append(phone_val)

                data.append(title_and_phone)
                print('Data scraped:%s' % title_and_phone)



            next_page = self.driver.find_element_by_link_text('Next >>')

            self.driver.execute_script("arguments[0].scrollIntoView();", next_page)
            next_page.click()

            sleep(5)


if __name__ == "__main__":

    Spider = YellowPage()
    Spider.browser()
    Spider.scrape()
