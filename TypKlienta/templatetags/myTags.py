from django import template

register = template.Library()


@register.filter
def NoweZuzycie(zuzycie,mnoznik):
 return zuzycie * mnoznik