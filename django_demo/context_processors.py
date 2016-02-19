import md5

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site


def extra_context(request):
    context = {
        'current_site': get_current_site(request),
        'login_form': AuthenticationForm(),
    }
    try:
        user_email = request.user.email
    except AttributeError:
        return context
    url_base = 'https://secure.gravatar.com/avatar/'
    email_hash = md5.new()
    email_hash.update(user_email.strip().lower())
    gravatar_url = url_base + email_hash.hexdigest() + '?d=mm'
    context['user_gravatar'] = gravatar_url
    return context
