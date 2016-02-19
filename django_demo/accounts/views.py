from django.conf import settings
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.debug import sensitive_post_parameters
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


class LoginView(generic.FormView):
    success_url = settings.LOGIN_REDIRECT_URL
    form_class = AuthenticationForm
    redirect_field_name = auth.REDIRECT_FIELD_NAME
    template_name = 'accounts/login.html'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        redirect_to = self.request.REQUEST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(generic.RedirectView):
    permanent = False
    pattern_name = 'main:landing'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class ProfileView(generic.TemplateView):
    pass
