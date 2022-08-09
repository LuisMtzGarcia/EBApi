from django.shortcuts import render

import requests

#############
# FUNCTIONS #
#############

def make_request(url):
    """Generates a response."""

    headers = {
        'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response = response.json()
        return response

#########
# VIEWS #
#########

def properties(request, page=1):
    """Lists a page of properties."""

    url = f'https://api.stagingeb.com/v1/properties?page={page}&limit=15&search%5Bstatuses%5D%5B%5D=published'

    response = make_request(url)

    # Obtains the number of the following page.
    # Reads the url from the response and splits it to obtain the number of the 
    # page.
    # If there isn't a next page, it returns None.
    next_page = response['pagination']['next_page']
    if next_page:
        next_page = next_page.split('&')
        next_page = next_page[1].split('=')
        next_page = next_page[1]

    # Obtains the previous page number.
    previous_page = page - 1
    if previous_page == 0:
        previous_page = None

    context = {
        'properties': response['content'], 
        'next_page': next_page,
        'previous_page': previous_page,
    }

    return render(request, 'EBApi/properties.html', context)
