import md5

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site


def build_gravatar_url(email, default='?d=mm'):
    url_base = 'https://secure.gravatar.com/avatar/'
    email_hash = md5.new()
    email_hash.update(email.strip().lower())
    return url_base + email_hash.hexdigest() + default


def extra_context(request):
    context = {
        'current_site': get_current_site(request),
        'login_form': AuthenticationForm(),
    }
    try:
        gravatar_url = request.session['gravatar_url']
    except KeyError:
        try:
            gravatar_url = build_gravatar_url(request.user.email)
            request.session['gravatar_url'] = gravatar_url
        except AttributeError:
            return context
    context['user_gravatar'] = gravatar_url
    return context
