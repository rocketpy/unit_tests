from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https:// ... ")

search = driver.find_element_by_id("id_name")
