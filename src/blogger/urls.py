from django.urls import path
from blogger import views


urlpatterns = [
    path('', views.index, name='bogger-index'),
    path("art/<int:numart>", views.art),
]