from django.urls import path, include
from .views import PassageListView, PassagePostView
#from app_rest import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register("/list", views.articleViewSet))

urlpatterns = [
    #path("", include(router.urls)),
    path('passage/', PassageListView.as_view()),
    path('passage/<int:passageID>/', PassageListView.as_view()),
    path('new_passage/', PassagePostView.as_view()),
]