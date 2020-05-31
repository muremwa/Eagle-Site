from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .settings import SECRET_EAGLE_NAME


def eagle_profile(request):
    if request.method == "GET":
        return {'eagle': get_object_or_404(User, username=SECRET_EAGLE_NAME).eagleprofile}
