from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, BillingAddress, Category, Slide, ProductInformation, Subcategory


# Register your models here.


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ref_code',
                    'ordered_date',
                    'shipping_address',
                    'billing_address',
                    'payment_method',
                    'coupon',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'is_pickup',
                    'order_completed'
                    ]
    # list_display_links = [
    #                'ordered',
    #                'being_delivered',
    #                'received',
    #                'refund_requested',
    #                'refund_granted',
    #                'is_pickup',
    #                'order_completed'
    # ]
    list_display_links = ['user', 'ref_code']  # Choose fields from list_display to be clickable links

    list_filter = ['user',
                   'ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted',
                   'is_pickup',
                   'order_completed']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    def shipping_address_display(self, obj):
        return f"{obj.shipping_address.street_address}, {obj.shipping_address.apartment_address}, {obj.shipping_address.zip}, {obj.shipping_address.country}"
    shipping_address_display.short_description = 'Shipping Address'

    def billing_address_display(self, obj):
        return f"{obj.billing_address.street_address}, {obj.billing_address.apartment_address}, {obj.billing_address.zip}, {obj.billing_address.country}"
    billing_address_display.short_description = 'Billing Address'

    def payment_method_display(self, obj):
        return obj.payment_method
    payment_method_display.short_description = 'Payment Method'
    
    actions = [make_refund_accepted, 'mark_order_completed']  # Add the new action here

    def mark_order_completed(self, request, queryset):
        queryset.update(order_completed=True)

    mark_order_completed.short_description = 'Mark selected orders as completed'

class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'apartment_address', 'country', 'zip', 'city', 'whatsapp_number', 'design_upload', 'address_type', 'default']
    
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


def copy_items(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


copy_items.short_description = 'Copy Items'


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'item_quantity', 'price']  # Add 'price' to list_display if needed
    fields = ['title', 'item_image1', 'item_image2', 'item_image3', 'item_details', 'item_quantity', 'price','discount_price', 'specification_image', 'category', 'subcategory', 'slug']
    list_filter = ['title', 'item_quantity']
    search_fields = ['title', 'item_quantity', 'price']  # Add 'price' to search_fields if needed
    actions = [copy_items]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active'
    ]
    list_filter = ['title', 'is_active']
    search_fields = ['title', 'is_active']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slide)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(BillingAddress, AddressAdmin)
admin.site.register(ProductInformation)
admin.site.register(Subcategory)