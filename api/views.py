from rest_framework import viewsets
from .models import Phone
from .serializers import PhoneSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all().order_by('-created_at')
    serializer_class = PhoneSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            # Filter case-insensitive match for name
            queryset = queryset.filter(name__iexact=name)
        return queryset
