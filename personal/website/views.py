from django.shortcuts import render
from .models import projects
# Create your views here.
from django.core.mail import send_mail
def home(request):
    if request.POST:
        msg = True
        all_prjects = projects.objects.all()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        message = '{} {}'.format(email,message)
        send_mail(name, message, email, ['elsayed.amr50@gmail.com'])
        print(name)
    else:
        msg = False
        all_prjects = projects.objects.all()
    context = {'project':all_prjects,'msg':msg}
    return render(request,'index.html',context)

def project(request,id):
    project = projects.objects.get(id=id)
    context = {
        'project':project
    }
    return render(request,'single.html',context)