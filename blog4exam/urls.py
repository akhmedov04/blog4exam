from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('blogs/', BlogView.as_view()),
    path('blogs/<int:id>/', MaqolaView.as_view()),
    path('logout/', logoutview),
]
