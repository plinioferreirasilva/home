from rest_framework import viewsets
from .models import AutomationEvent
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = AutomationEvent.objects.all()
    serializer_class = EventSerializer
