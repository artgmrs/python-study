from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

path = r"C:\DTI\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://www.instagram.com/")

# login
time.sleep(2)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("username")
password.send_keys("password")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

# redirect to account
driver.get("https://www.instagram.com/lucass.casstro")

time.sleep(2)

# click on first post
first_thumbnail = driver.find_element(
    By.XPATH,
    '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a',
)
first_thumbnail.click()
sleep(2)

# travel on all posts
next_post = "1"
reached_end = False
previous_url = ""
new_url = ""
liked, unlike = 0, 0

while reached_end is not True:
    if liked > 0 or unlike > 0:
        next_post.send_keys(Keys.RIGHT)
        sleep(3)
        new_url = driver.current_url
        if previous_url == new_url:
            reached_end = True

    # if not liked, like <3
    like_button = driver.find_element(
        By.XPATH, "//button//span//*[name()='svg' and @aria-label='Curtir']"
    )
    like = driver.find_element(By.XPATH, "//*[@aria-label='Like']")
    like.click()
    previous_url = driver.current_url
    print("previous url = " + previous_url)
    liked += 1
    next_post = driver.find_element(By.CLASS_NAME, "wpO6b  ")
    print("new url = " + previous_url)

print(str(liked) + " Posts Liked!")
