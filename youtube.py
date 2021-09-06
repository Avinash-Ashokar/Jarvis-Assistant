from selenium import webdriver


def youtube_search(yval):
    youtube = webdriver.Firefox(
        executable_path='C:\\Users\\avina\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe')
    youtube.get(url="https://www.youtube.com/results?search_query=" +yval)