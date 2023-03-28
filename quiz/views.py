from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Quizzes, Question
from .serializers import QuizzesSerializer, RandomQuestionSerializer, QuestionSerializer


# Create your views here.

class Quiz(generics.ListAPIView):
    serializer_class = QuizzesSerializer
    queryset = QuizzesSerializer.Meta.model.objects.all()


class RandomQuestion(APIView):
    """Single Quiz Question"""
    @staticmethod
    def get(request, **kwargs):
        question = RandomQuestionSerializer.Meta.model.objects.filter(quiz__title=kwargs['topic']).order_by("?")[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    """All Quiz Question"""
    @staticmethod
    def get(request, **kwargs):
        question = RandomQuestionSerializer.Meta.model.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
