from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
    ('PU', 'Pickup')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St',
        'class': 'form-control'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or suite',
        'class': 'form-control'
    }))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'City',
        'class': 'form-control'
    }))
    whatsapp_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'WhatsApp Number',
        'class': 'form-control'
    }))
    design_upload = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'form-control-file'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adjust required fields based on conditions (e.g., pickup option)
        if 'payment_option' in self.data and self.data['payment_option'] == 'PU':  # 'PU' is Pickup option
            self.fields['street_address'].required = False
            self.fields['apartment_address'].required = False
            self.fields['country'].required = False
            self.fields['zip'].required = False
            self.fields['city'].required = False
        else:
            self.fields['street_address'].required = True
            self.fields['apartment_address'].required = True
            self.fields['country'].required = True
            self.fields['zip'].required = True
            self.fields['city'].required = True


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()
