from django import forms
from user.models import Customer,Dealer


class UserForm(forms.ModelForm):
    dealer = forms.ModelChoiceField(queryset=Dealer.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['dealer'].required = True
        self.fields['dealer'].widget.attrs['required'] = True
        self.fields['dealer'].widget.attrs['class'] = 'input100'
        self.fields['dealer'].widget.attrs['id'] = 'selectItem'
        self.fields['dealer'].widget.choices = self.fields['dealer'].choices
        self.fields['fname'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'address_line1','placeholder':'First Name'})
        self.fields['lname'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'address_line2','placeholder':'Last Name'})
        self.fields['phone_number'].widget = forms.NumberInput(attrs={'class': 'input100', 'name': 'phone_number1','placeholder':'Phone Number'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'input100', 'name': 'phone_number2','placeholder':'Email'})

    class Meta:
        model = Customer
        fields = ('dealer','fname','lname','phone_number','email')



            
