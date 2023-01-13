from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service('D:\Installers\chromedriver.exe')
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)

url_main_page = "https://www.labcorp.com/"

driver.get(url_main_page)
careers_element = driver.find_element(By.CSS_SELECTOR, "a.ext")

print(careers_element.text)
careers_element.click()

careers_window = driver.window_handles[1]
driver.switch_to.window(careers_window)

search_bar = driver.find_element(By.CSS_SELECTOR, "div.job-filter input")
search_bar.send_keys("QA Automation Engineer")
search_bar.send_keys(Keys.ENTER)
job_titles = driver.find_elements(By.CSS_SELECTOR, "div.job-title span")
# job_titles = [title.text for title in driver.find_elements(By.CSS_SELECTOR, "div.job-title span")]

print(job_titles)

for title in job_titles:
    print(title.text)
    if title.text.lower().__contains__("automation"):
        title.click()
        break

# try:
#     job_title = driver.find_elements(By.CSS_SELECTOR, "div.job-title span")
# except:
#     pass
# else:
#     for title in job_title:
#         print(title.text)
