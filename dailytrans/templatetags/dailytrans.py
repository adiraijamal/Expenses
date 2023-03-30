from django import template


register = template.Library()

@register.filter
def render_table(table):
    return table.as_html()
