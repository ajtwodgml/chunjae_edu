from django.urls import path
# from articles import views
from . import views
urlpatterns = [
    # path('',views.data),
    # path('json-data/',views.json_data),
    # path('name/<str:name>/',views.str_data),
    # path('create/', views.create),
    # path('read/',views.read),
    # path('read/<int:id>/', views.read_single),
    path('',views.article_list),
    path('<int:id>/',views.article_detail)
]
