#A import requests
# from .headers import headers
# from .api_endpoint import getSekolah, getPengguna, getGtk, getRombonganBelajar, getPesertaDidik

# def get_data_from_api(api_url, headers):
#     try:
#         response = requests.get(api_url, headers=headers)
#         response.raise_for_status()
#         data = response.json()
#         return data.get('rows', [])
#     except requests.exceptions.RequestException as e:
#         return []
    
# # Data School
# dapodik_school = get_data_from_api(getSekolah, headers)
# if dapodik_school:
#     # print(dapodik_school)
#     print('Dapodik School API Connection [OK].')
# else:
#     pass

# # Data Users
# dapodik_users = get_data_from_api(getPengguna, headers)
# if dapodik_users:
#     print('Dapodik Users API Connection [OK].')
# else:
#     pass

# # Data Employees
# dapodik_employees = get_data_from_api(getGtk, headers)
# dapodik_employees_name = [(item['nama'], item['nama']) for item in dapodik_employees]
# if dapodik_employees:
#     print('Dapodik Employees API Connection [OK].')
# else:  
#     pass

# # Data Learning Group
# dapodik_learning_group_raw = get_data_from_api(getRombonganBelajar, headers)
# dapodik_learning_group = [(item['nama'], item['nama']) for item in dapodik_learning_group_raw]
# if dapodik_learning_group_raw:
#     print('Dapodik Learning Group API Connection [OK].')
# else:
#     pass

# # Data Students
# dapodik_students = get_data_from_api(getPesertaDidik, headers)
# dapodik_students_name = [(item['nama'], item['nama']) for item in dapodik_students]
# if dapodik_students:
#     print('Dapodik Students API Connection [OK].\n')
# else:   
#     pass



#B import requests
# from .models import Integrations

# def get_data_from_api(api_url, headers):
#     try:
#         response = requests.get(api_url, headers=headers)
#         response.raise_for_status()
#         data = response.json()
#         return data.get('rows', [])
#     except requests.exceptions.RequestException as e:
#         return []

# def update_api_data():
#     integration = Integrations.objects.get()
#     server_address = integration.server_address
#     npsn = integration.npsn
#     api_token = integration.token

#     base_url = f'http://{server_address}:1162/WebService/'

#     headers = {
#         'Authorization': f'Bearer {api_token}',
#         'Cache-Control': 'no-cache',
#     }

#     # Data School
#     dapodik_school = get_data_from_api(f'{base_url}getSekolah?npsn={npsn}', headers)
#     if dapodik_school:
#         print('Dapodik School API Connection [OK].')

#     # Data Users
#     dapodik_users = get_data_from_api(f'{base_url}getPengguna?npsn={npsn}', headers)
#     if dapodik_users:
#         print('Dapodik Users API Connection [OK].')

#     # Data Employees
#     dapodik_employees = get_data_from_api(f'{base_url}getGtk?npsn={npsn}', headers)
#     if dapodik_employees:
#         print('Dapodik Employees API Connection [OK].')

#     # Data Learning Group
#     dapodik_learning_group_raw = get_data_from_api(f'{base_url}getRombonganBelajar?npsn={npsn}', headers)
#     dapodik_learning_group = [(item['nama'], item['nama']) for item in dapodik_learning_group_raw]
#     if dapodik_learning_group_raw:
#         print('Dapodik Learning Group API Connection [OK].')

#     # Data Students
#     dapodik_students = get_data_from_api(f'{base_url}getPesertaDidik?npsn={npsn}', headers)
#     if dapodik_students:
#         print('Dapodik Students API Connection [OK].\n')

#     return dapodik_school, dapodik_users, dapodik_employees, dapodik_learning_group, dapodik_students

# # Panggil fungsi ini setiap kali Anda ingin memperbarui data
# dapodik_school, dapodik_users, dapodik_employees, dapodik_learning_group, dapodik_students = update_api_data()



import requests
from .models import Integrations

# Fungsi untuk mengambil data dari API
def get_data_from_api(api_url, headers):
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('rows', [])
    except requests.exceptions.RequestException as e:
        return []

# Fungsi untuk memperbarui data dari sumber API
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
    dapodik_school = get_data_from_api(f'{base_url}getSekolah?npsn={npsn}', headers)
    if dapodik_school:
        print('Dapodik School API Connection [OK].')

    # Data Users
    dapodik_users = get_data_from_api(f'{base_url}getPengguna?npsn={npsn}', headers)
    if dapodik_users:
        print('Dapodik Users API Connection [OK].')

    # Data Employees
    dapodik_employees = get_data_from_api(f'{base_url}getGtk?npsn={npsn}', headers)
    if dapodik_employees:
        print('Dapodik Employees API Connection [OK].')

    # Data Learning Group
    dapodik_learning_group_raw = get_data_from_api(f'{base_url}getRombonganBelajar?npsn={npsn}', headers)
    dapodik_learning_group = [(item['nama'], item['nama']) for item in dapodik_learning_group_raw]
    if dapodik_learning_group_raw:
        print('Dapodik Learning Group API Connection [OK].')

    # Data Students
    dapodik_students = get_data_from_api(f'{base_url}getPesertaDidik?npsn={npsn}', headers)
    if dapodik_students:
        print('Dapodik Students API Connection [OK].\n')

    return dapodik_school, dapodik_users, dapodik_employees, dapodik_learning_group, dapodik_students

# Panggil fungsi ini setiap kali Anda ingin memperbarui data
dapodik_school, dapodik_users, dapodik_employees, dapodik_learning_group, dapodik_students = update_api_data()

# Sekarang setel ulang variable-variable yang memegang data sebelumnya
# Anda ingin menggantikannya dengan data baru yang Anda peroleh setelah pembaruan
data_sekolah_sebelumnya = dapodik_school
data_pengguna_sebelumnya = dapodik_users
data_pegawai_sebelumnya = dapodik_employees
data_grup_belajar_sebelumnya = dapodik_learning_group
data_siswa_sebelumnya = dapodik_students

# Selanjutnya, Anda dapat mengakses data-data baru yang diperbarui seperti ini:
# Misalnya, jika Anda ingin mengakses data sekolah setelah pembaruan: