from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm, Contact, EditAccountForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html', {})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("core:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	else:
		form = NewUserForm()
	return render (request=request, template_name="core/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("core:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	else:
		form = AuthenticationForm()
	return render(request=request, template_name="core/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("core:home")

@login_required
def dashboard(request):
	return render(request, 'core/dashboard.html', {})

@login_required
def edit_user(request):
    template_name = 'core/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit_passwd(request):
	template_name = 'core/edit_passwd.html'
	context = {}
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			context['success'] = True
	else:
		form = PasswordChangeForm(user=request.user)
	context['form'] = form
	return render(request, template_name, context)

@login_required
def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.send_mail()
            form = Contact()
    else:
        form = Contact()
    return render(request, 'core/contact.html', {'contact_form': form})

def error_404_view(request, exception):

    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html', status=404)