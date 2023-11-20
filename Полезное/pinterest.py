import time

import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def start():
    driver = webdriver.Chrome()
    driver.get(url='https://www.pinterest.com/')
    time.sleep(15)
    button = driver.find_element(By.CSS_SELECTOR, 'tBJ dyH iFc sAJ xnr tg7 H2s').click()
    time.sleep(3)
    driver.quit()
    driver.close()




def main():
    start()


if __name__ == '__main__':
    main()