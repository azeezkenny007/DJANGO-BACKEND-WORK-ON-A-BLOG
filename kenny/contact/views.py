from django.shortcuts import render,redirect
from .models import Contact
from .forms import Contactform


# Create your views here.
def myview5(request):
    form=Contactform()
    if request.method=='POST':
        # contact=Contact(email=request.POST.get('email'),name=request.POST.get('username'),
        #                 phonenumber=request.POST.get('phonenumber'),
        #                 message=request.POST.get('message'))
        form=Contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect()



    return render(request,'contact/contact.html',context={'form':form})
