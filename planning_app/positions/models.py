from django.db import models
from projects.models import Project


class Position(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='positions')
    title = models.CharField(max_length=255)
    salary_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - {self.project.name}"
