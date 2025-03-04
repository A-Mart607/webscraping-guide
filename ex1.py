import requests
from bs4 import BeautifulSoup

def ex1():
    url = 'https://globalsearch.cuny.edu/CFGlobalSearchTool/CFSearchToolController'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # success!
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # "index" into checkboxes
        checkboxes=soup.find('ul', class_='checkboxes')

        # get a list of colleges as li's
        colleges = checkboxes.find_all('li')

        # strip them 1 by 1
        for college in colleges:
            print(college.getText())
ex1()