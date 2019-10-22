from django.urls import path
from . import views

app_name = "Tasks"

urlpatterns = [
    path('', views.taskView.as_view(), name='task')
]
