# import packages
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin


from .models import Question, Evaluation
from .serializers import QuestionSerializer, GetQuestionsSerializer, EvaluationSerializer
from Passage.serializers import PassageSerializer


# import Question Generator python file to use ML in new_question
import sys
import json
sys.path.append('/home/a1930008/k_sat/')
from k_sat import QuestionGenerate

sys.path.append('/home/a1930008/docxDownload/')
from form import makeDocx
from docx import Document

# APIView for getting questions in 'question' table
class QuestionListView(
  APIView,
  UpdateModelMixin,
  DestroyModelMixin,
):
  
  def get(self, request):
    question_type = self.request.query_params.get('type', None)
    num = self.request.query_params.get('num', None)
    if question_type:
      try:
        if num:
          num = int(num)
          queryset = Question.objects.filter(question_type=question_type)[:num]
        else :
          queryset = Question.objects.filter(question_type=question_type)
      except Question.DoesNotExist:
        return Response({'errors': 'This question type item does not exist.'}, status=400)

    else:    
      queryset = Question.objects.all()

    read_serializer = QuestionSerializer(queryset, many=True)
    d=makeDocx()
    d.__init__()
    d.saveDocx(read_serializer.data)
    response = Response(read_serializer.data) 
    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Methods'] = "GET, OPTIONS"
    response['Access-Control-Max-Age'] = "1000"
    response['Access-Control-Allow-Headers'] = "X-Requested-With, Content-Type"
    return response
    


# APIView for making new questions
class QuestionPostView(
  APIView,
  UpdateModelMixin,
  DestroyModelMixin,
):

  def get(self, request):
    queryset = Question.objects.all()
    read_serializer = QuestionSerializer(queryset, many=True)
    response = Response(read_serializer.data)
    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Methods'] = "GET, OPTIONS"
    response['Access-Control-Max-Age'] = "1000"
    response['Access-Control-Allow-Headers'] = "X-Requested-With, Content-Type"
    return response


  def post(self, request):
    create_serializer = PassageSerializer(data=request.data)  # { "passage":""} 형태로 data를 받음

    if create_serializer.is_valid():
      new_passage = create_serializer.save()
      new_passage_item = PassageSerializer(new_passage).data

      # running AI model
      new_questions = QuestionGenerate(new_passage_item['passageID'], new_passage_item['passage'])
      question_json = new_questions.result()

      # saving docx file
      d=makeDocx()
      d.__init__()
      d.saveDocx(question_json["question_details"])
      response = Response(question_json["question_details"], status=201)

      for qdata in question_json["question_details"]:
        qserializer = QuestionSerializer(data=qdata)
        if qserializer.is_valid():
          new_question = qserializer.save()
          read_qserializer = QuestionSerializer(new_question)
    
    else:
      response = Response(create_serializer.errors, status=400)

    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS"
    response['Access-Control-Max-Age'] = "1000"
    response['Access-Control-Allow-Headers'] = "X-Requested-With, Content-Type"
    return response


# question evaluation
class EvaluationListView(
  APIView,
  UpdateModelMixin,
  DestroyModelMixin,
):
  
  def get(self, request, questionID=None):
    if questionID:
      try:
        queryset = Evaluation.objects.filter(questionID=questionID)
      except Question.DoesNotExist:
        return Response({'errors': 'This question type item does not exist.'}, status=400)

    else:    
      queryset = Evaluation.objects.all()

    read_serializer = EvaluationSerializer(queryset, many=True)
    response = Response(read_serializer.data)
    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Methods'] = "GET, OPTIONS"
    response['Access-Control-Max-Age'] = "1000"
    response['Access-Control-Allow-Headers'] = "X-Requested-With, Content-Type"
    return response

class EvaluationPostView(
  APIView,
  UpdateModelMixin,
  DestroyModelMixin,
):

  def get(self, request):
    queryset = Evaluation.objects.all()
    read_serializer = EvaluationSerializer(queryset, many=True)
    response = Response(read_serializer.data)
    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Methods'] = "GET, OPTIONS"
    response['Access-Control-Max-Age'] = "1000"
    response['Access-Control-Allow-Headers'] = "X-Requested-With, Content-Type"
    return response

  def post(self, request):
    create_serializer = EvaluationSerializer(data=request.data)

    if create_serializer.is_valid():
      eval_object = create_serializer.save()
      read_serializer = EvaluationSerializer(eval_object)
      response = Response(read_serializer.data, status=201)
    
    else:
      response = Response(create_serializer.errors, status=400)
      
    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS"
    response['Access-Control-Max-Age'] = "1000"
    response['Access-Control-Allow-Headers'] = "X-Requested-With, Content-Type"
    return response


# when user click docx download button, use this api
# it automatically downloads download.docx file in our server
class QuestionDOCXView(
  APIView,
  UpdateModelMixin,
  DestroyModelMixin,
):
  
  def get(self, request):
    document=Document('/home/a1930008/docxDownload/download.docx')

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachement; filename=download.docx'
    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Methods'] = "GET, OPTIONS"
    response['Access-Control-Max-Age'] = "1000"
    response['Access-Control-Allow-Headers'] = "X-Requested-With, Content-Type"
    document.save(response)
    return response