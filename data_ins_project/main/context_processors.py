from .models import MenuItem, FooterItem


def menu(request):
    return {
        "menu_items": MenuItem.objects.filter(parent_id=None),
    }
    
    
def footer(request):
    return {
        "footer_items": FooterItem.objects.all(),
    }