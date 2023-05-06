from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addItem/', views.add_item),
    path('delete/<int:id>', views.delete_item),
    path('edit/<int:id>', views.edit_item)
]