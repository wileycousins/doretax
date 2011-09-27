from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField, USPostalCodeField
from django.contrib.localflavor.us.us_states import STATE_CHOICES

class Association(models.Model):
    """
    A civic or professional association.
     e.g. Chamber of Commerce, National Society of Pencil Sharpeners, etc. 
    """
    ASSOCIATION_TYPES = (
                         (0, 'Civic and Community'),
                         (1, 'Professional'), 
                         )
    name = models.CharField(max_length=100, unique=True)
    type = models.SmallIntegerField("Community or professional?", choices=ASSOCIATION_TYPES)
    link = models.URLField("Association link", null=True, blank=True, help_text="(optional)")
    
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
    
class Link(models.Model):
    """
    A client or community link with a name and optional description.
    e.g. Where's my refund?, Movies made locally, etc.
    """
    LINK_TYPES = (
                  (0, 'Client'),
                  (1, 'Community'), 
                  )
    name = models.CharField(max_length=100, unique=True)
    link = models.URLField()
    kind = models.SmallIntegerField(choices=LINK_TYPES)
    description = models.TextField(blank=True, null=True, help_text="(optional)")
    
    def __unicode__(self):
        return "%s, %s" % (self.name, self.link)
    
    class Meta:
        ordering = ['kind', 'name']

class USMailingAddress(models.Model):
    """
    A basic US mailing address.
    """
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True, help_text="(optional)")
    city = models.CharField(max_length=100)
    state = USStateField(choices=STATE_CHOICES)
    postal_code = models.SmallIntegerField()
    
    def __unicode__(self):
        return self.address1
    
    class Meta:
        ordering = ['city', 'state']
        verbose_name = "US Mailing Address"
        verbose_name_plural = "US Mailing Addresses"
        
class ContactInfo(models.Model):
    """
    Some basic contact info. Everything is optional.
    """
    email = models.EmailField(blank=True, null=True, help_text="(optional)")
    telephone = PhoneNumberField(blank=True, null=True, help_text="(optional)")
    fax = PhoneNumberField(blank=True, null=True, help_text="(optional)")
    cell = PhoneNumberField(blank=True, null=True, help_text="(optional)")
    address = models.ForeignKey(USMailingAddress, blank=True, null=True, help_text="(optional)")
    
    def __unicode__(self):
        return self.email
    
    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"
    