from django import template


register = template.Library()


@register.filter(name='child_protect')
def child_protect(value):
    if value.age and value.age > 13:
        return "allowed"
    else:
        return "blocked"


@register.filter(name='bizz_fuzz')
def bizz_fuzz(value):
    bizz = value.random_int % 3 == 0
    fuzz = value.random_int % 5 == 0
    if bizz and fuzz:
        return 'bizzfuzz'
    elif bizz:
        return 'bizz'
    elif fuzz:
        return 'fuzz'
    else:
        return value.random_int