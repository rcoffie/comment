
from django.urls import path
from .import views 
urlpatterns = [
  path('',views.Home,name='home'),
  path('<int:id>/',views.PostDetail,name='detail')
    
]
