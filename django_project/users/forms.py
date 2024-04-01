from allauth.account.forms import SignupForm
from django import forms
from .models import TestUser


class CustomSignupForm(SignupForm):
	# name = forms.CharField(required=True)
	avatar = forms.CharField(max_length=200, required=False)
	gender = forms.CharField(max_length=10, required=False)
	birthday = forms.DateTimeField(required=False)
	phone = forms.CharField(max_length=256, required=False)
	website = forms.CharField(max_length=100, required=False)
	biography = forms.CharField(widget=forms.Textarea, required=False)
	zipcode = forms.CharField(max_length=10, required=False)
	country = forms.CharField(max_length=50, required=False)
	state = forms.CharField(max_length=100, required=False)
	city = forms.CharField(max_length=120, required=False)
	address = forms.CharField(max_length=512, required=False)
	# longitude = forms.DecimalField(max_digits=11, decimal_places=8, required=False)
	# latitude = forms.DecimalField(max_digits=10, decimal_places=8, required=False)
	# following_count = forms.IntegerField(required=False)
	# follower_count = forms.IntegerField(required=False)
	block = forms.JSONField(required=False)
	article = forms.JSONField(required=False)
	first_name = forms.CharField(max_length=60, label="First name",
								 widget=forms.TextInput(attrs={'placeholder': 'First name'}))
	last_name = forms.CharField(max_length=60, label="Last name",
								widget=forms.TextInput(attrs={'placeholder': 'Last name'}))

	# name = forms.CharField(max_length=60, required=True)

	class Meta:
		model = TestUser
		# fields that does not exist in SignupForm
		fields = ("email", "name",
				  "avatar", 'gender', 'birthday', 'phone', 'website',
				  'biography', 'zipcode', 'country', 'state', 'city', 'address',
				  'block', 'article',"first_name", "last_name")




class CustomUserUpdateForm(forms.ModelForm):


	class Meta:
		model = TestUser
		fields = ("username",
				  "avatar", 'gender', 'birthday', 'phone', 'website',
				  'biography', 'zipcode', 'country', 'state', 'city', 'address',
				  'block', 'article')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


	def save(self, commit=True):
		user = super().save(commit=False)

		user.avatar = self.cleaned_data['avatar']
		user.gender = self.cleaned_data['gender']
		user.birthday = self.cleaned_data['birthday']
		user.phone = self.cleaned_data['phone']
		user.website = self.cleaned_data['website']
		user.biography = self.cleaned_data['biography']
		user.zipcode = self.cleaned_data['zipcode']
		user.country = self.cleaned_data['country']
		user.state = self.cleaned_data['state']
		user.city = self.cleaned_data['city']
		user.address = self.cleaned_data['address']
		user.is_active = True
		if commit:
			user.save()

		return user


