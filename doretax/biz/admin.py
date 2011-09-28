from biz.models import Association, AssocPosition, Service, Link, BusinessDetail
from django.contrib import admin

class AssocPositionInline(admin.TabularInline):
    model = AssocPosition
    extra = 1
    
class AssociationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'link')
    search_fields = [
                     'name', 'link', 
                     'assocposition__position',
                     'assocposition__start_year',
                     'assocposition__end_year',
                     ]
    inlines = [AssocPositionInline]

class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['name']

class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'kind')
    search_fields = ['name', 'link']

class BusinessDetailAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ('name', 'owner')
    fieldsets = (
        (None, {
            'fields': ('name', 'owner', 'email', 'telephone', 'fax', 'cell')
        }),
        ('Address', {
            'fields': ('address', 'city', 'state', 'postal_code')
        }),
    )
    

admin.site.register(Association, AssociationAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(BusinessDetail, BusinessDetailAdmin)