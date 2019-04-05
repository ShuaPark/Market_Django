from django.urls import path

from .views import photo_list, PhotoDeleteView,\
     PhotoUploadView, PhotoDetailView, PhotoUpdateView
from .models import Photo

app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='list'),
    path('upload/', PhotoUploadView.as_view(), name='upload'),
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='update'),
]
