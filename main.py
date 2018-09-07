from selenium import webdriver
from selenium.webdriver.common.keys import Keys


for i in range(1, 6):
    driver = webdriver.Firefox()
    url = "https://www.usnews.com/best-colleges/rankings/national-universities?_page={}&_mode=table".format(
        i)
    driver.get(url)
    data_rows = driver.find_elements_by_xpath(
        '//tbody[@data-js-id="items"]/tr')

    for row in data_rows:
        try:
            name = row.find_element_by_xpath('.//td[1]/div[1]/a').text
            city = row.find_element_by_xpath('.//td[1]/div[2]').text
            rank = row.find_element_by_xpath(
                './/td[1]/div[3]/span').text.split()[0]
            fee = row.find_element_by_xpath('.//td[2]/div').text
            print '{}| {}| {}| {}'.format(rank, name, city, fee)
        except:
            continue

    driver.close()
