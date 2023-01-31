from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions
from django.core.validators import RegexValidator

from studentapp.models import Student_Registration, Login_view, Mark, Admin1


class DateInput(forms.DateInput):
    input_type = 'date'

class Stud_form(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)
    class Meta:
        model = Student_Registration
        exclude = ("user","age",)

    def clean_picture(self):
        picture = self.cleaned_data.get("picture")
        if not picture:
            raise forms.ValidationError("No image!")
        else:
            w, h = get_image_dimensions(picture)
            if w != 100:
                raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 100px" % w)
            if h != 200:
                raise forms.ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)
        return picture


class admin_form(forms.ModelForm):

    class Meta:
        model = Admin1
        exclude = ("user",)


class user_reg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,validators=[
        RegexValidator(regex='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,}$',message='please enter valid number')])
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput,)
    class Meta:
        model = Login_view
        fields = ("username","password1","password2")


class mark_form(forms.ModelForm):
    class Meta:
        model = Mark
        fields = "__all__"