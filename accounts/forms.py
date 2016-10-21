from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        """
        user_qs = User.objects.filter(username=username)
        if user_qs.count() == 1:
            user = user_qs.first()
        """
        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                print("korisnik ne postoji")
                raise forms.ValidationError("Korisnik ne postoji.")

            if not user.check_password(password):
                print("lozinka")
                raise forms.ValidationError("Pogresna lozinka.")

            if not user.is_active:
                print("neaktivan")
                raise forms.ValidationError("Neaktivan korisnik.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean(self, *args, **kwargs):
        username_qs = User.objects.filter(username=self.cleaned_data.get('username'))
        if username_qs.exists():
            raise forms.ValidationError("Korisnicko ime vec postoji.")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
