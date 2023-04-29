from django import forms
g=[('Male','male'),('Female','female')]
h=[['Pyt','Java'],['Mern',"sql"]]
class StudentForm(forms.Form):
    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Url=forms.URLField()
    # # Img=forms.ImageField()
    # Email=forms.EmailField()
    # Gender=forms.ChoiceField(choices=g)#drop downlist
    # Gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    # Password=forms.CharField(widget=forms.PasswordInput)
    # Address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    # address=forms.CharField(max_length=300,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    # Course=forms.MultipleChoiceField(choices=h)
    # Radio=forms.ChoiceField(widget=forms.RadioSelect)
    # Course=forms.MultipleChoiceField(choices=h,widget=forms.CheckboxSelectMultiple)