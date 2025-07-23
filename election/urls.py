from django.urls import path

from . import views
from .views import election_list, election_detail , election_results

urlpatterns = [
    path('', election_list, name='election_list'),
    path('<int:election_id>/', election_detail, name='election_detail'),
    path('<int:election_id>/results/', views.election_results, name='election_results'),
    path('my-votes/', views.my_votes, name='my_votes'),


]
