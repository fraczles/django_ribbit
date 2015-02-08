from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from ribbit_app.forms import AuthenticateForm, UserCreateForm, RibbitForm
from ribbit_app.models import Ribbit

def index(request, auth_form=None, user_form=None):
	#User is logged in:
	if request.user.is_authenticated():
		ribbit_form = RibbitForm()
		user = request.user
		ribbits_self = Ribbit.objects.filter(user=user.id) #Retrieve Ribbits associated with my user ID
		ribbit_buddies = Ribbit.objects.filter(user__userprofile__in=user.profile.follows.all)
		ribbits = ribbits_self | ribbits_buddies
		
		return render(request,
					'buddies.html',
					{'ribbit_form': ribbit_form ,'user': user ,'ribbits': ribbits ,'next_url':'/' }
