from django.contrib import admin
from .models import Bank
from import_export.admin import ImportExportModelAdmin

@admin.register(Bank)

class Bank_detail(ImportExportModelAdmin):
	pass
