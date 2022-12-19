#from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Passage
from .serializers import PassageSerializer

# Create your views here.

class PassageListView(
  APIView,
  UpdateModelMixin,
  DestroyModelMixin,
):
  
  def get(self, request, passageID=None):
    if passageID:
      try:
        queryset = Passage.objects.get(passageID=passageID)
      except Passage.DoesNotExist:
        return Response({'errors': 'This passage item does not exist.'}, status=400)
      read_serializer = PassageSerializer(queryset)
      return Response(read_serializer.data)

    else :
      queryset = Passage.objects.all()
      read_serializer = PassageSerializer(queryset, many=True)

      return Response(read_serializer.data)


class PassagePostView(
  APIView,
  UpdateModelMixin,
  DestroyModelMixin,
) :

  def get(self, request):
    queryset = Passage.objects.all()
    read_serializer = PassageSerializer(queryset, many=True)

    return Response(read_serializer.data)


  def post(self, request):
    create_serializer = PassageSerializer(data=request.data)

    if create_serializer.is_valid():

      passage_item_object = create_serializer.save()
      read_serializer = PassageSerializer(passage_item_object)
      return Response(read_serializer.data, status=201)

    return Response(create_serializer.errors, status=400)
