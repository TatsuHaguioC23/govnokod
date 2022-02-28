"""from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
mail = "Тут почта"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://mail.rambler.ru/?utm_source=head&utm_campaign=self_promo&utm_medium=header&utm_content=mail')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[5]/div[1]').click()
"""
"""from fake_useragent import UserAgent
ua = UserAgent()
ua.firefox
print(ua.firefox)"""
"""nrk_all = "'article', class_='article'"
soup = BeautifulSoup(url.text, 'html.parser')
for x in nrk_all:
	list_news = soup.findAll(x)
	# Или 
	list_news = soup.findAll(x[0])"""
import re

text = "привет"
count = [i for i in range(len(text))]
print(''.join(text[i].upper() if (i % 2 != 0) else text[i] for i in count))