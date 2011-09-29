from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def phone_paren(value, delimiter):
    """
    Tries to format as a phone number in the format '(123) 456_7890' or '456_7890'
    where the '_' is the delimiter you pass.
    It puts parens around the area code.
    """
    extras = (' ', '.', ',', '-', '(', ')')
    newvalue = value
    
    for extra in extras:
        newvalue = newvalue.replace(extra, '')
    
    if len(newvalue) == 7:
        return newvalue[:3] + delimiter + newvalue[3:]
    elif len(newvalue) == 10:
        return "(%s) %s%s%s" % (newvalue[:3], newvalue[3:7], delimiter, newvalue[7:])
    else:
        print len(newvalue)
        return value

@register.filter
@stringfilter
def phone(value, delimiter):
    """
    Tries to format as a phone number in the format '123_456_7890' or '456_7890'
    where the '_' is the delimiter you pass.
    It does not put parens around the area code.
    """
    extras = (' ', '.', ',', '-', '(', ')')
    newvalue = value
    
    for extra in extras:
        newvalue = newvalue.replace(extra, '')
    
    if len(newvalue) == 7:
        return newvalue[:3] + delimiter + newvalue[3:]
    elif len(newvalue) == 10:
        return newvalue[:3] + delimiter + newvalue[3:7] +delimiter + newvalue[7:]
    else:
        return value

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False        
    
@register.filter
@stringfilter
def pretty_numbers(value, class_name="number", autoescape=None):
    """
    Spans any numbers it finds in the provided class_name, or defaults to "number".
    Does not currently support decimals.
    e.g. 123 Main becomes <span class='number'>123</span> Main 
    """
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    
    spanbegin = "<span class='%s'>" % class_name
    spanend = "</span>"
    spanning = False
    newvalue = ''
    
    for c in value:
        if is_number(c):
            if spanning:
                newvalue += esc(c)
            else:
                newvalue += spanbegin + esc(c)
                spanning = True 
        else:
            if spanning:
                newvalue += spanend + esc(c)
                spanning = False
            else:
                newvalue += esc(c)
    
    if spanning:
        newvalue += spanend
    
    return mark_safe(newvalue)
pretty_numbers.needs_autoescape = True