from django.core.mail import send_mail
from django.contrib.auth import get_user_model


User = get_user_model()

def set_activaion_code(user):
    code = user.create_activation_code()
    if User.objects.filter(activation_code=code).exists():
        user.set_activation_code
    else:
        user.activation_code = code
        user.save()


def send_activation_email(email, activation_code):
    activation_url = f'http://localhost:8000/api/v1/activate/{activation_code}/'
    message = f'''thank for your signing up
                follow this link {activation_url}'''

    send_mail(
        'Hey booy',
        message,
        'test@mail.ru',
        [email, ],
        fail_silently=False
    )