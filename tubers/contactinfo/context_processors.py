from django.contrib.auth.models import User
from .models import Contactinfo, Socallinks

def project_context(request):

	context = {
        'me': Contactinfo.objects.all(),
        'you': Socallinks.objects.all(),
	}

	return context