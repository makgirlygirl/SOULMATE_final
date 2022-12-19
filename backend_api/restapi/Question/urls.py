from django.urls import path, include
from .views import QuestionListView, QuestionPostView, EvaluationListView, EvaluationPostView, QuestionDOCXView
#from app_rest import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register("/list", views.articleViewSet))

urlpatterns = [
    #path("", include(router.urls)),
    path("question", QuestionListView.as_view()),
    path("question/", QuestionListView.as_view()),
    path("new_question", QuestionPostView.as_view()),
    path("new_question/", QuestionPostView.as_view()),
    path("evaluation", EvaluationListView().as_view()),
    path("new_evaluation", EvaluationPostView().as_view()),
    path("get_docx", QuestionDOCXView().as_view())
]