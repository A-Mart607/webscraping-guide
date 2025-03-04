import time

from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the WebDriver (you may need to download the appropriate driver, e.g., ChromeDriver)
driver = webdriver.Chrome()  # You can use Firefox or another browser as needed
driver.get('https://leetcode.com/u/kickinandrew/')

# wait for page to load
time.sleep(5)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()


# Now you can use BeautifulSoup as usual
selector = 'div[class="absolute inset-0"]'
problemsSolved = soup.select_one(selector)

selector ='span[class="text-[30px] font-semibold leading-[32px]"]'
problemsSolved = problemsSolved.select_one(selector)

problemsSolved = problemsSolved.getText()

# now get name
selector = 'div[class="text-label-1 dark:text-dark-label-1 break-all text-base font-semibold"]'
getName = soup.select_one(selector).getText()

print(f"{getName} has solved {problemsSolved} problems")

# get the problem break down
selector = 'div[class="flex h-full w-[90px] flex-none flex-col gap-2"]'
problemBank = soup.select_one(selector)

# break it down further
selector = 'div[class="text-sd-foreground text-xs font-medium"]'
problems = problemBank.select(selector)
problems = [problem.getText() for problem in problems]

print(
    f"{getName} has solved\n"
    f"{problems[0]} easies\n"
    f"{problems[1]} mediums\n"
    f"{problems[2]} hards\n"
)
