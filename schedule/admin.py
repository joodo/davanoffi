from django.contrib import admin
from schedule.models import Project, Schedule

class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [ScheduleInline]

admin.site.register(Project, ProjectAdmin)
