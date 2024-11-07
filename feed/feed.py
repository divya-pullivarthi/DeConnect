from django import forms

# Post Form
class PostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Post Title',
            'class': 'form-control'
        }),
        label='',
    )
   
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your post here...',
            'class': 'form-control',
            'rows': 4
        }),
        label='',
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        }),
        label='Upload Image (optional)',
    )
