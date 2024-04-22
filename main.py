from selenium import webdriver
from PIL import Image
from io import BytesIO
from time import sleep


def get_screenshot(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
    sleep(3)
    width = driver.execute_script("return document.body.scrollWidth")
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(width, height)
    screen = driver.get_screenshot_as_png()
    driver.quit()
    img = Image.open(BytesIO(screen))
    return img

url = input("Link: ")
screen = get_screenshot(url)
if screen:
    screen.show()