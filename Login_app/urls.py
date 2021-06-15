from django.urls import include, path
from .import views


urlpatterns = [
    # path('', views.home, name = 'home'),
    path('', views.create, name = 'home'),
    path('delete<int:id>/', views.delete_user, name = 'delete_user'),
    path('<int:id>/', views.update_user, name = 'update_user'),
]
