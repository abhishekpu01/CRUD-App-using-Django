from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.SearchQuestion, name="search"),
    path('show/', views.show, name="show"),
    path('delete/<str:pk>', views.deleteques, name="deleteques"),
    path('update/<str:pk>', views.Updateques, name="updateques"),
    path('delques/', views.ShowDelQues, name="ShowDelQues"),
    path('restoredel/<str:pk>', views.RestoreQues, name="restoredel"),
    path('permdel/<str:pk>', views.permDel, name="permdel"),
]
