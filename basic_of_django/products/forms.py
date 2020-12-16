from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter your title'}))
    description = forms.CharField(required=False, 
                                    widget=forms.Textarea(
                                        attrs={'placeholder':'this is the description',
                                        }
                                    )
                                )
    price = forms.DecimalField(initial=199)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'feature'
        ] 
    
    # def clean_title(self,*args,**kwargs):                                #  We can set  Validation 
    #     title = self.cleaned_data.get('title')
    #     if 'CFE' in title:   # CFE should contain in the data or it will raise notice
    #         return title
    #     else:
    #         raise forms.ValidationError('This is not a valid title')

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = [
#             'title',
#             'description',
#             'price',
#             'summary',
#             'feature'
#         ] 

class RowProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter your title'}))
    description = forms.CharField(required=False, 
                                    widget=forms.Textarea(
                                        attrs={'placeholder':'this is the description',
                                        }
                                    )
                                )
    price = forms.DecimalField(initial=199)
