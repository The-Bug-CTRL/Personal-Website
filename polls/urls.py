from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='polls_page'),  # Updated name to 'polls_page'
    path('user_auth', views.index, name='user_auth'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]