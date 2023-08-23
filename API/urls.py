from django.urls import path,include
from API import views
urlpatterns = [
    
    path('index/',views.UserDetailApi.as_view(),name='index'),
    path('company/',views.UserCompanyApi.as_view(),name='company'),
    path('company/<int:pk>/',views.UserCompanyApi.as_view(),name='company'),


]