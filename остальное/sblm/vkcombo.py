from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://nftines.city-mobil.ru/')
driver.maximize_window() # For maximizing window
driver.implicitly_wait(5) # gives an implicit wait for 20 seconds
target = driver.find_element_by_xpath('/html/body/div[6]/div[1]')
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[2]/div[2]/div[2]/div/img').click()
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[3]/svg[4]').click()
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[3]/div[2]/input').sendKeys('gapsotespi@yevme.com')