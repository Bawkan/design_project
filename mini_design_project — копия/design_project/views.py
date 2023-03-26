from django.views.generic import DetailView
from design_project.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from design_project.forms import Contact
from django.contrib import messages
from django.http import HttpResponseRedirect

def design(request):
    obj = Work.objects.all()
    references = References.objects.all()
    return render(request, 'web/index.html', {'obj': obj,
                                              'references': references})


class ProjectDetail(DetailView):
    model = Work
    template_name = 'web/projects.html'


def shop(request):
    references = References.objects.all()
    return render(request, 'web/shop.html', {'references': references})


def send_to_mail(request):

    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            from_email = form.cleaned_data['mail']
            message = form.cleaned_data['text'] + ' ' + str(phone)
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
                messages.success(request, 'письмо успешно отправлено')
            except BadHeaderError:
                return HttpResponse('ошибка в писме')
            return redirect('design_project:design')
    else:
        form = Contact()
    return HttpResponseRedirect(request.META['HTTP_REFERER'], {'form', form})
