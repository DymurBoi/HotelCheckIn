from django import forms
from .models import Room, RoomCategory

class RoomForm(forms.ModelForm):
    room_category = forms.ModelChoiceField(
        queryset=RoomCategory.objects.all(),
        empty_label="Select Room Category",
        label="Room Category",
    )

    class Meta:
        model = Room
        fields = ['room_id', 'room_category','is_available']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ['category_id', 'room_photo', 'room_desc', 'room_price']
        labels = {
            'category_id': 'Category',
            'room_photo': 'Room Photo',
            'room_desc': 'Room Description',
            'room_price': 'Room Price',
           
        }
        widgets = {
            'room_desc': forms.Textarea(attrs={'rows': 3}),
            'room_price': forms.NumberInput(attrs={'step': '0.01'}),
        }
