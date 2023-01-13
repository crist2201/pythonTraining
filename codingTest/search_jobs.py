from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_driver_path = Service('D:\Installers\chromedriver.exe')
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)

url_main_page = "https://www.labcorp.com/"
user_job = "QA Test Automation Developer"

class Labcorp:
    def __init__(self):
        self.path = Service('D:\Installers\chromedriver.exe')
        self.option = Options()
        self.option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.path, options=self.option)

    def main_page(self):
        self.driver.get(url_main_page)

    def go_to_careers(self):
        careers_element = self.driver.find_element(By.CSS_SELECTOR, "a.ext")
        careers_element.click()
        careers_window = self.driver.window_handles[1]
        self.driver.switch_to.window(careers_window)

    def search_jobs(self, job):
        search_bar = self.driver.find_element(By.CSS_SELECTOR, "div.job-filter input")
        search_bar.send_keys(job)
        search_bar.send_keys(Keys.ENTER)


        # return self.driver.find_elements(By.CSS_SELECTOR, "div.job-title span")

        # self.select_job(job)

    def select_job(self, job):
        jobs = self.driver.find_elements(By.CSS_SELECTOR, "span[role=heading] a.au-target")
        # jobs = self.driver.find_elements(By.CSS_SELECTOR, "div.job-title span")
        for title in jobs:
            print(title.text)
            if title.text.lower() == job.lower():
                title.click()
                break
            #     break
            # print(title.text)
            #
            #     title.click()


lab = Labcorp()
lab.main_page()
lab.go_to_careers()
lab.search_jobs(job=user_job)
# print(all_jobs)
lab.select_job(job=user_job)





# driver.get(url_main_page)
# careers_element = driver.find_element(By.CSS_SELECTOR, "a.ext")
#
# print(careers_element.text)
# careers_element.click()
#
# careers_window = driver.window_handles[1]
# driver.switch_to.window(careers_window)

# search_bar = driver.find_element(By.CSS_SELECTOR, "div.job-filter input")
# search_bar.send_keys("QA Automation Engineer")
# search_bar.send_keys(Keys.ENTER)

# job_titles = [title.text for title in driver.find_elements(By.CSS_SELECTOR, "div.job-title span")]

# def selectJob():
#     driver.find_element(By.CSS_SELECTOR, "span.job-category")
#     driver.find_element(By.CSS_SELECTOR, "span.job-location")
#     driver.find_element(By.CSS_SELECTOR, "span.jobId span")
#     driver.find_element(By.CSS_SELECTOR, "span.au-target")
#     driver.find_element(By.CSS_SELECTOR, "")
#
#     pass



