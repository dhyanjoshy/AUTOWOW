from django import forms
from .models import *
from store.models import Brand,Product,Category,Color,Varient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'username'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'input100', 'name': 'email', 'type': 'email'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'firstname'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'lastname'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input100', 'name': 'password1'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input100', 'name': 'password2'})

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class DealerForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user'].required = True
        self.fields['user'].widget.attrs['required'] = True
        self.fields['user'].widget.attrs['class'] = 'input100'
        self.fields['user'].widget.attrs['id'] = 'selectUser'
        self.fields['user'].widget.choices = self.fields['user'].choices
        self.fields['dealer'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'dealer'})
        self.fields['address_line1'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'address_line1'})
        self.fields['address_line2'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'address_line2'})
        self.fields['address_line3'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'address_line3'})
        self.fields['location'].widget = forms.URLInput(attrs={'class': 'input100', 'name': 'location'})
        self.fields['phone_number1'].widget = forms.NumberInput(attrs={'class': 'input100', 'name': 'phone_number1'})
        self.fields['phone_number2'].widget = forms.NumberInput(attrs={'class': 'input100', 'name': 'phone_number2'})

    class Meta:
        model = Dealer
        fields = ('user','dealer','address_line1','address_line2','address_line3','location','phone_number1','phone_number2')


class BrandForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].required = True
        self.fields['category'].widget.attrs['required'] = True
        self.fields['category'].widget.attrs['class'] = 'input100'
        self.fields['category'].widget.attrs['id'] = 'selectUser'
        self.fields['category'].widget.choices = self.fields['category'].choices
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'title'})
        self.fields['description'].widget = forms.Textarea(attrs={'class': 'input100', 'name': 'description'})
        self.fields['logo'].widget = forms.ClearableFileInput(attrs={'class': 'input100', 'name': 'address_line3'})

    class Meta:
        model = Brand
        fields = ('category', 'title', 'description', 'logo')

class ProductForm(forms.ModelForm):
    dealer = forms.ModelChoiceField(queryset=Dealer.objects.all())
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['dealer'].required = True
        self.fields['dealer'].widget.attrs['required'] = True
        self.fields['dealer'].widget.attrs['class'] = 'input100'
        self.fields['dealer'].widget.attrs['id'] = 'selectUser'
        self.fields['dealer'].widget.choices = self.fields['dealer'].choices
        
        self.fields['brand'].required = True
        self.fields['brand'].widget.attrs['required'] = True
        self.fields['brand'].widget.attrs['class'] = 'input100'
        self.fields['brand'].widget.choices = self.fields['brand'].choices

        self.fields['category'].required = True
        self.fields['category'].widget.attrs['required'] = True
        self.fields['category'].widget.attrs['class'] = 'input100'
        self.fields['category'].widget.choices = self.fields['category'].choices

        self.fields['title'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'title'})
        self.fields['description'].widget = forms.Textarea(attrs={'class': 'input100', 'name': 'description'})
        self.fields['image'].widget = forms.ClearableFileInput(attrs={'class': 'input100', 'name': 'image'})

    class Meta:
        model = Product
        fields = ('dealer','category','brand', 'title', 'description', 'image')

class ColorForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product'].required = True
        self.fields['product'].widget.attrs['required'] = True
        self.fields['product'].widget.attrs['class'] = 'input100'
        self.fields['product'].widget.attrs['id'] = 'selectUser'
        self.fields['product'].widget.choices = self.fields['product'].choices
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'title'})
        self.fields['image'].widget = forms.ClearableFileInput(attrs={'class': 'input100', 'name': 'address_line3'})

    class Meta:
        model = Color
        fields = ('product', 'title', 'image')

class VarientForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product'].required = True
        self.fields['product'].widget.attrs['required'] = True
        self.fields['product'].widget.attrs['class'] = 'input100'
        self.fields['product'].widget.attrs['id'] = 'selectUser'
        self.fields['product'].widget.choices = self.fields['product'].choices
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'title'})
        self.fields['price'].widget = forms.NumberInput(attrs={'class': 'input100', 'name': 'address_line3'})

    class Meta:
        model = Varient
        fields = ('product', 'title', 'price')


            
