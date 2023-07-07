from django.contrib.auth.models import User
from .models import Integrations

def get_user_server_address(user):
    try:
        my_model = Integrations.objects.get(user=user)
        field_value = my_model.server_address
    except Integrations.DoesNotExist:
        field_value = 'dapodik.smpn290jakarta.sch.id'

    return field_value

def get_user_npsn(user):
    try:
        my_model = Integrations.objects.get(user=user)
        field_value = my_model.npsn
    except Integrations.DoesNotExist:
        field_value = '69980874'

    return field_value

def get_user_token(user):
    try:
        my_model = Integrations.objects.get(user=user)
        field_value = my_model.token
    except Integrations.DoesNotExist:
        field_value = 'Wmr36w90UBMiout'

    return field_value