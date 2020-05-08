from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https:// ... ")

search = driver.find_element_by_id("id_name")  # on web_page searh input
search.send_keys("some word_key")

search_button = driver.find_element_by_xpath("xpath_of_element")
search_button.click()

#  for checking , we are on correct web_page or not
assert "some word_key" in driver.title

driver.quit()
