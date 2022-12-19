from django.urls import path, include
from .views import PassageListView, PassagePostView
from rest_framework import routers

urlpatterns = [
    path('passage/', PassageListView.as_view()),
    path('passage/<int:passageID>/', PassageListView.as_view()),
    path('new_passage/', PassagePostView.as_view()),
]