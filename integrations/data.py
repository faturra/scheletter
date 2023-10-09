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
else:
    pass

# Data Users
dapodik_users = get_data_from_api(getPengguna, headers)
if dapodik_users:
    print('Dapodik Users API Connection [OK].')
else:
    pass

# Data Employees
dapodik_employees = get_data_from_api(getGtk, headers)
dapodik_employees_name = [(item['nama'], item['nama']) for item in dapodik_employees]
if dapodik_employees:
    print('Dapodik Employees API Connection [OK].')
else:  
    pass

# Data Learning Group
dapodik_learning_group_raw = get_data_from_api(getRombonganBelajar, headers)
dapodik_learning_group = [(item['nama'], item['nama']) for item in dapodik_learning_group_raw]
if dapodik_learning_group_raw:
    print('Dapodik Learning Group API Connection [OK].')
else:
    pass

# Data Students
dapodik_students = get_data_from_api(getPesertaDidik, headers)
dapodik_students_name = [(item['nama'], item['nama']) for item in dapodik_students]
if dapodik_students:
    print('Dapodik Students API Connection [OK].\n')
else:   
    pass

####################
# import requests
# from .models import Integrations
# import json

# integration = Integrations.objects.get()
# server_address = integration.server_address
# npsn = integration.npsn
# api_token = integration.token

# base_url = f'http://{server_address}:1162/WebService/'

# headers = {
#    'Authorization': f'Bearer {api_token}',
#    'Cache-Control': 'no-cache',
# }

# # Variabel-variabel untuk menyimpan data
# dapodik_students = []
# dapodik_employees = []
# dapodik_school = []
# dapodik_users = []
# dapodik_learning_group = []

# def stream_data_from_api(api_url, headers):
#    try:
#        response = requests.get(api_url, headers=headers, stream=True)
#        response.raise_for_status()
#        for chunk in response.iter_content(chunk_size=1024):
#            if chunk:
#                # Proses data streaming disini
#                data = json.loads(chunk.decode('utf-8'))
#                print(data)
#                # Lakukan sesuatu dengan data
#                # Misalnya, tambahkan data ke variabel yang sesuai
#                rows = data.get('rows', [])
#                if api_url.endswith('getPesertaDidik'):
#                    dapodik_students.extend(rows)
#                elif api_url.endswith('getGtk'):
#                    dapodik_employees.extend(rows)
#                elif api_url.endswith('getSekolah'):
#                    dapodik_school.extend(rows)
#                elif api_url.endswith('getPengguna'):
#                    dapodik_users.extend(rows)
#                elif api_url.endswith('getRombonganBelajar'):
#                    dapodik_learning_group.extend(rows)
#                # Tambahkan kondisi dan variabel lain sesuai kebutuhan
#    except requests.exceptions.RequestException as e:
#        return []

# # Data School
# stream_data_from_api(f'{base_url}getSekolah?npsn={npsn}', headers)
# # Data Users
# stream_data_from_api(f'{base_url}getPengguna?npsn={npsn}', headers)
# # Data Employees
# stream_data_from_api(f'{base_url}getGtk?npsn={npsn}', headers)
# # Data Learning Group
# stream_data_from_api(f'{base_url}getRombonganBelajar?npsn={npsn}', headers)
# # Data Students
# stream_data_from_api(f'{base_url}getPesertaDidik?npsn={npsn}', headers)

# # Variabel-variabel berisi data sekarang akan berisi data dari respons API yang diterima melalui streaming
# import requests
# from .models import Integrations
# import json

# integration = Integrations.objects.get()
# server_address = integration.server_address
# npsn = integration.npsn
# api_token = integration.token

# base_url = f'http://{server_address}:1162/WebService/'

# headers = {
#    'Authorization': f'Bearer {api_token}',
#    'Cache-Control': 'no-cache',
# }

# # Variabel-variabel untuk menyimpan data
# dapodik_students = []
# dapodik_employees = []
# dapodik_school = []
# dapodik_users = []
# dapodik_learning_group = []

# def stream_data_from_api(api_url, headers, target_variable):
#    try:
#        response = requests.get(api_url, headers=headers, stream=True)
#        response.raise_for_status()
       
#        # Mengurai data JSON dari respons
#        data = json.loads(response.text)
       
#        # Lakukan sesuatu dengan data
#        # Misalnya, tambahkan data ke variabel yang sesuai
#        rows = data.get('rows', [])
#        target_variable.extend(rows)
#    except requests.exceptions.RequestException as e:
#        return []

# # Data School
# stream_data_from_api(f'{base_url}getSekolah?npsn={npsn}', headers, dapodik_school)
# # Data Users
# stream_data_from_api(f'{base_url}getPengguna?npsn={npsn}', headers, dapodik_users)
# # Data Employees
# stream_data_from_api(f'{base_url}getGtk?npsn={npsn}', headers, dapodik_employees)
# # Data Learning Group
# stream_data_from_api(f'{base_url}getRombonganBelajar?npsn={npsn}', headers, dapodik_learning_group)
# # Data Students
# stream_data_from_api(f'{base_url}getPesertaDidik?npsn={npsn}', headers, dapodik_students)

# # Setiap variabel berisi data dari masing-masing endpoint API
# dapodik_school = dapodik_school
# dapodik_users = dapodik_users
# dapodik_employees = dapodik_employees
# dapodik_learning_group = dapodik_learning_group
# dapodik_students = dapodik_students

# # Filter data
# dapodik_employees_name = [(item['nama'], item['nama']) for item in dapodik_employees]
# dapodik_students_name = [(item['nama'], item['nama']) for item in dapodik_students]