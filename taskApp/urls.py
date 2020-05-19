from django.urls import path,include
from .models import *
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('format',UserModelViewSet,basename='Format')
urlpatterns = [
	path('json/',include(router.urls),name="router"),
    path('u/',users,name="customers"),
    path('user/<str:id>/',get_user,name="customer"),
    path('login/',loginPage,name="login"),
    path('logout/',logoutUser,name="logout"),
    path('register/',registerPage,name="register"),
    path('',home,name="home"),
    path('create/',customerCreate,name="form"),
    path('api/',api,name="api"),
    path('dashboard/',customerDashboard,name="dashboard"),
    ]