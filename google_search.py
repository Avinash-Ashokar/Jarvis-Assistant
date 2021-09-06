from selenium import webdriver


def search(val):
    browser = webdriver.Firefox(
        executable_path='C:\\Users\\avina\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe')
    browser.get(url="https://www.google.com/")
    s = browser.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
    s.click()
    s.send_keys(val)
    s.send_keys('\ue007')
