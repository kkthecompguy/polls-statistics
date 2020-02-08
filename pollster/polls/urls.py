from django.urls import path
from . import views

app_name='polls'

urlpatterns = [
  path('', views.index, name='index'),
  path('<str:question_id>/', views.details, name='details'),
  path('<str:question_id>/vote/', views.vote, name='vote'),
  path('<str:question_id>/results/', views.results, name='results'),
  path('<str:question_id>/result_data/', views.resultData, name='result_data'),
]
