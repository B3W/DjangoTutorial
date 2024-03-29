from django.urls import path

from . import views

# Namespace for this app's URLs
app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),                       # /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),            # /polls/N/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # /polls/N/results
    path('<int:question_id>/vote/', views.vote, name='vote'),                # /polls/N/vote
]
