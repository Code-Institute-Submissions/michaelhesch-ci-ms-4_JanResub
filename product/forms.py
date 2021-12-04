from django import forms

from .models import Category, Product


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'category',
            'product_name',
            'description',
            'price',
            'image',
        ]

    image = forms.ImageField(label='Image', required=False)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
