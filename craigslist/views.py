from django.shortcuts import render
import requests

def project_home(request):
    """Go to index route, return home template"""
    return render(request, 'project-home.html')

def home(request):
    """Go to craigslist index, return index template"""
    return render(request, 'craigslist/home.html')

def new_search(request):
    """Show template to perform search"""
    return render(request, 'craigslist/new-search.html')

def search_results(request):
    """Send search results"""
    base_url = 'https://jacksonville.craigslist.org/search/sss?query={}'
    try:
        search_terms = request.POST['search-terms']
    except KeyError:
        search_terms = 'python tutor'
    else:
        results = requests.get(base_url.format(search_terms))
        print(results.content)
        results = '123456'
        return render(request, 'craigslist/search-results.html', {'search_results': results})
