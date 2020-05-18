from django.urls import path,include
from .models import *
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('model',UserModelViewSet,basename='userviewset')
urlpatterns = [
	path('l/',include(router.urls)),
    path('u/',users,name="customers"),
    path('user/<str:id>',get_user),
    path('login/',loginPage,name="login"),
    path('logout/',logoutUser,name="logout"),
    path('register/',registerPage,name="register"),
    ]