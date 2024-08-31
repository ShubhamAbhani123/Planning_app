from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer
from user.models import UserProfile


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(collaborators=self.request.user) | Project.objects.filter(
            creator=self.request.user)

    def perform_create(self, serializer):
        project = serializer.save()
        collaborator_email = self.request.data.get('collaborator_email')
        if collaborator_email:
            try:
                collaborator = UserProfile.objects.get(email__in=collaborator_email)
                project.collaborators.add(collaborator)
            except UserProfile.DoesNotExist:
                pass
