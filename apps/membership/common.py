from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _

ROLES = (
    (1, _("User")),
    (2, _("Editor")),
    (3, _("Super Admin")),
)


def send_auth_email(request, user_email):
    user_model = get_user_model()
    user = user_model.objects.get(email=user_email)
    current_site = get_current_site(request)
    domain = (current_site.domain,)
    uid = (urlsafe_base64_encode(force_bytes(user.pk)),)
    token = default_token_generator.make_token(user)
    mail_subject = _("Activate your blog account.")
    protocol = "http"
    url = f"{protocol}://{domain[0]}/api/v1/membership/activate/{uid[0]}/{token}"
    message = f'<p><a href="{url}">{url}</a></p>'
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.send()
