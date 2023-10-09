import requests
from .headers import headers
from .api_endpoint import getSekolah, getPengguna, getGtk, getRombonganBelajar, getPesertaDidik

def get_data_from_api(api_url, headers):
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('rows', [])
    except requests.exceptions.RequestException as e:
        return []
    
# Data School
dapodik_school = get_data_from_api(getSekolah, headers)
if dapodik_school:
    # print(dapodik_school)
    print('Dapodik School API Connection [OK].')

# Data Users
dapodik_users = get_data_from_api(getPengguna, headers)
if dapodik_users:
    print('Dapodik Users API Connection [OK].')

# Data Employees
dapodik_employees = get_data_from_api(getGtk, headers)
dapodik_employees_name = [(item['nama'], item['nama']) for item in dapodik_employees]
if dapodik_employees:
    print('Dapodik Employees API Connection [OK].')

# Data Learning Group
dapodik_learning_group_raw = get_data_from_api(getRombonganBelajar, headers)
dapodik_learning_group = [(item['nama'], item['nama']) for item in dapodik_learning_group_raw]
if dapodik_learning_group_raw:
    print('Dapodik Learning Group API Connection [OK].')

# Data Students
dapodik_students = get_data_from_api(getPesertaDidik, headers)
dapodik_students_name = [(item['nama'], item['nama']) for item in dapodik_students]
if dapodik_students:
    print('Dapodik Students API Connection [OK].\n')
