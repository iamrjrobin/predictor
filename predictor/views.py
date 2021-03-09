import spacy
from django.shortcuts import render
from google_trans_new import google_translator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializer import PredictorSerializer
from rest_framework import viewsets



class PredictorViewSet(viewsets.ModelViewSet):
    serializer_class = PredictorSerializer

    # @swagger_auto_schema(
    # manual_parameters=[
    #     openapi.Parameter("Name", openapi.IN_QUERY, type=openapi.TYPE_STRING),])
    
    @permission_classes((AllowAny,))
    def create(self, request, *args , **kwargs):
        if request.method == 'POST':
            # data = request.query_params.get('Name')
            # ser = PredictorSerializer(data=data)
            serializer = self.get_serializer(data=request.data)
            # str = input("Enter a single noun: ") 
            if serializer.is_valid():
                str = serializer.validated_data.get('name')
                translator = google_translator()
                nlp = spacy.load("en_core_web_sm")
                translate_text = translator.translate(str, lang_tgt='en')
                doc = nlp(translate_text)
                for ent in doc:
                    # print(doc, ent.pos_)
                    value = (ent.pos_)
                print(value)
                if (value!='NOUN'):
                    print("This is not a noun")
                    return Response(f"{str} This is not a noun")
                else: 
                    print(f"{str}: The {translate_text}")
                    return Response(f"{str}: The {translate_text}")