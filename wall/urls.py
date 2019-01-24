from django.urls import path
from wall import views

app_name = "wall"


urlpatterns = [
    path('', views.home_page, name="home_page"),
]
