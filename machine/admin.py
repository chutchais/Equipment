from django.contrib import admin

# Register your models here.
from .models import Log
from .models import Pm
from .models import Machine
from .models import Machine_type


class MachineTypeAdmin(admin.ModelAdmin):
    search_fields = ['name','description']
    list_filter = ['name']
    list_display = ('name','description')
    fieldsets = [
        (None,               {'fields': ['name','description','user']}),
    ]
admin.site.register(Machine_type,MachineTypeAdmin)


class MachineAdmin(admin.ModelAdmin):
    search_fields = ['name','model','description']
    list_filter = ['status','name','machine_type']
    list_display = ('name','machine_type','model','description','status')
    fieldsets = [
        (None,               {'fields': ['name','machine_type','status','model','description','user']}),
    ]
admin.site.register(Machine,MachineAdmin)


class LogAdmin(admin.ModelAdmin):
    search_fields = ['machine','comment']
    list_filter = ['machine__machine_type','created_date','action','machine__name']
    list_display = ('machine','action','created_date','finished_date','comment')
    fieldsets = [
        (None,               {'fields': ['machine','action','finished_date','comment','user']}),
    ]
admin.site.register(Log,LogAdmin)


class PmAdmin(admin.ModelAdmin):
    search_fields = ['machine','description']
    list_filter = ['status','machine__machine_type','machine__name']
    list_display = ('machine','description','planed_date','finished_date','status')
    fieldsets = [
        (None,               {'fields': ['machine','description','planed_date','finished_date','status','user']}),
    ]
admin.site.register(Pm,PmAdmin)