from django.shortcuts import render

# Create your views here.
def landing_page(request):

	# add template name + extension (.html). It is not an URL!
	# always return the request object as a first argument in render().
	return render(request, 'landing_page.html')  