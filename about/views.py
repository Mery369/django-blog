from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About
from .forms import CollaborateForm
from django.contrib import messages

# Create your views here.
def about_me(request):
    """
    Renders the About page
    """
    if request.method == "POST":
             
             collab_form = CollaborateForm(data=request.POST)
             if collab_form.is_valid():
                collab_form.save()
                messages.add_message(request, messages.SUCCESS,'Collaboration request received! I endeavour to respond within 2 working days.'
                 )
    about = About.objects.all().order_by('-updated_on').first()
      
    collab_form = CollaborateForm()
    
    return render(
        request,
        "about/about.html",
        {"about": about,
        "collab_form": collab_form,},
            )