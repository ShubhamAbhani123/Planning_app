from django.contrib import admin

import positions.models as models


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'title', 'salary_budget')
    list_filter = ('project', 'id', 'title', 'salary_budget')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Position, PositionAdmin)
