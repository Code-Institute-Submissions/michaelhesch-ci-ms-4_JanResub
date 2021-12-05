from django.conf import settings

from liffey.settings import FREE_DELIVERY_THRESHOLD


def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = 10
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
