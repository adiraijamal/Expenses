from django import template


register = template.Library()


@register.filter(name='cf')
def cf(amount):
    # Return an empty string if amount is None, an empty string, or zero
    if amount in (None, '', 0):
        return ''

    # Format the amount as an integer with commas
    formatted_amount = f"{int(amount):,}"

    # Determine the CSS class based on the sign of the amount
    if amount < 0:
        css_class = "red-text"
    else:
        css_class = "green-text"

    # Generate the HTML markup with the CSS class and formatted amount
    return f'<span class="{css_class}">{formatted_amount}</span>'


@register.filter(name='dictkey')
def dictkey(key, the_dict):
    """
    A filter that returns True if the given key is in the dictionary.
    """
    if isinstance(the_dict, dict):
        return 'True' if key in the_dict else ''
    else:
        return ''


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
