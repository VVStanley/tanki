from django.urls import path

from test2.views import TestView

urlpatterns = [
    path('', TestView.as_view(), name='test')
]