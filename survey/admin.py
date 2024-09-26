from django.contrib import admin
from .models import NearMissReport

@admin.register(NearMissReport)
class NearMissReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'frequency', 'mitigation')
