from django.urls import path

from . import views

# Namespace for this app's URLs
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),                                # /polls/
    path('<int:question_id>/', views.detail, name='detail'),            # /polls/N/
    path('<int:question_id>/results/', views.results, name='results'),  # /polls/N/results
    path('<int:question_id>/vote/', views.vote, name='vote'),           # /polls/N/vote
]
