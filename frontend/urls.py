from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.ListData.as_view(),name ="list_data"),
]
