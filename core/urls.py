from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from .views import (
    ItemDetailView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    ShopView,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    CategoryView,
    SubcategoryView,
    privacypolicy,
    termsandconditions,
    PickupView,
    order_success,
    contact,
    about
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-success/', order_success, name='order-success'),
    path('pickup/', PickupView.as_view(), name='pickup'),  # Add this line
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('subcategory/<slug>/', SubcategoryView.as_view(), name='subcategory'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path("privacypolicy/", privacypolicy, name="privacy-policy"),
    path("termsandconditions/", termsandconditions, name="terms-and-conditions"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)