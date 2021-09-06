from selenium import webdriver


def news_info():
    news = webdriver.Firefox(
        executable_path='C:\\Users\\avina\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe')
    news.get(
        url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
