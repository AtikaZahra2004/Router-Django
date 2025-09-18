from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
import io
from django.views.decorators.csrf import csrf_exempt    
from django.forms.models import model_to_dict


# VIEWS..... 
from rest_framework import viewsets
class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer                            
                     
                            
    
        

    


