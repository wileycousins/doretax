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
    list_display = ('name', 'link', 'type')
    search_fields = ['name', 'link']

class BusinessDetailAdmin(admin.ModelAdmin):
    list_display = ['name']
    exclude = ['owner']
    readonly_fields = ['name']
    fieldsets = (
        (None, {
            'fields': ('name', 'telephone', 'fax', 'cell', 'email')
        }),
        ('Address', {
            'fields': ('address1', 'address2', 'city', 'state', 'postal_code')
        }),
    )
    

admin.site.register(Association, AssociationAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(BusinessDetail, BusinessDetailAdmin)