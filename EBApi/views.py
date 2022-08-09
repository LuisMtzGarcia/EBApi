from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect

from .forms import ContactRequestForm

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

def property_detail(request, id):
    """Displays a property information."""

    url = f"https://api.stagingeb.com/v1/properties/{id}"

    response = make_request(url)

    # Information fields
    public_id = response["public_id"]
    title = response["title"]
    description = response["description"]
    image_url = response["property_images"][0]["url"]
    image_title = response["property_images"][0]["title"]
    property_type = response["property_type"]
    location = response["location"]["name"]
    form = contact_request(request, public_id)

    context = {
        'public_id': public_id,
        'title': title,
        'description': description,
        'image_url': image_url,
        'image_title': image_title,
        'property_type': property_type,
        'location': location,
        'form': form,
    }

    return render(request, 'EBApi/property.html', context)

#########
# FORMS #
#########

def contact_request(request, id):
    """Send a client's contact request."""

    if request.method != 'POST':
        form = ContactRequestForm(initial={'public_id': id})
    else:
        form = ContactRequestForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(JsonResponse(data).content)
            return redirect('EBApi:property', id=id)

    return form