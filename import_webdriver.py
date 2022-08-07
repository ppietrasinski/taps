from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://fabrykatestow.pl')
time.sleep(3)
driver.close()
