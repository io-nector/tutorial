from django.urls import include, path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('<str:subject_request>',views.subject_view,name='subject_view')
]