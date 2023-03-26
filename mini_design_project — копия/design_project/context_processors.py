
from design_project.forms import Contact


def form_contact(request):
    form = Contact()
    return {'form_contact': form}

