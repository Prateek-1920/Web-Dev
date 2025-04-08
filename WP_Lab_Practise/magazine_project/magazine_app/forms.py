from django import forms

class MagazineForm(forms.Form):
    title = forms.CharField(label="Cover Title",max_length=100)
    subtitle = forms.CharField(label="Subtitle",max_length=200,required=False)
    textcolor = forms.CharField(label="Text Color",max_length=20,initial="#000000")
    fontsize = forms.IntegerField(label="Font Size",min_value=10,max_value=30)
    background = forms.CharField(label="BackGround Color",max_length=20,initial="#ffffff")
    image = forms.ImageField(label="Upload Cover Image",required=False)