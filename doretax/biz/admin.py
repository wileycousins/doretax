from biz.models import Association, AssocPosition, Service, Link, ContactInfo
from django.contrib import admin

class AssocPositionInline(admin.TabularInline):
    model = AssocPosition
    extra = 1
    
class AssociationAdmin(admin.ModelAdmin):
    inlines = [AssocPositionInline]

admin.site.register(Association, AssociationAdmin)
admin.site.register(Service)
admin.site.register(Link)
admin.site.register(ContactInfo)