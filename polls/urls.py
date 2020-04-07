from django.urls import path
from . import views

# Create URLs Mapping for polls module.
app_name = 'polls'

urlpatterns = [
    # Path: /polls/
    path('', views.index, name="index"),
    # Path => /polls/5/
    path('<int:question_id>/', views.detail, name="detail"),
    # Path => /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # Path => /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
