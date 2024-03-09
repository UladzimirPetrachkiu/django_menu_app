from typing import Any

from django import template
from django.utils.safestring import mark_safe

from django_menu_app.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context: Any, menu_name: str) -> str:
    """
    Render the menu based on the menu_name provided.

    Args:
    - context: Any
    - menu_name: str

    Returns:
    - str
    """

    # Get the request object from the context
    request = context.get('request')
    if not request:
        return ''

    # Retrieve the menu item based on the menu_name
    menu = MenuItem.objects.filter(name=menu_name).first()
    if not menu:
        return ''

    def is_active(menu_item: MenuItem) -> bool:
        """
        Check if the given menu item is active by comparing its URL with the current request path.

        Args:
            menu_item (MenuItem): The menu item to check.
        Returns:
            bool: True if the menu item is active, False otherwise.
        """
        return menu_item.url == request.path

    def is_expanded(menu_item: MenuItem) -> bool:
        """
        Check if the menu item is expanded by checking if it is active or if any of its children are active or expanded.

        Args:
            menu_item: The MenuItem object to check

        Returns:
            True if the menu item is expanded, False otherwise
        """
        if is_active(menu_item):
            return True
        for child in menu_item.children.all():
            if is_active(child) or is_expanded(child):
                return True
        return False

    def render_menu(menu_item: MenuItem) -> str:
        """
        Renders a menu item and its children as HTML list items, with active and expanded classes as needed.

        Args:
            menu_item (MenuItem): The menu item to be rendered.

        Returns:
            str: The HTML representation of the menu item and its children.
        """
        active_class = 'active' if is_active(menu_item) else ''
        expanded_class = 'expanded' if is_expanded(menu_item) else ''
        children = menu_item.children.all()
        if children:
            submenu = ''.join(render_menu(child) for child in children)
            return f'<li class="{active_class} {expanded_class}"><a href="{menu_item.url}">{menu_item.name}</a><ul>{submenu}</ul></li>'
        else:
            return f'<li class="{active_class}"><a href="{menu_item.url}">{menu_item.name}</a></li>'

    # Render the menu as HTML
    menu_html = ''.join(render_menu(menu))
    return mark_safe(f'<ul>{menu_html}</ul>')
