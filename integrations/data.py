import requests
from .headers import headers
from .api_endpoint import getSekolah, getPengguna, getGtk, getRombonganBelajar, getPesertaDidik

# Data School
response = requests.get(getSekolah, headers=headers)

try:
        response.raise_for_status()
        data = response.json()
        dapodik_school = data.get('rows', [])
        print('Dapodik School API Connection [OK].')
        
except requests.exceptions.RequestException as e:
        print('Error:', e)

# Data Users 
response = requests.get(getPengguna, headers=headers)

try:
        response.raise_for_status()
        data = response.json()
        dapodik_users = data.get('rows', [])
        print('Dapodik Users API Connection [OK].')

except requests.exceptions.RequestException as e:
        print('Error:', e)

# Data Employees  
response = requests.get(getGtk, headers=headers)

try:
        response.raise_for_status()
        data = response.json()
        dapodik_employees = data.get('rows', [])
        print('Dapodik Employees API Connection [OK].')

except requests.exceptions.RequestException as e:
        pass

# Data Learning Group  
response = requests.get(getRombonganBelajar, headers=headers)

try:
        response.raise_for_status()
        data = response.json()
        dapodik_employees = data.get('rows', [])
        print('Dapodik Learning Group API Connection [OK].')

except requests.exceptions.RequestException as e:
        pass

# Data Students
response = requests.get(getPesertaDidik, headers=headers)

try:
        response.raise_for_status()
        data = response.json()
        dapodik_students = data.get('rows', [])
        print('Dapodik Students API Connection [OK].\n')

except requests.exceptions.RequestException as e:
        print('Error:', e)

# if response.status_code == 200:
# 	data = response.json()
# 	dapodik_school = data.get('rows', [])
# 	print('Dapodik School API Connection [OK].')
# else:
# 	print('Dapodik School API Connection Failed [ERROR].')

# # Data Users
# response = requests.get(getPengguna, headers=headers)

# if response.status_code == 200:
# 	data = response.json()
# 	dapodik_users = data.get('rows', [])
# 	print('Dapodik Users API Connection [OK].')
# else:
# 	print('Dapodik Users API Connection Failed [ERROR].')

# # Data Employees
# response = requests.get(getGtk, headers=headers)

# if response.status_code == 200:
# 	data = response.json()
# 	dapodik_employees = data.get('rows', [])
# 	print('Dapodik Employees API Connection [OK].')
# else:
# 	print('Dapodik Employees API Connection Failed [ERROR].')

# # Data Students
# response = requests.get(getPesertaDidik, headers=headers)

# if response.status_code == 200:
# 	data = response.json()
# 	dapodik_students = data.get('rows', [])
# 	print('Dapodik Students API Connection [OK].')
# else:
# 	print('Dapodik Students API Connection Failed [ERROR].')