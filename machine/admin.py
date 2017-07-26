from django.contrib import admin

# Register your models here.
from .models import Log
from .models import Ticket
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


class MachineTicketInline(admin.TabularInline):
    model = Ticket
    extra = 1

class MachinePmInline(admin.TabularInline):
    model = Pm
    extra = 1

class MachineAdmin(admin.ModelAdmin):
    search_fields = ['name','model','description']
    list_filter = ['status','machine_type']
    list_display = ('name','machine_type','model','description','status')
    fieldsets = [
        (None,               {'fields': ['name','machine_type','status','model','description','user']}),
    ]
    inlines = [MachinePmInline,MachineTicketInline]

admin.site.register(Machine,MachineAdmin)


class TicketLogline(admin.TabularInline):
    model = Log
    extra = 1

class TicketAdmin(admin.ModelAdmin):
    search_fields = ['machine__name','symptom','description']
    list_filter = ['status','machine__machine_type','machine__name']
    list_display = ('machine','symptom','created_date','ack_date','target_date','status')
    fieldsets = [
        (None,               {'fields': ['machine','symptom','description','status','ack_date','target_date','finished_date']}),
    ]
    inlines = [TicketLogline]
    
admin.site.register(Ticket,TicketAdmin)

class LogAdmin(admin.ModelAdmin):
    search_fields = ['comment']
    list_filter = ['ticket__machine__machine_type','log_type','ticket__machine__name']
    list_display = ('ticket','log_type','comment','modified_date','user')
    fieldsets = [
        (None,               {'fields': ['ticket','log_type','comment','user']}),
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