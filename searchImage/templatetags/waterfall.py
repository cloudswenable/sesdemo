from django import template


register = template.Library()

@register.filter(name="detail1")
def detail1(value, arg):
    allcount, remainder = arg.split(",")
    allcount = int(allcount)
    remainder = int(remainder)
    if value%allcount == remainder:
        return True
    return False