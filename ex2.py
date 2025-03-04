import requests
from bs4 import BeautifulSoup

def ex2():
    url = 'https://globalsearch.cuny.edu/CFGlobalSearchTool/CFSearchToolController'

    # in order to manage a "session" / cookies
    with requests.Session() as session:

        # load to main page
        session.get(url)
        form_data = {
            'selectedInstName': 'Queens College |',
            'inst_selection': 'QNS01',
            'selectedTermName': '2024 Fall Term',
            'term_value': '1249',
            'next_btn': 'Next'
        }

        post_response = session.post(url, data=form_data)
        soup = BeautifulSoup(post_response.text, 'html.parser')

        # get the "parent" of the majors
        subject_box = soup.find('select', {'class': 'form-search-display'})



        majors_list = subject_box.find_all('option')[1:]
        majors_list = [(major['value'], major.get_text()) for major in majors_list]

        for major in majors_list:
            print(major)
ex2()
