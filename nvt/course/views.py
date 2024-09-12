from django.shortcuts import render,get_object_or_404
from .models import Coursetype,Attendcourse
from question.models import UserAnswer
from .serializer import Coursetypeserializer,Attendserializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.response import Response
from background_task import background
import time





# Create your views here.
class CourseViewSets(viewsets.ModelViewSet):
    queryset=Coursetype.objects.all()
    serializer_class=Coursetypeserializer



class AttendenceViewset(viewsets.ModelViewSet):
    queryset=Attendcourse.objects.all()
    serializer_class=Attendserializer



    
    def start(self,request,pk):
           user_instance=request.user
           course_instance=get_object_or_404(Coursetype,id=pk)
           Attendcourse,created=Attendcourse.objects.update_or_create(
             
          user=user_instance,
          course=course_instance,
          defaults={'start_time': timezone.now()}
    )

         
    

    def submit(self,request,pk):
        user_instance=request.user
        course_instance=get_object_or_404(Coursetype,id=pk)
        course_question=course_instance.question.all()
        user_answer=UserAnswer.objects.filter(user=user_instance,question__in=course_question)
        i=0
        for q in user_answer:
                i=i+q.get_result
        Attendcourse.objects.update_or_create(
             
          user=user_instance,
          course=course_instance,
          defaults={'total_number': i}
    )
        
       
        return Response ('your time has over')



  
   

    @background(schedule=30)
    def check_time_over(self,request,pk):
         present_time = timezone.now()
         examinee=request.user
         course_instance=get_object_or_404(Coursetype,id=pk)
         attendcourse_instance=get_object_or_404(Attendcourse,user=examinee,course=course_instance)
         end_time=course_instance.duration+attendcourse_instance.start_time
         if present_time>end_time:
             return self.submit(request, pk)
         return None
              
   
    




    



