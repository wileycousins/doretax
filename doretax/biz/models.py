from django.db import models

class Association(models.Model):
    ASSOCIATION_TYPES = (
                         (0, 'Professional'),
                         (1, 'Civic and Community'), 
                         )
    name = models.CharField(max_length=100)
    type = models.SmallIntegerField(choices=ASSOCIATION_TYPES)
    
    def __unicode__(self):
        return self.name
    
    
class AssocAppointment(models.Model):
    association = models.ForeignKey(Association)
    position = models.CharField(max_length=100)
    start_year = models.SmallIntegerField(null=True, blank=True)
    end_year = models.SmallIntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    
    def __unicode__(self):
        return self.position
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
class Links(models.Model):
    LINK_TYPES = (
                  (0, 'Community'),
                  (1, 'Client'), 
                  )
    name = models.CharField(max_length=100)
    link = models.URLField()
    kind = models.SmallIntegerField(choices=LINK_TYPES)
    description = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return link
    
class ContactInfo(models.Model):
    email = models.EmailField()
    #telephone = models
    #fax = models
    #cell = models
    #address = models
    