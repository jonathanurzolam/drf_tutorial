from rest_framework import viewsets
from user.models import Customer
from user.serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()