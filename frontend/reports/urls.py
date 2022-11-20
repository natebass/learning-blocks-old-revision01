from django.urls import path

from . import views

urlpatterns = [
    path('', views.reports)
    # ex: /reports/
    # path('', views.index, name='index'),
    # ex: /reports/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /reports/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /reports/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
