from wsgiref import validate
from rest_framework import serializers
from .models import Question, Evaluation

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class GetQuestionsSerializer(serializers.ModelSerializer):
    qNum = serializers.IntegerField()
    qTypeList = serializers.ListField(
      child=serializers.BooleanField()
    )
      
    class Meta:
        model = Question
        fields = ('qNum', 'qTypeList')

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'