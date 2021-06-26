from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from termcolor import colored

user_name = input("Enter the profile user name : ").strip()

browser = webdriver.Chrome(ChromeDriverManager().install())

print(colored("Starting ..", color="yellow"))
sleep(1)


browser.get(f"https://instagram.com/{user_name}")
sleep(2)

posts = browser.find_element_by_css_selector(".k9GMp li:first-of-type .g47SY ")
sleep(2)
followrs = browser.find_element_by_css_selector(".k9GMp li:nth-of-type(2) .g47SY ")
sleep(2)
following = browser.find_element_by_css_selector(".k9GMp li:nth-of-type(3) .g47SY ")
sleep(2)

print("Posts\t\t", posts.get_attribute("innerHTML"))
print("Followers\t", followrs.get_attribute("innerHTML"))
print("Following\t", following.get_attribute("innerHTML"))

sleep(1)

browser.quit()