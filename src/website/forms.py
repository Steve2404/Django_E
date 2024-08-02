from django import forms

JOBS = (
    ("Python", "Developpeur Python"),
    ("JavaScript", "Developpeur JavaScript"),
    ("PHP", "Developpeur PHP"),
    ("Java", "Developpeur Java")
)


class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)
