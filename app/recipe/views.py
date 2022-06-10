"""Views for recipe api"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """View for managing recipe API """
    serializer_class=serializers.Serializer.RequestSerializer
    queryset=Recipe.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        """Retrive recipes for authenticated user"""
        return self.queryset.filter(username=self.request.user).order_by('-id')
