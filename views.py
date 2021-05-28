from django.http import HttpResponse 
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


from .forms import QuoteForm
from .forms import ContactForm



def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home.html", {})

def contact_view(request):
    if request.method == 'GET':
       form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 
                	email, ['cassandratalbot@yahoo.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def about_view(request, *args, **kwargs):
	my_context = {
		"title": "The work I do",
		"this is true": True, 
		"my_number": 123,
		"my_list": [900, 4567, 1342, "Abc"],
		"my_html": "<h1>hello world</h1>"
	}
	return render(request, "about.html", my_context)

def projects_view(request, *args, **kwargs):
	return render(request, "projects.html", {})

def directory_view(request, *args, **kwargs):
	return render(request, "directory.html", {})

def prices_view(request, *args, **kwargs):
	return render(request, "prices.html", {})

def quoteView(request):
    if request.method == 'GET':
        form = QuoteForm()
    else:
        form = QuoteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            number = form.cleaned_data['number']
            about = form.cleaned_data['about']
            try:
                send_mail(name, email, about, ['cassandratalbot@yahoo.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "quote/quote.html", {'form': form})
 

def successView(request):
    return render(request, "success.html", {})

def updates_View(request, *args, **kwargs):
	return render(request, "updates.html", {})

def reasons_View(request, *args, **kwargs):
	return render(request, "reasons.html", {})
