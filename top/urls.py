from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('top', views.top, name='top'),
    path('refrigerator', views.refrigerator, name='refrigerator'),
    path('ingredient', views.ingredient, name='ingredient'),
    path('ingredient/<int:num>/', views.ingredient, name='ingredient'),
    path('search', views.search, name='search'),
    path('regist', views.regist, name='regist'),
    path('dishes', views.dishes, name='dishes'),
    path('dishschedule', views.dishschedule, name='dishschedule'),
    path('components', views.components, name='components'),
    path('project', views.project, name='project'),
]