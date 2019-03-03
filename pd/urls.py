from django.urls import path
from .views import recordListView, recordCreateView, recordDeleteView,recordDetailView
urlpatterns = [
    path('', recordListView.as_view(),name='home'),
    path('new', recordCreateView.as_view(), name='record_new'),
    path('/<int:pk>/delete', recordDeleteView.as_view(), name='record_delete'),
    path('record/<int:pk>', recordDetailView.as_view(), name='record_detail'),
    
]
