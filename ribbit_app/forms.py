from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from ribbit_app.models import Ribbit

class UserCreateForm(UserCreationForm):
	email = forms.EmailForm(requried=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Email'}))
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'First Name'}))
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name'}))
	username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder':'Username'}))
	password1 = forms.Charfield(widgets.PasswordInput(attrs={'placeholder':'Password'}))
	password2 = forms.Charfield(widgets.PasswordInput(attrs={'placeholder':'Password Confirmation'}))

	def is_valid(self):
		form = super(UserCreateForm,self).is_valid()
		for f, error in self.errors.iteritems():
			if f != '__all_':
				self.fields[f].widget.attrs.update({'class':'error', 'value': strip_tags(error)})
		return form
	
	class Meta:
		fields = ['email', 'username', 'first_name','last_name','email','password1', 'password2' ]
		model = User