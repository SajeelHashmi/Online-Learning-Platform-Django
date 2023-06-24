from django.urls import path
from . import views
urlpatterns = [
    path('', views.notifications, name='notifications'),
    path('<int:id>', views.markAsRead, name='markAsRead'),

]
