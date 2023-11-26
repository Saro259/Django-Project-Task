from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(JobAdListing)
admin.site.register(ApplyJob)

class JobAdListingAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'user')
    actions = None

    def save_model(self, request, obj, form, change) -> None:
        if not obj.user:
            obj.user = request.user
            obj.save()