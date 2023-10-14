import requests
from django.core.cache import cache
from .models import Integrations

def get_data_from_api(api_url, headers):
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('rows', [])
    except requests.exceptions.RequestException as e:
        return []

def update_api_data():
    integration = Integrations.objects.get()
    server_address = integration.server_address
    npsn = integration.npsn
    api_token = integration.token

    base_url = f'http://{server_address}:1162/WebService/'

    headers = {
        'Authorization': f'Bearer {api_token}',
        'Cache-Control': 'no-cache',
    }

    # Data School
    dapodik_school_api = get_data_from_api(f'{base_url}getSekolah?npsn={npsn}', headers)
    if dapodik_school_api:
        print('Dapodik School API Connection [OK].')

    # Data Employees
    dapodik_employees_api = get_data_from_api(f'{base_url}getGtk?npsn={npsn}', headers)
    if dapodik_employees_api:
        print('Dapodik Employees API Connection [OK].')

    # Data Students
    dapodik_students_api = get_data_from_api(f'{base_url}getPesertaDidik?npsn={npsn}', headers)
    if dapodik_students_api:
        print('Dapodik Students API Connection [OK].\n')

    return dapodik_school_api, dapodik_employees_api, dapodik_students_api