from django import forms


class stud_form(forms.Form):
    Name = forms.CharField(max_length=20)
    Stud_Id = forms.IntegerField()
    Email = forms.EmailField(max_length=20)
    Password = forms.CharField(max_length=20, widget = forms.PasswordInput)
    Date = forms.DateField(widget=forms.DateInput)
    choices = [('1','Male'),('2','Female')]
    Gender_choice = forms.ChoiceField(choices=choices)
    Gender_Radio = forms.ChoiceField(choices=choices, widget = forms.RadioSelect)
    I_Agree = forms.CharField(widget = forms.CheckboxInput)
    Description = forms.CharField(widget = forms.Textarea)
    Url = forms.URLField(widget=forms.URLInput)
    Label_Sufix = forms.CharField(label_suffix =' :==>')
    Initial = forms.CharField(initial='Mr/Ms. ')

