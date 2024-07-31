from social_core.exceptions import AuthException
from users.models import CustomUser
from django.shortcuts import redirect
from django.urls import reverse


def social_user(backend, uid, user=None, *args, **kwargs):
    provider = backend.name
    response = kwargs.get('response', {})
    email = response.get('email')
    print(f"Provider: {provider}")
    print(f"Response data: {response}")
    print(f"Email from response: {email}")

    if not email:
        raise AuthException(backend, 'No email address found in response.')

    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        user = None

    if not user:
        kwargs['strategy'].session_set('social_auth_data', response)
        return redirect(reverse('register'))

    return {'user': user}
