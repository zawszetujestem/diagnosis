from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializer import *
from .models import *


class SymptomsView(ModelViewSet):
    serializer_class = SymptomsSerializer
    queryset = Symptoms.objects.all()


class BoreliaEventsView(ModelViewSet):
    serializer_class = BoreliaEventsSerializer
    queryset = BoreliaEvents.objects.all()


class HealthConditionView(ModelViewSet):
    serializer_class = HealthConditionSerializer
    queryset = HealthCondition.objects.all()
