from django.shortcuts import render,get_object_or_404
from .models import Question,UserAnswer
from .serializers import Questionserializer,Useranswerserializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

class QuestionViewset(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=Questionserializer
    




class UserAnswerViewset(viewsets.ModelViewSet):
    queryset=UserAnswer.objects.all()
    serializer_class=Useranswerserializer



    @action(detail=True, methods=['post'])
    def submit(self,request,pk):
        question_instance=get_object_or_404(Question,id=pk)
        reply=request.data.get('reply')
        userid=request.user
        user_instance=User.objects.get(id=userid)
        user_answer,created=UserAnswer.objects.update_or_create(

           question=question_instance,
           user=user_instance,
           reply=reply

        )
        if int(reply)==int(question_instance.ans):
             user_answer.get_result=1
             user_answer.save()
             return Response ('your ans is correct')
        else:
             user_answer.get_result=0
             user_answer.save()
             return Response('your ans is wrong')

        

