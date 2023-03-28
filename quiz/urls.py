from django.urls import path

from .views import Quiz, RandomQuestion, QuizQuestion

urlpatterns = [
    path("quiz/", Quiz.as_view(), name="quiz"),
    path("r/<str:topic>/", RandomQuestion.as_view(), name="random"),
    path("<str:topic>/", QuizQuestion.as_view(), name="question"),
]
