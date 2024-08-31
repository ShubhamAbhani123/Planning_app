from rest_framework import viewsets, permissions
from .models import Position
from .serializers import PositionSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Position.objects.filter(project__collaborators=self.request.user) | Position.objects.filter(
            project__creator=self.request.user)
