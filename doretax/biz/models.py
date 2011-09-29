from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField, USPostalCodeField
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.contrib.auth.models import User


class AssociationManager(models.Manager):
    def professional(self):
        return self.get_query_set().filter(type='prof')
    
    def civic(self):
        return self.get_query_set().filter(type='civic')

class Association(models.Model):
    """
    A civic or professional association.
    e.g. Chamber of Commerce, National Society of Pencil Sharpeners, etc. 
    """
    ASSOCIATION_TYPES = (
                         ('civic', 'Civic and Community'),
                         ('prof', 'Professional'), 
                         )
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=5, choices=ASSOCIATION_TYPES)
    link = models.URLField(null=True, blank=True, help_text="(optional)")
    objects = AssociationManager()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['type', 'name']    
    
class AssocPosition(models.Model):
    """
    A position held at an association.
    e.g. CSO (Chief Sharpening Officer) 
    """
    association = models.ForeignKey(Association)
    position = models.CharField(max_length=100)
    start_year = models.SmallIntegerField("Year you started this position", null=True, blank=True, help_text="(optional)")
    end_year = models.SmallIntegerField("Year you ended this position", null=True, blank=True, help_text="(optional) if you currently hold this position, leave blank")
    
    def __unicode__(self):
        return self.position
    
    class Meta:
        unique_together = ('association', 'position', 'start_year', 'end_year')
        ordering = ['association', 'start_year']
        verbose_name = "Association Position"
        verbose_name_plural = "Association Position"
    
class Service(models.Model):
    """
    A service provided.
    e.g. Individual and Business pencil sharpening, Payroll Services, etc.
    """
    name = models.CharField(max_length=100, unique=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class LinkManager(models.Manager):
    def client(self):
        return self.get_query_set().filter(kind='client')
    
    def community(self):
        return self.get_query_set().filter(kind='community')
    
class Link(models.Model):
    """
    A client or community link with a name and optional description.
    e.g. Where's my refund?, Movies made locally, etc.
    """
    LINK_TYPES = (
                  ('client', 'Client'),
                  ('community', 'Community'), 
                  )
    name = models.CharField(max_length=100, unique=True)
    link = models.URLField()
    kind = models.CharField(max_length=9, choices=LINK_TYPES)
    description = models.TextField(blank=True, null=True, help_text="(optional)")
    objects = LinkManager()
    
    def __unicode__(self):
        return self.link
    
    class Meta:
        ordering = ['kind', 'name']

class BusinessDetail(models.Model):
    """
    A basic sole proprietor business detail.
    """
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, help_text="(optional)")
    fax = PhoneNumberField(blank=True, null=True, help_text="(optional)")
    cell = PhoneNumberField(blank=True, null=True, help_text="(optional)")
    telephone = PhoneNumberField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = USStateField(choices=STATE_CHOICES)
    postal_code = models.IntegerField(blank=True, null=True, help_text="(optional)")
    
    def __unicode__(self):
        return self.name