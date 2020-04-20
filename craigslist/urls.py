from django.urls import path
from . import views

# used for namespacing urls
app_name = 'craigslist'

urlpatterns = [
    path('', views.home, name="home"),
    path('new-search/', views.new_search, name="new_search"),
    path('search-results/', views.search_results, name="search_results")
]
