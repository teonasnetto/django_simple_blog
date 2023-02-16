from django import template

register = template.Library()

@register.filter(is_safe=True, name='add_classes')
def add_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })