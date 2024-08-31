from django.contrib import admin
import projects.models as models


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'creator',
        'total_budget',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'creator',
        'created_at',
        'updated_at',
        'id',
        'name',
        'total_budget',
    )
    raw_id_fields = ('collaborators',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Project, ProjectAdmin)
