from rest_framework import serializers
from .models import Project
from user.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    collaborators = UserSerializer(many=True, read_only=True)
    remaining_budget = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'creator', 'collaborators', 'total_budget', 'remaining_budget', 'created_at',
                  'updated_at']

    def get_remaining_budget(self, obj):
        utilized_budget = sum(position.salary_budget for position in obj.positions.all())
        return obj.total_budget - utilized_budget

    def create(self, validated_data):
        creator = self.context['request'].user
        project = Project.objects.create(creator=creator, **validated_data)
        return project
